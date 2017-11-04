# coding=utf-8
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zipai.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='zipai.proto',
    package='',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x0bzipai.proto\"D\n\rCalculateData\x12\x0f\n\x07\x61llocid\x18\x01 \x01(\x05\x12\x10\n\x08handlist\x18\x02 \x03(\x05\x12\x10\n\x08penglist\x18\x03 \x03(\x05\"V\n\x0f\x43\x61lculateResult\x12\x0f\n\x07\x63hilist\x18\x01 \x03(\x05\x12\x10\n\x08penglist\x18\x02 \x03(\x05\x12\x10\n\x08zhaolist\x18\x03 \x03(\x05\x12\x0e\n\x06hulist\x18\x04 \x03(\x05\"\xad\x01\n\nSettleData\x12\x0f\n\x07\x61llocid\x18\x01 \x01(\x05\x12\x10\n\x08huUserId\x18\x02 \x01(\x05\x12\x0e\n\x06huCard\x18\x03 \x01(\x05\x12\'\n\x0esettlePatterns\x18\x04 \x03(\x0e\x32\x0f.SettlePatterns\x12\r\n\x05\x64\x61gun\x18\x05 \x01(\x08\x12\x0b\n\x03qia\x18\x06 \x01(\x08\x12\'\n\x0euserSettleData\x18\x07 \x03(\x0b\x32\x0f.UserSettleData\"\x8a\x01\n\x0eUserSettleData\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x0f\n\x07\x63hilist\x18\x02 \x03(\x05\x12\x10\n\x08penglist\x18\x03 \x03(\x05\x12\x0f\n\x07kanlist\x18\x04 \x03(\x05\x12\x10\n\x08zhaolist\x18\x05 \x03(\x05\x12\x10\n\x08longlist\x18\x06 \x03(\x05\x12\x10\n\x08handlist\x18\x07 \x03(\x05\";\n\x0cSettleResult\x12+\n\x10userSettleResule\x18\x01 \x03(\x0b\x32\x11.UserSettleResult\"t\n\x10UserSettleResult\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\n\n\x02hu\x18\x02 \x01(\x05\x12\x0c\n\x04\x62\x61ng\x18\x03 \x01(\x05\x12\r\n\x05score\x18\x04 \x01(\x05\x12\'\n\x0esettlePatterns\x18\x05 \x03(\x0e\x32\x0f.SettlePatterns\"U\n\x0bShuffleData\x12\x0f\n\x07\x61llocid\x18\x01 \x01(\x05\x12%\n\ruserCardLevel\x18\x02 \x03(\x0b\x32\x0e.UserCardLevel\x12\x0e\n\x06\x62\x61nker\x18\x03 \x01(\x05\".\n\rUserCardLevel\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\r\n\x05level\x18\x02 \x01(\x05\"D\n\rShuffleResult\x12\x14\n\x0csurplusCards\x18\x01 \x03(\x05\x12\x1d\n\tdealCards\x18\x02 \x03(\x0b\x32\n.DealCards\"q\n\tDealCards\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x10\n\x08\x63\x61rdlist\x18\x02 \x03(\x05\x12\x10\n\x08penglist\x18\x03 \x03(\x05\x12\x10\n\x08zhaolist\x18\x04 \x03(\x05\x12\x0e\n\x06hulist\x18\x05 \x03(\x05\x12\x0e\n\x06tianhu\x18\x06 \x01(\x08*^\n\x0eSettlePatterns\x12\n\n\x06HONGHU\x10\x00\x12\t\n\x05HEIHU\x10\x01\x12\n\n\x06TIANHU\x10\x02\x12\x08\n\x04\x44IHU\x10\x03\x12\t\n\x05LANHU\x10\x04\x12\x08\n\x04ZIMO\x10\x05\x12\n\n\x06PIAOHU\x10\x06\x32\x8b\x01\n\x05Zipai\x12/\n\tcalculate\x12\x0e.CalculateData\x1a\x10.CalculateResult\"\x00\x12&\n\x06settle\x12\x0b.SettleData\x1a\r.SettleResult\"\x00\x12)\n\x07shuffle\x12\x0c.ShuffleData\x1a\x0e.ShuffleResult\"\x00\x42\x1b\n\x10zipai.mode.protoB\x05ZipaiP\x01\x62\x06proto3')
)

_SETTLEPATTERNS = _descriptor.EnumDescriptor(
    name='SettlePatterns',
    full_name='SettlePatterns',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='HONGHU', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='HEIHU', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='TIANHU', index=2, number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='DIHU', index=3, number=3,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='LANHU', index=4, number=4,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ZIMO', index=5, number=5,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='PIAOHU', index=6, number=6,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=989,
    serialized_end=1083,
)
_sym_db.RegisterEnumDescriptor(_SETTLEPATTERNS)

SettlePatterns = enum_type_wrapper.EnumTypeWrapper(_SETTLEPATTERNS)
HONGHU = 0
HEIHU = 1
TIANHU = 2
DIHU = 3
LANHU = 4
ZIMO = 5
PIAOHU = 6

_CALCULATEDATA = _descriptor.Descriptor(
    name='CalculateData',
    full_name='CalculateData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='allocid', full_name='CalculateData.allocid', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='handlist', full_name='CalculateData.handlist', index=1,
            number=2, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='penglist', full_name='CalculateData.penglist', index=2,
            number=3, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=15,
    serialized_end=83,
)

_CALCULATERESULT = _descriptor.Descriptor(
    name='CalculateResult',
    full_name='CalculateResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='chilist', full_name='CalculateResult.chilist', index=0,
            number=1, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='penglist', full_name='CalculateResult.penglist', index=1,
            number=2, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='zhaolist', full_name='CalculateResult.zhaolist', index=2,
            number=3, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='hulist', full_name='CalculateResult.hulist', index=3,
            number=4, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=85,
    serialized_end=171,
)

_SETTLEDATA = _descriptor.Descriptor(
    name='SettleData',
    full_name='SettleData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='allocid', full_name='SettleData.allocid', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='huUserId', full_name='SettleData.huUserId', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='huCard', full_name='SettleData.huCard', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='settlePatterns', full_name='SettleData.settlePatterns', index=3,
            number=4, type=14, cpp_type=8, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='dagun', full_name='SettleData.dagun', index=4,
            number=5, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='qia', full_name='SettleData.qia', index=5,
            number=6, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='userSettleData', full_name='SettleData.userSettleData', index=6,
            number=7, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=174,
    serialized_end=347,
)

_USERSETTLEDATA = _descriptor.Descriptor(
    name='UserSettleData',
    full_name='UserSettleData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='userId', full_name='UserSettleData.userId', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='chilist', full_name='UserSettleData.chilist', index=1,
            number=2, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='penglist', full_name='UserSettleData.penglist', index=2,
            number=3, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='kanlist', full_name='UserSettleData.kanlist', index=3,
            number=4, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='zhaolist', full_name='UserSettleData.zhaolist', index=4,
            number=5, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='longlist', full_name='UserSettleData.longlist', index=5,
            number=6, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='handlist', full_name='UserSettleData.handlist', index=6,
            number=7, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=350,
    serialized_end=488,
)

_SETTLERESULT = _descriptor.Descriptor(
    name='SettleResult',
    full_name='SettleResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='userSettleResule', full_name='SettleResult.userSettleResule', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=490,
    serialized_end=549,
)

_USERSETTLERESULT = _descriptor.Descriptor(
    name='UserSettleResult',
    full_name='UserSettleResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='userId', full_name='UserSettleResult.userId', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='hu', full_name='UserSettleResult.hu', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='bang', full_name='UserSettleResult.bang', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='score', full_name='UserSettleResult.score', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='settlePatterns', full_name='UserSettleResult.settlePatterns', index=4,
            number=5, type=14, cpp_type=8, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=551,
    serialized_end=667,
)

_SHUFFLEDATA = _descriptor.Descriptor(
    name='ShuffleData',
    full_name='ShuffleData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='allocid', full_name='ShuffleData.allocid', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='userCardLevel', full_name='ShuffleData.userCardLevel', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='banker', full_name='ShuffleData.banker', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=669,
    serialized_end=754,
)

_USERCARDLEVEL = _descriptor.Descriptor(
    name='UserCardLevel',
    full_name='UserCardLevel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='userId', full_name='UserCardLevel.userId', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='level', full_name='UserCardLevel.level', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=756,
    serialized_end=802,
)

_SHUFFLERESULT = _descriptor.Descriptor(
    name='ShuffleResult',
    full_name='ShuffleResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='surplusCards', full_name='ShuffleResult.surplusCards', index=0,
            number=1, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='dealCards', full_name='ShuffleResult.dealCards', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=804,
    serialized_end=872,
)

_DEALCARDS = _descriptor.Descriptor(
    name='DealCards',
    full_name='DealCards',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='userId', full_name='DealCards.userId', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='cardlist', full_name='DealCards.cardlist', index=1,
            number=2, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='penglist', full_name='DealCards.penglist', index=2,
            number=3, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='zhaolist', full_name='DealCards.zhaolist', index=3,
            number=4, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='hulist', full_name='DealCards.hulist', index=4,
            number=5, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='tianhu', full_name='DealCards.tianhu', index=5,
            number=6, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=874,
    serialized_end=987,
)

_SETTLEDATA.fields_by_name['settlePatterns'].enum_type = _SETTLEPATTERNS
_SETTLEDATA.fields_by_name['userSettleData'].message_type = _USERSETTLEDATA
_SETTLERESULT.fields_by_name['userSettleResule'].message_type = _USERSETTLERESULT
_USERSETTLERESULT.fields_by_name['settlePatterns'].enum_type = _SETTLEPATTERNS
_SHUFFLEDATA.fields_by_name['userCardLevel'].message_type = _USERCARDLEVEL
_SHUFFLERESULT.fields_by_name['dealCards'].message_type = _DEALCARDS
DESCRIPTOR.message_types_by_name['CalculateData'] = _CALCULATEDATA
DESCRIPTOR.message_types_by_name['CalculateResult'] = _CALCULATERESULT
DESCRIPTOR.message_types_by_name['SettleData'] = _SETTLEDATA
DESCRIPTOR.message_types_by_name['UserSettleData'] = _USERSETTLEDATA
DESCRIPTOR.message_types_by_name['SettleResult'] = _SETTLERESULT
DESCRIPTOR.message_types_by_name['UserSettleResult'] = _USERSETTLERESULT
DESCRIPTOR.message_types_by_name['ShuffleData'] = _SHUFFLEDATA
DESCRIPTOR.message_types_by_name['UserCardLevel'] = _USERCARDLEVEL
DESCRIPTOR.message_types_by_name['ShuffleResult'] = _SHUFFLERESULT
DESCRIPTOR.message_types_by_name['DealCards'] = _DEALCARDS
DESCRIPTOR.enum_types_by_name['SettlePatterns'] = _SETTLEPATTERNS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CalculateData = _reflection.GeneratedProtocolMessageType('CalculateData', (_message.Message,), dict(
    DESCRIPTOR=_CALCULATEDATA,
    __module__='zipai_pb2'
    # @@protoc_insertion_point(class_scope:CalculateData)
))
_sym_db.RegisterMessage(CalculateData)

CalculateResult = _reflection.GeneratedProtocolMessageType('CalculateResult', (_message.Message,), dict(
    DESCRIPTOR=_CALCULATERESULT,
    __module__='zipai_pb2'
    # @@protoc_insertion_point(class_scope:CalculateResult)
))
_sym_db.RegisterMessage(CalculateResult)

SettleData = _reflection.GeneratedProtocolMessageType('SettleData', (_message.Message,), dict(
    DESCRIPTOR=_SETTLEDATA,
    __module__='zipai_pb2'
    # @@protoc_insertion_point(class_scope:SettleData)
))
_sym_db.RegisterMessage(SettleData)

UserSettleData = _reflection.GeneratedProtocolMessageType('UserSettleData', (_message.Message,), dict(
    DESCRIPTOR=_USERSETTLEDATA,
    __module__='zipai_pb2'
    # @@protoc_insertion_point(class_scope:UserSettleData)
))
_sym_db.RegisterMessage(UserSettleData)

SettleResult = _reflection.GeneratedProtocolMessageType('SettleResult', (_message.Message,), dict(
    DESCRIPTOR=_SETTLERESULT,
    __module__='zipai_pb2'
    # @@protoc_insertion_point(class_scope:SettleResult)
))
_sym_db.RegisterMessage(SettleResult)

UserSettleResult = _reflection.GeneratedProtocolMessageType('UserSettleResult', (_message.Message,), dict(
    DESCRIPTOR=_USERSETTLERESULT,
    __module__='zipai_pb2'
    # @@protoc_insertion_point(class_scope:UserSettleResult)
))
_sym_db.RegisterMessage(UserSettleResult)

ShuffleData = _reflection.GeneratedProtocolMessageType('ShuffleData', (_message.Message,), dict(
    DESCRIPTOR=_SHUFFLEDATA,
    __module__='zipai_pb2'
    # @@protoc_insertion_point(class_scope:ShuffleData)
))
_sym_db.RegisterMessage(ShuffleData)

UserCardLevel = _reflection.GeneratedProtocolMessageType('UserCardLevel', (_message.Message,), dict(
    DESCRIPTOR=_USERCARDLEVEL,
    __module__='zipai_pb2'
    # @@protoc_insertion_point(class_scope:UserCardLevel)
))
_sym_db.RegisterMessage(UserCardLevel)

ShuffleResult = _reflection.GeneratedProtocolMessageType('ShuffleResult', (_message.Message,), dict(
    DESCRIPTOR=_SHUFFLERESULT,
    __module__='zipai_pb2'
    # @@protoc_insertion_point(class_scope:ShuffleResult)
))
_sym_db.RegisterMessage(ShuffleResult)

DealCards = _reflection.GeneratedProtocolMessageType('DealCards', (_message.Message,), dict(
    DESCRIPTOR=_DEALCARDS,
    __module__='zipai_pb2'
    # @@protoc_insertion_point(class_scope:DealCards)
))
_sym_db.RegisterMessage(DealCards)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(),
                                                _b('\n\020zipai.mode.protoB\005ZipaiP\001'))

_ZIPAI = _descriptor.ServiceDescriptor(
    name='Zipai',
    full_name='Zipai',
    file=DESCRIPTOR,
    index=0,
    options=None,
    serialized_start=1086,
    serialized_end=1225,
    methods=[
        _descriptor.MethodDescriptor(
            name='calculate',
            full_name='Zipai.calculate',
            index=0,
            containing_service=None,
            input_type=_CALCULATEDATA,
            output_type=_CALCULATERESULT,
            options=None,
        ),
        _descriptor.MethodDescriptor(
            name='settle',
            full_name='Zipai.settle',
            index=1,
            containing_service=None,
            input_type=_SETTLEDATA,
            output_type=_SETTLERESULT,
            options=None,
        ),
        _descriptor.MethodDescriptor(
            name='shuffle',
            full_name='Zipai.shuffle',
            index=2,
            containing_service=None,
            input_type=_SHUFFLEDATA,
            output_type=_SHUFFLERESULT,
            options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_ZIPAI)

DESCRIPTOR.services_by_name['Zipai'] = _ZIPAI

try:
    # THESE ELEMENTS WILL BE DEPRECATED.
    # Please use the generated *_pb2_grpc.py files instead.
    import grpc
    from grpc.beta import implementations as beta_implementations
    from grpc.beta import interfaces as beta_interfaces
    from grpc.framework.common import cardinality
    from grpc.framework.interfaces.face import utilities as face_utilities


    class ZipaiStub(object):
        # missing associated documentation comment in .proto file
        pass

        def __init__(self, channel):
            """Constructor.

            Args:
              channel: A grpc.Channel.
            """
            self.calculate = channel.unary_unary(
                '/Zipai/calculate',
                request_serializer=CalculateData.SerializeToString,
                response_deserializer=CalculateResult.FromString,
            )
            self.settle = channel.unary_unary(
                '/Zipai/settle',
                request_serializer=SettleData.SerializeToString,
                response_deserializer=SettleResult.FromString,
            )
            self.shuffle = channel.unary_unary(
                '/Zipai/shuffle',
                request_serializer=ShuffleData.SerializeToString,
                response_deserializer=ShuffleResult.FromString,
            )


    class ZipaiServicer(object):
        # missing associated documentation comment in .proto file
        pass

        def calculate(self, request, context):
            """进行过程计算
            """
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details('Method not implemented!')
            raise NotImplementedError('Method not implemented!')

        def settle(self, request, context):
            """结算
            """
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details('Method not implemented!')
            raise NotImplementedError('Method not implemented!')

        def shuffle(self, request, context):
            """洗牌函数
            """
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details('Method not implemented!')
            raise NotImplementedError('Method not implemented!')


    def add_ZipaiServicer_to_server(servicer, server):
        rpc_method_handlers = {
            'calculate': grpc.unary_unary_rpc_method_handler(
                servicer.calculate,
                request_deserializer=CalculateData.FromString,
                response_serializer=CalculateResult.SerializeToString,
            ),
            'settle': grpc.unary_unary_rpc_method_handler(
                servicer.settle,
                request_deserializer=SettleData.FromString,
                response_serializer=SettleResult.SerializeToString,
            ),
            'shuffle': grpc.unary_unary_rpc_method_handler(
                servicer.shuffle,
                request_deserializer=ShuffleData.FromString,
                response_serializer=ShuffleResult.SerializeToString,
            ),
        }
        generic_handler = grpc.method_handlers_generic_handler(
            'Zipai', rpc_method_handlers)
        server.add_generic_rpc_handlers((generic_handler,))


    class BetaZipaiServicer(object):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This class was generated
        only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
        # missing associated documentation comment in .proto file
        pass

        def calculate(self, request, context):
            """进行过程计算
            """
            context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)

        def settle(self, request, context):
            """结算
            """
            context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)

        def shuffle(self, request, context):
            """洗牌函数
            """
            context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


    class BetaZipaiStub(object):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This class was generated
        only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
        # missing associated documentation comment in .proto file
        pass

        def calculate(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
            """进行过程计算
            """
            raise NotImplementedError()

        calculate.future = None

        def settle(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
            """结算
            """
            raise NotImplementedError()

        settle.future = None

        def shuffle(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
            """洗牌函数
            """
            raise NotImplementedError()

        shuffle.future = None


    def beta_create_Zipai_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This function was
        generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
        request_deserializers = {
            ('Zipai', 'calculate'): CalculateData.FromString,
            ('Zipai', 'settle'): SettleData.FromString,
            ('Zipai', 'shuffle'): ShuffleData.FromString,
        }
        response_serializers = {
            ('Zipai', 'calculate'): CalculateResult.SerializeToString,
            ('Zipai', 'settle'): SettleResult.SerializeToString,
            ('Zipai', 'shuffle'): ShuffleResult.SerializeToString,
        }
        method_implementations = {
            ('Zipai', 'calculate'): face_utilities.unary_unary_inline(servicer.calculate),
            ('Zipai', 'settle'): face_utilities.unary_unary_inline(servicer.settle),
            ('Zipai', 'shuffle'): face_utilities.unary_unary_inline(servicer.shuffle),
        }
        server_options = beta_implementations.server_options(request_deserializers=request_deserializers,
                                                             response_serializers=response_serializers,
                                                             thread_pool=pool, thread_pool_size=pool_size,
                                                             default_timeout=default_timeout,
                                                             maximum_timeout=maximum_timeout)
        return beta_implementations.server(method_implementations, options=server_options)


    def beta_create_Zipai_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This function was
        generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
        request_serializers = {
            ('Zipai', 'calculate'): CalculateData.SerializeToString,
            ('Zipai', 'settle'): SettleData.SerializeToString,
            ('Zipai', 'shuffle'): ShuffleData.SerializeToString,
        }
        response_deserializers = {
            ('Zipai', 'calculate'): CalculateResult.FromString,
            ('Zipai', 'settle'): SettleResult.FromString,
            ('Zipai', 'shuffle'): ShuffleResult.FromString,
        }
        cardinalities = {
            'calculate': cardinality.Cardinality.UNARY_UNARY,
            'settle': cardinality.Cardinality.UNARY_UNARY,
            'shuffle': cardinality.Cardinality.UNARY_UNARY,
        }
        stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer,
                                                         request_serializers=request_serializers,
                                                         response_deserializers=response_deserializers,
                                                         thread_pool=pool, thread_pool_size=pool_size)
        return beta_implementations.dynamic_stub(channel, 'Zipai', cardinalities, options=stub_options)
except ImportError:
    pass
# @@protoc_insertion_point(module_scope)
