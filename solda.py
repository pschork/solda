import json
import os
import snappy

import grpc
from dotenv import load_dotenv
from solana.rpc.api import Client
from solana.rpc.websocket_api import connect

import disperser_pb2
import disperser_pb2_grpc

load_dotenv()
RPC_ENDPOINT = os.getenv('RPC_ENDPOINT')
GRPC_ENDPOINT = os.getenv('GRPC_ENDPOINT')
ACCOUNT = os.getenv('ACCOUNT')

CHUNK_SIZE = 31  # 31 bytes

def chunk_encode(data):
    length_prefix = len(data).to_bytes(4, 'big')
    total_length = len(length_prefix) + len(data)
    padding_length = (CHUNK_SIZE - (total_length % CHUNK_SIZE)) % CHUNK_SIZE
    padded_bytes = length_prefix + data + b'\x00' * padding_length
    chunks = [padded_bytes[i:i + CHUNK_SIZE] for i in range(0, len(padded_bytes), CHUNK_SIZE)]

    # With big endian, set first byte as 0 to ensure data is within valid range of bn254 curve
    prefixed_chunks = [b'\x00' + chunk for chunk in chunks]

    return b''.join(prefixed_chunks)


def chunk_decode(data):
    if len(data) % (CHUNK_SIZE + 1) != 0:
        raise ValueError("Data length is not a multiple of the chunk size plus one.")

    combined_bytes = b''.join([data[i+1:i+1 + CHUNK_SIZE] for i in range(0, len(data), CHUNK_SIZE + 1)])
    length_prefix = combined_bytes[:4]
    json_length = int.from_bytes(length_prefix, 'big')
    return combined_bytes[4:4 + json_length]


def disperse_blob(request):
    channel = grpc.secure_channel(GRPC_ENDPOINT, grpc.ssl_channel_credentials())
    client = disperser_pb2_grpc.DisperserStub(channel)
    response = client.DisperseBlob(request)
    print(response)

sol = Client(RPC_ENDPOINT)
slot = sol.get_slot().value
block = sol.get_block(slot, encoding="json", max_supported_transaction_version=0).value
json_data = block.to_json().encode("utf-8")
json_size = len(json_data)/1024/1024
snappy_data = chunk_encode(snappy.compress(json_data))
snappy_size = len(snappy_data)/1024/1024

print(f'Block {slot} {block.blockhash} json:{json_size:.1f}MB snappy:{snappy_size:.1f}MB' )

#assert snappy.decompress(chunk_decode(snappy_data)) == json_data

request = disperser_pb2.DisperseBlobRequest(
    data=snappy_data,
    account_id=ACCOUNT
)
disperse_blob(request)
