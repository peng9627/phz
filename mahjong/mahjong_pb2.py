# coding=utf-8
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mahjong.proto

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
    name='mahjong.proto',
    package='majong_rpc',
    syntax='proto3',
    serialized_pb=_b(
        '\n\rmahjong.proto\x12\nmajong_rpc\"\x16\n\x05\x43\x61rds\x12\r\n\x05\x63\x61rds\x18\x01 \x03(\x05\"v\n\x08GangData\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.majong_rpc.GangType\x12\x0f\n\x07\x66ighter\x18\x02 \x03(\x05\x12\x11\n\tgangvalue\x18\x03 \x01(\x05\x12\x11\n\tgangscore\x18\x04 \x01(\x05\x12\x0f\n\x07zhuanyi\x18\x05 \x01(\x05\"\x97\x01\n\x11MahjongPlayerData\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x12\x10\n\x08handlist\x18\x02 \x03(\x05\x12\x0b\n\x03\x63hi\x18\x03 \x03(\x05\x12\x0c\n\x04peng\x18\x04 \x03(\x05\x12\"\n\x04gang\x18\x05 \x03(\x0b\x32\x14.majong_rpc.GangData\x12\x0f\n\x07\x62\x61ojiao\x18\x06 \x01(\x08\x12\r\n\x05score\x18\x07 \x01(\x05\"^\n\rCalculateData\x12\x0f\n\x07\x61llocid\x18\x01 \x01(\x05\x12-\n\x06player\x18\x02 \x01(\x0b\x32\x1d.majong_rpc.MahjongPlayerData\x12\r\n\x05rogue\x18\x03 \x01(\x05\"^\n\x0f\x43\x61lculateResult\x12\x0b\n\x03\x63hi\x18\x01 \x03(\x05\x12\x0b\n\x03\x64ui\x18\x02 \x03(\x05\x12\x0b\n\x03san\x18\x03 \x03(\x05\x12\n\n\x02si\x18\x04 \x03(\x05\x12\n\n\x02hu\x18\x05 \x03(\x05\x12\x0c\n\x04zimo\x18\x06 \x03(\x05\"\xaf\x02\n\nSettleData\x12\x10\n\x08\x61lloc_id\x18\x01 \x01(\x05\x12-\n\x06player\x18\x02 \x03(\x0b\x32\x1d.majong_rpc.MahjongPlayerData\x12\x0e\n\x06\x62\x61nker\x18\x03 \x01(\x05\x12-\n\x06hudata\x18\x04 \x03(\x0b\x32\x1d.majong_rpc.SettleData.HuData\x12\r\n\x05rogue\x18\x05 \x01(\x05\x12\x10\n\x08\x66\x65ngding\x18\x06 \x01(\x05\x12\x0f\n\x07peijiao\x18\x07 \x01(\x08\x12\x0e\n\x06yinghu\x18\x08 \x01(\x08\x12\x12\n\nzimojiafan\x18\t \x01(\x08\x1aK\n\x06HuData\x12\x0e\n\x06huUser\x18\x01 \x01(\x05\x12\x11\n\tloseUsers\x18\x02 \x03(\x05\x12\x0e\n\x06settle\x18\x03 \x03(\x05\x12\x0e\n\x06majong\x18\x04 \x01(\x05\"F\n\x0cSettleResult\x12\x36\n\x10userSettleResule\x18\x01 \x03(\x0b\x32\x1c.majong_rpc.UserSettleResult\"m\n\x10UserSettleResult\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x0b\n\x03win\x18\x02 \x01(\x05\x12\x11\n\tgangScore\x18\x03 \x01(\x05\x12\x11\n\tcardScore\x18\x04 \x01(\x05\x12\x16\n\x0esettlePatterns\x18\x05 \x03(\x05\":\n\tCheatData\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x12\x0b\n\x03loc\x18\x02 \x01(\x05\x12\r\n\x05level\x18\x03 \x01(\x05\"F\n\x0bShuffleData\x12\x10\n\x08\x61lloc_id\x18\x01 \x01(\x05\x12%\n\x06\x63heats\x18\x02 \x03(\x0b\x32\x15.majong_rpc.CheatData\"!\n\rShuffleResult\x12\x10\n\x08\x63\x61rdlist\x18\x01 \x03(\x05*+\n\x08GangType\x12\t\n\x05\x42GANG\x10\x00\x12\t\n\x05MGANG\x10\x01\x12\t\n\x05\x41GANG\x10\x02\x32\x96\x02\n\x0fMajongCalculate\x12\x45\n\tcalculate\x12\x19.majong_rpc.CalculateData\x1a\x1b.majong_rpc.CalculateResult\"\x00\x12<\n\x06settle\x12\x16.majong_rpc.SettleData\x1a\x18.majong_rpc.SettleResult\"\x00\x12?\n\x07shuffle\x12\x17.majong_rpc.ShuffleData\x1a\x19.majong_rpc.ShuffleResult\"\x00\x12=\n\x0b\x62\x61ojiaoGang\x12\x19.majong_rpc.CalculateData\x1a\x11.majong_rpc.Cards\"\x00\x42\x16\n\x12mahjong.mode.protoP\x01\x62\x06proto3')
)

_GANGTYPE = _descriptor.EnumDescriptor(
    name='GangType',
    full_name='majong_rpc.GangType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='BGANG', index=0, number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='MGANG', index=1, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='AGANG', index=2, number=2,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=1175,
    serialized_end=1218,
)
_sym_db.RegisterEnumDescriptor(_GANGTYPE)

GangType = enum_type_wrapper.EnumTypeWrapper(_GANGTYPE)
BGANG = 0
MGANG = 1
AGANG = 2

_CARDS = _descriptor.Descriptor(
    name='Cards',
    full_name='majong_rpc.Cards',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='cards', full_name='majong_rpc.Cards.cards', index=0,
            number=1, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
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
    serialized_start=29,
    serialized_end=51,
)

_GANGDATA = _descriptor.Descriptor(
    name='GangData',
    full_name='majong_rpc.GangData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type', full_name='majong_rpc.GangData.type', index=0,
            number=1, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='fighter', full_name='majong_rpc.GangData.fighter', index=1,
            number=2, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='gangvalue', full_name='majong_rpc.GangData.gangvalue', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='gangscore', full_name='majong_rpc.GangData.gangscore', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='zhuanyi', full_name='majong_rpc.GangData.zhuanyi', index=4,
            number=5, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
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
    serialized_start=53,
    serialized_end=171,
)

_MAHJONGPLAYERDATA = _descriptor.Descriptor(
    name='MahjongPlayerData',
    full_name='majong_rpc.MahjongPlayerData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='player_id', full_name='majong_rpc.MahjongPlayerData.player_id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='handlist', full_name='majong_rpc.MahjongPlayerData.handlist', index=1,
            number=2, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='chi', full_name='majong_rpc.MahjongPlayerData.chi', index=2,
            number=3, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='peng', full_name='majong_rpc.MahjongPlayerData.peng', index=3,
            number=4, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='gang', full_name='majong_rpc.MahjongPlayerData.gang', index=4,
            number=5, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='baojiao', full_name='majong_rpc.MahjongPlayerData.baojiao', index=5,
            number=6, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='score', full_name='majong_rpc.MahjongPlayerData.score', index=6,
            number=7, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
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
    serialized_end=325,
)

_CALCULATEDATA = _descriptor.Descriptor(
    name='CalculateData',
    full_name='majong_rpc.CalculateData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='allocid', full_name='majong_rpc.CalculateData.allocid', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='player', full_name='majong_rpc.CalculateData.player', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='rogue', full_name='majong_rpc.CalculateData.rogue', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
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
    serialized_start=327,
    serialized_end=421,
)

_CALCULATERESULT = _descriptor.Descriptor(
    name='CalculateResult',
    full_name='majong_rpc.CalculateResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='chi', full_name='majong_rpc.CalculateResult.chi', index=0,
            number=1, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='dui', full_name='majong_rpc.CalculateResult.dui', index=1,
            number=2, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='san', full_name='majong_rpc.CalculateResult.san', index=2,
            number=3, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='si', full_name='majong_rpc.CalculateResult.si', index=3,
            number=4, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='hu', full_name='majong_rpc.CalculateResult.hu', index=4,
            number=5, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='zimo', full_name='majong_rpc.CalculateResult.zimo', index=5,
            number=6, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
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
    serialized_start=423,
    serialized_end=517,
)

_SETTLEDATA_HUDATA = _descriptor.Descriptor(
    name='HuData',
    full_name='majong_rpc.SettleData.HuData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='huUser', full_name='majong_rpc.SettleData.HuData.huUser', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='loseUsers', full_name='majong_rpc.SettleData.HuData.loseUsers', index=1,
            number=2, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='settle', full_name='majong_rpc.SettleData.HuData.settle', index=2,
            number=3, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='majong', full_name='majong_rpc.SettleData.HuData.majong', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
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
    serialized_start=748,
    serialized_end=823,
)

_SETTLEDATA = _descriptor.Descriptor(
    name='SettleData',
    full_name='majong_rpc.SettleData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='alloc_id', full_name='majong_rpc.SettleData.alloc_id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='player', full_name='majong_rpc.SettleData.player', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='banker', full_name='majong_rpc.SettleData.banker', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='hudata', full_name='majong_rpc.SettleData.hudata', index=3,
            number=4, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='rogue', full_name='majong_rpc.SettleData.rogue', index=4,
            number=5, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='fengding', full_name='majong_rpc.SettleData.fengding', index=5,
            number=6, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='peijiao', full_name='majong_rpc.SettleData.peijiao', index=6,
            number=7, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='yinghu', full_name='majong_rpc.SettleData.yinghu', index=7,
            number=8, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='zimojiafan', full_name='majong_rpc.SettleData.zimojiafan', index=8,
            number=9, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_SETTLEDATA_HUDATA, ],
    enum_types=[
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=520,
    serialized_end=823,
)

_SETTLERESULT = _descriptor.Descriptor(
    name='SettleResult',
    full_name='majong_rpc.SettleResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='userSettleResule', full_name='majong_rpc.SettleResult.userSettleResule', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
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
    serialized_start=825,
    serialized_end=895,
)

_USERSETTLERESULT = _descriptor.Descriptor(
    name='UserSettleResult',
    full_name='majong_rpc.UserSettleResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='userId', full_name='majong_rpc.UserSettleResult.userId', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='win', full_name='majong_rpc.UserSettleResult.win', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='gangScore', full_name='majong_rpc.UserSettleResult.gangScore', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='cardScore', full_name='majong_rpc.UserSettleResult.cardScore', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='settlePatterns', full_name='majong_rpc.UserSettleResult.settlePatterns', index=4,
            number=5, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
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
    serialized_start=897,
    serialized_end=1006,
)

_CHEATDATA = _descriptor.Descriptor(
    name='CheatData',
    full_name='majong_rpc.CheatData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='player_id', full_name='majong_rpc.CheatData.player_id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='loc', full_name='majong_rpc.CheatData.loc', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='level', full_name='majong_rpc.CheatData.level', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
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
    serialized_start=1008,
    serialized_end=1066,
)

_SHUFFLEDATA = _descriptor.Descriptor(
    name='ShuffleData',
    full_name='majong_rpc.ShuffleData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='alloc_id', full_name='majong_rpc.ShuffleData.alloc_id', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='cheats', full_name='majong_rpc.ShuffleData.cheats', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
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
    serialized_start=1068,
    serialized_end=1138,
)

_SHUFFLERESULT = _descriptor.Descriptor(
    name='ShuffleResult',
    full_name='majong_rpc.ShuffleResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='cardlist', full_name='majong_rpc.ShuffleResult.cardlist', index=0,
            number=1, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None, file=DESCRIPTOR),
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
    serialized_start=1140,
    serialized_end=1173,
)

_GANGDATA.fields_by_name['type'].enum_type = _GANGTYPE
_MAHJONGPLAYERDATA.fields_by_name['gang'].message_type = _GANGDATA
_CALCULATEDATA.fields_by_name['player'].message_type = _MAHJONGPLAYERDATA
_SETTLEDATA_HUDATA.containing_type = _SETTLEDATA
_SETTLEDATA.fields_by_name['player'].message_type = _MAHJONGPLAYERDATA
_SETTLEDATA.fields_by_name['hudata'].message_type = _SETTLEDATA_HUDATA
_SETTLERESULT.fields_by_name['userSettleResule'].message_type = _USERSETTLERESULT
_SHUFFLEDATA.fields_by_name['cheats'].message_type = _CHEATDATA
DESCRIPTOR.message_types_by_name['Cards'] = _CARDS
DESCRIPTOR.message_types_by_name['GangData'] = _GANGDATA
DESCRIPTOR.message_types_by_name['MahjongPlayerData'] = _MAHJONGPLAYERDATA
DESCRIPTOR.message_types_by_name['CalculateData'] = _CALCULATEDATA
DESCRIPTOR.message_types_by_name['CalculateResult'] = _CALCULATERESULT
DESCRIPTOR.message_types_by_name['SettleData'] = _SETTLEDATA
DESCRIPTOR.message_types_by_name['SettleResult'] = _SETTLERESULT
DESCRIPTOR.message_types_by_name['UserSettleResult'] = _USERSETTLERESULT
DESCRIPTOR.message_types_by_name['CheatData'] = _CHEATDATA
DESCRIPTOR.message_types_by_name['ShuffleData'] = _SHUFFLEDATA
DESCRIPTOR.message_types_by_name['ShuffleResult'] = _SHUFFLERESULT
DESCRIPTOR.enum_types_by_name['GangType'] = _GANGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Cards = _reflection.GeneratedProtocolMessageType('Cards', (_message.Message,), dict(
    DESCRIPTOR=_CARDS,
    __module__='mahjong_pb2'
    # @@protoc_insertion_point(class_scope:majong_rpc.Cards)
))
_sym_db.RegisterMessage(Cards)

GangData = _reflection.GeneratedProtocolMessageType('GangData', (_message.Message,), dict(
    DESCRIPTOR=_GANGDATA,
    __module__='mahjong_pb2'
    # @@protoc_insertion_point(class_scope:majong_rpc.GangData)
))
_sym_db.RegisterMessage(GangData)

MahjongPlayerData = _reflection.GeneratedProtocolMessageType('MahjongPlayerData', (_message.Message,), dict(
    DESCRIPTOR=_MAHJONGPLAYERDATA,
    __module__='mahjong_pb2'
    # @@protoc_insertion_point(class_scope:majong_rpc.MahjongPlayerData)
))
_sym_db.RegisterMessage(MahjongPlayerData)

CalculateData = _reflection.GeneratedProtocolMessageType('CalculateData', (_message.Message,), dict(
    DESCRIPTOR=_CALCULATEDATA,
    __module__='mahjong_pb2'
    # @@protoc_insertion_point(class_scope:majong_rpc.CalculateData)
))
_sym_db.RegisterMessage(CalculateData)

CalculateResult = _reflection.GeneratedProtocolMessageType('CalculateResult', (_message.Message,), dict(
    DESCRIPTOR=_CALCULATERESULT,
    __module__='mahjong_pb2'
    # @@protoc_insertion_point(class_scope:majong_rpc.CalculateResult)
))
_sym_db.RegisterMessage(CalculateResult)

SettleData = _reflection.GeneratedProtocolMessageType('SettleData', (_message.Message,), dict(

    HuData=_reflection.GeneratedProtocolMessageType('HuData', (_message.Message,), dict(
        DESCRIPTOR=_SETTLEDATA_HUDATA,
        __module__='mahjong_pb2'
        # @@protoc_insertion_point(class_scope:majong_rpc.SettleData.HuData)
    ))
    ,
    DESCRIPTOR=_SETTLEDATA,
    __module__='mahjong_pb2'
    # @@protoc_insertion_point(class_scope:majong_rpc.SettleData)
))
_sym_db.RegisterMessage(SettleData)
_sym_db.RegisterMessage(SettleData.HuData)

SettleResult = _reflection.GeneratedProtocolMessageType('SettleResult', (_message.Message,), dict(
    DESCRIPTOR=_SETTLERESULT,
    __module__='mahjong_pb2'
    # @@protoc_insertion_point(class_scope:majong_rpc.SettleResult)
))
_sym_db.RegisterMessage(SettleResult)

UserSettleResult = _reflection.GeneratedProtocolMessageType('UserSettleResult', (_message.Message,), dict(
    DESCRIPTOR=_USERSETTLERESULT,
    __module__='mahjong_pb2'
    # @@protoc_insertion_point(class_scope:majong_rpc.UserSettleResult)
))
_sym_db.RegisterMessage(UserSettleResult)

CheatData = _reflection.GeneratedProtocolMessageType('CheatData', (_message.Message,), dict(
    DESCRIPTOR=_CHEATDATA,
    __module__='mahjong_pb2'
    # @@protoc_insertion_point(class_scope:majong_rpc.CheatData)
))
_sym_db.RegisterMessage(CheatData)

ShuffleData = _reflection.GeneratedProtocolMessageType('ShuffleData', (_message.Message,), dict(
    DESCRIPTOR=_SHUFFLEDATA,
    __module__='mahjong_pb2'
    # @@protoc_insertion_point(class_scope:majong_rpc.ShuffleData)
))
_sym_db.RegisterMessage(ShuffleData)

ShuffleResult = _reflection.GeneratedProtocolMessageType('ShuffleResult', (_message.Message,), dict(
    DESCRIPTOR=_SHUFFLERESULT,
    __module__='mahjong_pb2'
    # @@protoc_insertion_point(class_scope:majong_rpc.ShuffleResult)
))
_sym_db.RegisterMessage(ShuffleResult)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\022mahjong.mode.protoP\001'))

_MAJONGCALCULATE = _descriptor.ServiceDescriptor(
    name='MajongCalculate',
    full_name='majong_rpc.MajongCalculate',
    file=DESCRIPTOR,
    index=0,
    options=None,
    serialized_start=1221,
    serialized_end=1499,
    methods=[
        _descriptor.MethodDescriptor(
            name='calculate',
            full_name='majong_rpc.MajongCalculate.calculate',
            index=0,
            containing_service=None,
            input_type=_CALCULATEDATA,
            output_type=_CALCULATERESULT,
            options=None,
        ),
        _descriptor.MethodDescriptor(
            name='settle',
            full_name='majong_rpc.MajongCalculate.settle',
            index=1,
            containing_service=None,
            input_type=_SETTLEDATA,
            output_type=_SETTLERESULT,
            options=None,
        ),
        _descriptor.MethodDescriptor(
            name='shuffle',
            full_name='majong_rpc.MajongCalculate.shuffle',
            index=2,
            containing_service=None,
            input_type=_SHUFFLEDATA,
            output_type=_SHUFFLERESULT,
            options=None,
        ),
        _descriptor.MethodDescriptor(
            name='baojiaoGang',
            full_name='majong_rpc.MajongCalculate.baojiaoGang',
            index=3,
            containing_service=None,
            input_type=_CALCULATEDATA,
            output_type=_CARDS,
            options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_MAJONGCALCULATE)

DESCRIPTOR.services_by_name['MajongCalculate'] = _MAJONGCALCULATE

# @@protoc_insertion_point(module_scope)
