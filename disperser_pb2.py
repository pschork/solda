# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: disperser.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x64isperser.proto\x12\tdisperser\"\x9b\x01\n\x14\x41uthenticatedRequest\x12:\n\x10\x64isperse_request\x18\x01 \x01(\x0b\x32\x1e.disperser.DisperseBlobRequestH\x00\x12<\n\x13\x61uthentication_data\x18\x02 \x01(\x0b\x32\x1d.disperser.AuthenticationDataH\x00\x42\t\n\x07payload\"\x8e\x01\n\x12\x41uthenticatedReply\x12\x35\n\x10\x62lob_auth_header\x18\x01 \x01(\x0b\x32\x19.disperser.BlobAuthHeaderH\x00\x12\x36\n\x0e\x64isperse_reply\x18\x02 \x01(\x0b\x32\x1c.disperser.DisperseBlobReplyH\x00\x42\t\n\x07payload\"-\n\x0e\x42lobAuthHeader\x12\x1b\n\x13\x63hallenge_parameter\x18\x01 \x01(\r\"1\n\x12\x41uthenticationData\x12\x1b\n\x13\x61uthentication_data\x18\x01 \x01(\x0c\"V\n\x13\x44isperseBlobRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x1d\n\x15\x63ustom_quorum_numbers\x18\x02 \x03(\r\x12\x12\n\naccount_id\x18\x03 \x01(\t\"N\n\x11\x44isperseBlobReply\x12%\n\x06result\x18\x01 \x01(\x0e\x32\x15.disperser.BlobStatus\x12\x12\n\nrequest_id\x18\x02 \x01(\x0c\"\'\n\x11\x42lobStatusRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\x0c\"[\n\x0f\x42lobStatusReply\x12%\n\x06status\x18\x01 \x01(\x0e\x32\x15.disperser.BlobStatus\x12!\n\x04info\x18\x02 \x01(\x0b\x32\x13.disperser.BlobInfo\"D\n\x13RetrieveBlobRequest\x12\x19\n\x11\x62\x61tch_header_hash\x18\x01 \x01(\x0c\x12\x12\n\nblob_index\x18\x02 \x01(\r\"!\n\x11RetrieveBlobReply\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"y\n\x08\x42lobInfo\x12*\n\x0b\x62lob_header\x18\x01 \x01(\x0b\x32\x15.disperser.BlobHeader\x12\x41\n\x17\x62lob_verification_proof\x18\x02 \x01(\x0b\x32 .disperser.BlobVerificationProof\"$\n\x0cG1Commitment\x12\t\n\x01x\x18\x01 \x01(\x0c\x12\t\n\x01y\x18\x02 \x01(\x0c\"\x86\x01\n\nBlobHeader\x12+\n\ncommitment\x18\x01 \x01(\x0b\x32\x17.disperser.G1Commitment\x12\x13\n\x0b\x64\x61ta_length\x18\x02 \x01(\r\x12\x36\n\x12\x62lob_quorum_params\x18\x03 \x03(\x0b\x32\x1a.disperser.BlobQuorumParam\"\x91\x01\n\x0f\x42lobQuorumParam\x12\x15\n\rquorum_number\x18\x01 \x01(\r\x12&\n\x1e\x61\x64versary_threshold_percentage\x18\x02 \x01(\r\x12)\n!confirmation_threshold_percentage\x18\x03 \x01(\r\x12\x14\n\x0c\x63hunk_length\x18\x04 \x01(\r\"\xa0\x01\n\x15\x42lobVerificationProof\x12\x10\n\x08\x62\x61tch_id\x18\x01 \x01(\r\x12\x12\n\nblob_index\x18\x02 \x01(\r\x12\x30\n\x0e\x62\x61tch_metadata\x18\x03 \x01(\x0b\x32\x18.disperser.BatchMetadata\x12\x17\n\x0finclusion_proof\x18\x04 \x01(\x0c\x12\x16\n\x0equorum_indexes\x18\x05 \x01(\x0c\"\xa7\x01\n\rBatchMetadata\x12,\n\x0c\x62\x61tch_header\x18\x01 \x01(\x0b\x32\x16.disperser.BatchHeader\x12\x1d\n\x15signatory_record_hash\x18\x02 \x01(\x0c\x12\x0b\n\x03\x66\x65\x65\x18\x03 \x01(\x0c\x12!\n\x19\x63onfirmation_block_number\x18\x04 \x01(\r\x12\x19\n\x11\x62\x61tch_header_hash\x18\x05 \x01(\x0c\"|\n\x0b\x42\x61tchHeader\x12\x12\n\nbatch_root\x18\x01 \x01(\x0c\x12\x16\n\x0equorum_numbers\x18\x02 \x01(\x0c\x12!\n\x19quorum_signed_percentages\x18\x03 \x01(\x0c\x12\x1e\n\x16reference_block_number\x18\x04 \x01(\r*\x80\x01\n\nBlobStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nPROCESSING\x10\x01\x12\r\n\tCONFIRMED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x12\r\n\tFINALIZED\x10\x04\x12\x1b\n\x17INSUFFICIENT_SIGNATURES\x10\x05\x12\x0e\n\nDISPERSING\x10\x06\x32\xd9\x02\n\tDisperser\x12N\n\x0c\x44isperseBlob\x12\x1e.disperser.DisperseBlobRequest\x1a\x1c.disperser.DisperseBlobReply\"\x00\x12_\n\x19\x44isperseBlobAuthenticated\x12\x1f.disperser.AuthenticatedRequest\x1a\x1d.disperser.AuthenticatedReply(\x01\x30\x01\x12K\n\rGetBlobStatus\x12\x1c.disperser.BlobStatusRequest\x1a\x1a.disperser.BlobStatusReply\"\x00\x12N\n\x0cRetrieveBlob\x12\x1e.disperser.RetrieveBlobRequest\x1a\x1c.disperser.RetrieveBlobReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'disperser_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BLOBSTATUS']._serialized_start=1744
  _globals['_BLOBSTATUS']._serialized_end=1872
  _globals['_AUTHENTICATEDREQUEST']._serialized_start=31
  _globals['_AUTHENTICATEDREQUEST']._serialized_end=186
  _globals['_AUTHENTICATEDREPLY']._serialized_start=189
  _globals['_AUTHENTICATEDREPLY']._serialized_end=331
  _globals['_BLOBAUTHHEADER']._serialized_start=333
  _globals['_BLOBAUTHHEADER']._serialized_end=378
  _globals['_AUTHENTICATIONDATA']._serialized_start=380
  _globals['_AUTHENTICATIONDATA']._serialized_end=429
  _globals['_DISPERSEBLOBREQUEST']._serialized_start=431
  _globals['_DISPERSEBLOBREQUEST']._serialized_end=517
  _globals['_DISPERSEBLOBREPLY']._serialized_start=519
  _globals['_DISPERSEBLOBREPLY']._serialized_end=597
  _globals['_BLOBSTATUSREQUEST']._serialized_start=599
  _globals['_BLOBSTATUSREQUEST']._serialized_end=638
  _globals['_BLOBSTATUSREPLY']._serialized_start=640
  _globals['_BLOBSTATUSREPLY']._serialized_end=731
  _globals['_RETRIEVEBLOBREQUEST']._serialized_start=733
  _globals['_RETRIEVEBLOBREQUEST']._serialized_end=801
  _globals['_RETRIEVEBLOBREPLY']._serialized_start=803
  _globals['_RETRIEVEBLOBREPLY']._serialized_end=836
  _globals['_BLOBINFO']._serialized_start=838
  _globals['_BLOBINFO']._serialized_end=959
  _globals['_G1COMMITMENT']._serialized_start=961
  _globals['_G1COMMITMENT']._serialized_end=997
  _globals['_BLOBHEADER']._serialized_start=1000
  _globals['_BLOBHEADER']._serialized_end=1134
  _globals['_BLOBQUORUMPARAM']._serialized_start=1137
  _globals['_BLOBQUORUMPARAM']._serialized_end=1282
  _globals['_BLOBVERIFICATIONPROOF']._serialized_start=1285
  _globals['_BLOBVERIFICATIONPROOF']._serialized_end=1445
  _globals['_BATCHMETADATA']._serialized_start=1448
  _globals['_BATCHMETADATA']._serialized_end=1615
  _globals['_BATCHHEADER']._serialized_start=1617
  _globals['_BATCHHEADER']._serialized_end=1741
  _globals['_DISPERSER']._serialized_start=1875
  _globals['_DISPERSER']._serialized_end=2220
# @@protoc_insertion_point(module_scope)
