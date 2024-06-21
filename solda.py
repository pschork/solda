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

MAX_SIZE = 2 * 1024 * 1024  # 2 MiB
CHUNK_SIZE = 32  # 32 bytes
VALID_RANGE = 21888242871839275222246405745257275088548364400416034343698204186575808495617

def chunk_encode(data):
    length_prefix = len(data).to_bytes(4, 'big')
    total_length = len(length_prefix) + len(data)
    padding_length = (CHUNK_SIZE - (total_length % CHUNK_SIZE)) % CHUNK_SIZE
    padded_bytes = length_prefix + data + b'\x00' * padding_length
    chunks = [padded_bytes[i:i + CHUNK_SIZE] for i in range(0, len(padded_bytes), CHUNK_SIZE)]

    # Ensure the chunk values are within VALID_RANGE
    valid_chunks = []
    for chunk in chunks:
        chunk_value = int.from_bytes(chunk, 'big')
        if chunk_value >= VALID_RANGE:
            chunk_value %= VALID_RANGE
            chunk = chunk_value.to_bytes(CHUNK_SIZE, 'big')
        valid_chunks.append(chunk)

    return b''.join(valid_chunks)

def chunk_decode(data):
    if len(data) % CHUNK_SIZE != 0:
        raise ValueError("Data length is not a multiple of the chunk size.")

    combined_bytes = b''.join([data[i:i + CHUNK_SIZE] for i in range(0, len(data), CHUNK_SIZE)])
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

request = disperser_pb2.DisperseBlobRequest(
    data=snappy_data,
    account_id=ACCOUNT
)
disperse_blob(request)
