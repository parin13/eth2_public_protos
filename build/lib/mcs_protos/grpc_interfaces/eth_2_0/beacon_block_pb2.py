# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: beacon_block.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .import attestation_pb2 as attestation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='beacon_block.proto',
  package='ethereum.eth.v1alpha1',
  syntax='proto3',
  serialized_options=_b('\n\031org.ethereum.eth.v1alpha1B\020BeaconBlockProtoP\001Z6github.com/prysmaticlabs/ethereumapis/eth/v1alpha1;eth\252\002\025Ethereum.Eth.v1alpha1\312\002\025Ethereum\\Eth\\v1alpha1'),
  serialized_pb=_b('\n\x12\x62\x65\x61\x63on_block.proto\x12\x15\x65thereum.eth.v1alpha1\x1a\x11\x61ttestation.proto\"\x92\x01\n\x0b\x42\x65\x61\x63onBlock\x12\x0c\n\x04slot\x18\x01 \x01(\x04\x12\x16\n\x0eproposer_index\x18\x02 \x01(\x04\x12\x13\n\x0bparent_root\x18\x03 \x01(\x0c\x12\x12\n\nstate_root\x18\x04 \x01(\x0c\x12\x34\n\x04\x62ody\x18\x05 \x01(\x0b\x32&.ethereum.eth.v1alpha1.BeaconBlockBody\"Y\n\x11SignedBeaconBlock\x12\x31\n\x05\x62lock\x18\x01 \x01(\x0b\x32\".ethereum.eth.v1alpha1.BeaconBlock\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"\xa9\x03\n\x0f\x42\x65\x61\x63onBlockBody\x12\x15\n\rrandao_reveal\x18\x01 \x01(\x0c\x12\x32\n\teth1_data\x18\x02 \x01(\x0b\x32\x1f.ethereum.eth.v1alpha1.Eth1Data\x12\x10\n\x08graffiti\x18\x03 \x01(\x0c\x12\x43\n\x12proposer_slashings\x18\x04 \x03(\x0b\x32\'.ethereum.eth.v1alpha1.ProposerSlashing\x12\x43\n\x12\x61ttester_slashings\x18\x05 \x03(\x0b\x32\'.ethereum.eth.v1alpha1.AttesterSlashing\x12\x38\n\x0c\x61ttestations\x18\x06 \x03(\x0b\x32\".ethereum.eth.v1alpha1.Attestation\x12\x30\n\x08\x64\x65posits\x18\x07 \x03(\x0b\x32\x1e.ethereum.eth.v1alpha1.Deposit\x12\x43\n\x0fvoluntary_exits\x18\x08 \x03(\x0b\x32*.ethereum.eth.v1alpha1.SignedVoluntaryExit\"\x96\x01\n\x10ProposerSlashing\x12@\n\x08header_1\x18\x02 \x01(\x0b\x32..ethereum.eth.v1alpha1.SignedBeaconBlockHeader\x12@\n\x08header_2\x18\x03 \x01(\x0b\x32..ethereum.eth.v1alpha1.SignedBeaconBlockHeader\"\x96\x01\n\x10\x41ttesterSlashing\x12@\n\rattestation_1\x18\x01 \x01(\x0b\x32).ethereum.eth.v1alpha1.IndexedAttestation\x12@\n\rattestation_2\x18\x02 \x01(\x0b\x32).ethereum.eth.v1alpha1.IndexedAttestation\"\xaa\x01\n\x07\x44\x65posit\x12\r\n\x05proof\x18\x01 \x03(\x0c\x12\x31\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32#.ethereum.eth.v1alpha1.Deposit.Data\x1a]\n\x04\x44\x61ta\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12\x1e\n\x16withdrawal_credentials\x18\x02 \x01(\x0c\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x04\x12\x11\n\tsignature\x18\x04 \x01(\x0c\"7\n\rVoluntaryExit\x12\r\n\x05\x65poch\x18\x01 \x01(\x04\x12\x17\n\x0fvalidator_index\x18\x02 \x01(\x04\"\\\n\x13SignedVoluntaryExit\x12\x32\n\x04\x65xit\x18\x01 \x01(\x0b\x32$.ethereum.eth.v1alpha1.VoluntaryExit\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"K\n\x08\x45th1Data\x12\x14\n\x0c\x64\x65posit_root\x18\x01 \x01(\x0c\x12\x15\n\rdeposit_count\x18\x02 \x01(\x04\x12\x12\n\nblock_hash\x18\x03 \x01(\x0c\"u\n\x11\x42\x65\x61\x63onBlockHeader\x12\x0c\n\x04slot\x18\x01 \x01(\x04\x12\x16\n\x0eproposer_index\x18\x02 \x01(\x04\x12\x13\n\x0bparent_root\x18\x03 \x01(\x0c\x12\x12\n\nstate_root\x18\x04 \x01(\x0c\x12\x11\n\tbody_root\x18\x05 \x01(\x0c\"f\n\x17SignedBeaconBlockHeader\x12\x38\n\x06header\x18\x01 \x01(\x0b\x32(.ethereum.eth.v1alpha1.BeaconBlockHeader\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"x\n\x12IndexedAttestation\x12\x19\n\x11\x61ttesting_indices\x18\x01 \x03(\x04\x12\x34\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32&.ethereum.eth.v1alpha1.AttestationData\x12\x11\n\tsignature\x18\x03 \x01(\x0c\x42\x97\x01\n\x19org.ethereum.eth.v1alpha1B\x10\x42\x65\x61\x63onBlockProtoP\x01Z6github.com/prysmaticlabs/ethereumapis/eth/v1alpha1;eth\xaa\x02\x15\x45thereum.Eth.v1alpha1\xca\x02\x15\x45thereum\\Eth\\v1alpha1b\x06proto3')
  ,
  dependencies=[attestation__pb2.DESCRIPTOR,])




_BEACONBLOCK = _descriptor.Descriptor(
  name='BeaconBlock',
  full_name='ethereum.eth.v1alpha1.BeaconBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slot', full_name='ethereum.eth.v1alpha1.BeaconBlock.slot', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposer_index', full_name='ethereum.eth.v1alpha1.BeaconBlock.proposer_index', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_root', full_name='ethereum.eth.v1alpha1.BeaconBlock.parent_root', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_root', full_name='ethereum.eth.v1alpha1.BeaconBlock.state_root', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='ethereum.eth.v1alpha1.BeaconBlock.body', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=211,
)


_SIGNEDBEACONBLOCK = _descriptor.Descriptor(
  name='SignedBeaconBlock',
  full_name='ethereum.eth.v1alpha1.SignedBeaconBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block', full_name='ethereum.eth.v1alpha1.SignedBeaconBlock.block', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='ethereum.eth.v1alpha1.SignedBeaconBlock.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=302,
)


_BEACONBLOCKBODY = _descriptor.Descriptor(
  name='BeaconBlockBody',
  full_name='ethereum.eth.v1alpha1.BeaconBlockBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='randao_reveal', full_name='ethereum.eth.v1alpha1.BeaconBlockBody.randao_reveal', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eth1_data', full_name='ethereum.eth.v1alpha1.BeaconBlockBody.eth1_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graffiti', full_name='ethereum.eth.v1alpha1.BeaconBlockBody.graffiti', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposer_slashings', full_name='ethereum.eth.v1alpha1.BeaconBlockBody.proposer_slashings', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attester_slashings', full_name='ethereum.eth.v1alpha1.BeaconBlockBody.attester_slashings', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attestations', full_name='ethereum.eth.v1alpha1.BeaconBlockBody.attestations', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deposits', full_name='ethereum.eth.v1alpha1.BeaconBlockBody.deposits', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voluntary_exits', full_name='ethereum.eth.v1alpha1.BeaconBlockBody.voluntary_exits', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=730,
)


_PROPOSERSLASHING = _descriptor.Descriptor(
  name='ProposerSlashing',
  full_name='ethereum.eth.v1alpha1.ProposerSlashing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header_1', full_name='ethereum.eth.v1alpha1.ProposerSlashing.header_1', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header_2', full_name='ethereum.eth.v1alpha1.ProposerSlashing.header_2', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=733,
  serialized_end=883,
)


_ATTESTERSLASHING = _descriptor.Descriptor(
  name='AttesterSlashing',
  full_name='ethereum.eth.v1alpha1.AttesterSlashing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attestation_1', full_name='ethereum.eth.v1alpha1.AttesterSlashing.attestation_1', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attestation_2', full_name='ethereum.eth.v1alpha1.AttesterSlashing.attestation_2', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=886,
  serialized_end=1036,
)


_DEPOSIT_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='ethereum.eth.v1alpha1.Deposit.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='ethereum.eth.v1alpha1.Deposit.Data.public_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withdrawal_credentials', full_name='ethereum.eth.v1alpha1.Deposit.Data.withdrawal_credentials', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='ethereum.eth.v1alpha1.Deposit.Data.amount', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='ethereum.eth.v1alpha1.Deposit.Data.signature', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1116,
  serialized_end=1209,
)

_DEPOSIT = _descriptor.Descriptor(
  name='Deposit',
  full_name='ethereum.eth.v1alpha1.Deposit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proof', full_name='ethereum.eth.v1alpha1.Deposit.proof', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='ethereum.eth.v1alpha1.Deposit.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEPOSIT_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1039,
  serialized_end=1209,
)


_VOLUNTARYEXIT = _descriptor.Descriptor(
  name='VoluntaryExit',
  full_name='ethereum.eth.v1alpha1.VoluntaryExit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='epoch', full_name='ethereum.eth.v1alpha1.VoluntaryExit.epoch', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validator_index', full_name='ethereum.eth.v1alpha1.VoluntaryExit.validator_index', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1211,
  serialized_end=1266,
)


_SIGNEDVOLUNTARYEXIT = _descriptor.Descriptor(
  name='SignedVoluntaryExit',
  full_name='ethereum.eth.v1alpha1.SignedVoluntaryExit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exit', full_name='ethereum.eth.v1alpha1.SignedVoluntaryExit.exit', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='ethereum.eth.v1alpha1.SignedVoluntaryExit.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1268,
  serialized_end=1360,
)


_ETH1DATA = _descriptor.Descriptor(
  name='Eth1Data',
  full_name='ethereum.eth.v1alpha1.Eth1Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deposit_root', full_name='ethereum.eth.v1alpha1.Eth1Data.deposit_root', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deposit_count', full_name='ethereum.eth.v1alpha1.Eth1Data.deposit_count', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_hash', full_name='ethereum.eth.v1alpha1.Eth1Data.block_hash', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1362,
  serialized_end=1437,
)


_BEACONBLOCKHEADER = _descriptor.Descriptor(
  name='BeaconBlockHeader',
  full_name='ethereum.eth.v1alpha1.BeaconBlockHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slot', full_name='ethereum.eth.v1alpha1.BeaconBlockHeader.slot', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposer_index', full_name='ethereum.eth.v1alpha1.BeaconBlockHeader.proposer_index', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_root', full_name='ethereum.eth.v1alpha1.BeaconBlockHeader.parent_root', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_root', full_name='ethereum.eth.v1alpha1.BeaconBlockHeader.state_root', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body_root', full_name='ethereum.eth.v1alpha1.BeaconBlockHeader.body_root', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1439,
  serialized_end=1556,
)


_SIGNEDBEACONBLOCKHEADER = _descriptor.Descriptor(
  name='SignedBeaconBlockHeader',
  full_name='ethereum.eth.v1alpha1.SignedBeaconBlockHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='ethereum.eth.v1alpha1.SignedBeaconBlockHeader.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='ethereum.eth.v1alpha1.SignedBeaconBlockHeader.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1558,
  serialized_end=1660,
)


_INDEXEDATTESTATION = _descriptor.Descriptor(
  name='IndexedAttestation',
  full_name='ethereum.eth.v1alpha1.IndexedAttestation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attesting_indices', full_name='ethereum.eth.v1alpha1.IndexedAttestation.attesting_indices', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='ethereum.eth.v1alpha1.IndexedAttestation.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='ethereum.eth.v1alpha1.IndexedAttestation.signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1662,
  serialized_end=1782,
)

_BEACONBLOCK.fields_by_name['body'].message_type = _BEACONBLOCKBODY
_SIGNEDBEACONBLOCK.fields_by_name['block'].message_type = _BEACONBLOCK
_BEACONBLOCKBODY.fields_by_name['eth1_data'].message_type = _ETH1DATA
_BEACONBLOCKBODY.fields_by_name['proposer_slashings'].message_type = _PROPOSERSLASHING
_BEACONBLOCKBODY.fields_by_name['attester_slashings'].message_type = _ATTESTERSLASHING
_BEACONBLOCKBODY.fields_by_name['attestations'].message_type = attestation__pb2._ATTESTATION
_BEACONBLOCKBODY.fields_by_name['deposits'].message_type = _DEPOSIT
_BEACONBLOCKBODY.fields_by_name['voluntary_exits'].message_type = _SIGNEDVOLUNTARYEXIT
_PROPOSERSLASHING.fields_by_name['header_1'].message_type = _SIGNEDBEACONBLOCKHEADER
_PROPOSERSLASHING.fields_by_name['header_2'].message_type = _SIGNEDBEACONBLOCKHEADER
_ATTESTERSLASHING.fields_by_name['attestation_1'].message_type = _INDEXEDATTESTATION
_ATTESTERSLASHING.fields_by_name['attestation_2'].message_type = _INDEXEDATTESTATION
_DEPOSIT_DATA.containing_type = _DEPOSIT
_DEPOSIT.fields_by_name['data'].message_type = _DEPOSIT_DATA
_SIGNEDVOLUNTARYEXIT.fields_by_name['exit'].message_type = _VOLUNTARYEXIT
_SIGNEDBEACONBLOCKHEADER.fields_by_name['header'].message_type = _BEACONBLOCKHEADER
_INDEXEDATTESTATION.fields_by_name['data'].message_type = attestation__pb2._ATTESTATIONDATA
DESCRIPTOR.message_types_by_name['BeaconBlock'] = _BEACONBLOCK
DESCRIPTOR.message_types_by_name['SignedBeaconBlock'] = _SIGNEDBEACONBLOCK
DESCRIPTOR.message_types_by_name['BeaconBlockBody'] = _BEACONBLOCKBODY
DESCRIPTOR.message_types_by_name['ProposerSlashing'] = _PROPOSERSLASHING
DESCRIPTOR.message_types_by_name['AttesterSlashing'] = _ATTESTERSLASHING
DESCRIPTOR.message_types_by_name['Deposit'] = _DEPOSIT
DESCRIPTOR.message_types_by_name['VoluntaryExit'] = _VOLUNTARYEXIT
DESCRIPTOR.message_types_by_name['SignedVoluntaryExit'] = _SIGNEDVOLUNTARYEXIT
DESCRIPTOR.message_types_by_name['Eth1Data'] = _ETH1DATA
DESCRIPTOR.message_types_by_name['BeaconBlockHeader'] = _BEACONBLOCKHEADER
DESCRIPTOR.message_types_by_name['SignedBeaconBlockHeader'] = _SIGNEDBEACONBLOCKHEADER
DESCRIPTOR.message_types_by_name['IndexedAttestation'] = _INDEXEDATTESTATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BeaconBlock = _reflection.GeneratedProtocolMessageType('BeaconBlock', (_message.Message,), {
  'DESCRIPTOR' : _BEACONBLOCK,
  '__module__' : 'beacon_block_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.BeaconBlock)
  })
_sym_db.RegisterMessage(BeaconBlock)

SignedBeaconBlock = _reflection.GeneratedProtocolMessageType('SignedBeaconBlock', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDBEACONBLOCK,
  '__module__' : 'beacon_block_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.SignedBeaconBlock)
  })
_sym_db.RegisterMessage(SignedBeaconBlock)

BeaconBlockBody = _reflection.GeneratedProtocolMessageType('BeaconBlockBody', (_message.Message,), {
  'DESCRIPTOR' : _BEACONBLOCKBODY,
  '__module__' : 'beacon_block_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.BeaconBlockBody)
  })
_sym_db.RegisterMessage(BeaconBlockBody)

ProposerSlashing = _reflection.GeneratedProtocolMessageType('ProposerSlashing', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSERSLASHING,
  '__module__' : 'beacon_block_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.ProposerSlashing)
  })
_sym_db.RegisterMessage(ProposerSlashing)

AttesterSlashing = _reflection.GeneratedProtocolMessageType('AttesterSlashing', (_message.Message,), {
  'DESCRIPTOR' : _ATTESTERSLASHING,
  '__module__' : 'beacon_block_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.AttesterSlashing)
  })
_sym_db.RegisterMessage(AttesterSlashing)

Deposit = _reflection.GeneratedProtocolMessageType('Deposit', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _DEPOSIT_DATA,
    '__module__' : 'beacon_block_pb2'
    # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.Deposit.Data)
    })
  ,
  'DESCRIPTOR' : _DEPOSIT,
  '__module__' : 'beacon_block_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.Deposit)
  })
_sym_db.RegisterMessage(Deposit)
_sym_db.RegisterMessage(Deposit.Data)

VoluntaryExit = _reflection.GeneratedProtocolMessageType('VoluntaryExit', (_message.Message,), {
  'DESCRIPTOR' : _VOLUNTARYEXIT,
  '__module__' : 'beacon_block_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.VoluntaryExit)
  })
_sym_db.RegisterMessage(VoluntaryExit)

SignedVoluntaryExit = _reflection.GeneratedProtocolMessageType('SignedVoluntaryExit', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDVOLUNTARYEXIT,
  '__module__' : 'beacon_block_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.SignedVoluntaryExit)
  })
_sym_db.RegisterMessage(SignedVoluntaryExit)

Eth1Data = _reflection.GeneratedProtocolMessageType('Eth1Data', (_message.Message,), {
  'DESCRIPTOR' : _ETH1DATA,
  '__module__' : 'beacon_block_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.Eth1Data)
  })
_sym_db.RegisterMessage(Eth1Data)

BeaconBlockHeader = _reflection.GeneratedProtocolMessageType('BeaconBlockHeader', (_message.Message,), {
  'DESCRIPTOR' : _BEACONBLOCKHEADER,
  '__module__' : 'beacon_block_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.BeaconBlockHeader)
  })
_sym_db.RegisterMessage(BeaconBlockHeader)

SignedBeaconBlockHeader = _reflection.GeneratedProtocolMessageType('SignedBeaconBlockHeader', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDBEACONBLOCKHEADER,
  '__module__' : 'beacon_block_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.SignedBeaconBlockHeader)
  })
_sym_db.RegisterMessage(SignedBeaconBlockHeader)

IndexedAttestation = _reflection.GeneratedProtocolMessageType('IndexedAttestation', (_message.Message,), {
  'DESCRIPTOR' : _INDEXEDATTESTATION,
  '__module__' : 'beacon_block_pb2'
  # @@protoc_insertion_point(class_scope:ethereum.eth.v1alpha1.IndexedAttestation)
  })
_sym_db.RegisterMessage(IndexedAttestation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
