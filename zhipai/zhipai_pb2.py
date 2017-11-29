# coding=utf-8
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zhipai.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='zhipai.proto',
    package='',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x0czhipai.proto\"i\n\nSettleData\x12\x0f\n\x07\x61llocid\x18\x01 \x01(\x05\x12\x0e\n\x06\x62\x61nker\x18\x02 \x01(\x05\x12\'\n\x0euserSettleData\x18\x03 \x03(\x0b\x32\x0f.UserSettleData\x12\x11\n\textraData\x18\x04 \x01(\x0c\"K\n\x10NiuniuSettleData\x12\x10\n\x08playRule\x18\x01 \x01(\x05\x12\x12\n\ndoubleRule\x18\x02 \x01(\x05\x12\x11\n\tgameRules\x18\x03 \x01(\x05\"7\n\x12PiBanBanSettleData\x12\x10\n\x08playType\x18\x01 \x01(\x05\x12\x0f\n\x07jackpot\x18\x02 \x01(\x05\"A\n\x0eUserSettleData\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x10\n\x08\x63\x61rdlist\x18\x02 \x03(\x05\x12\r\n\x05score\x18\x03 \x01(\x05\";\n\x0cSettleResult\x12+\n\x10userSettleResule\x18\x01 \x03(\x0b\x32\x11.UserSettleResult\"B\n\x10UserSettleResult\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x11\n\tcardValue\x18\x02 \x01(\x05\x12\x0b\n\x03win\x18\x03 \x01(\x05\"\x1e\n\x0bShuffleData\x12\x0f\n\x07\x61llocid\x18\x01 \x01(\x05\"!\n\rShuffleResult\x12\x10\n\x08\x63\x61rdlist\x18\x01 \x03(\x05\x32[\n\x06Zhipai\x12&\n\x06settle\x12\x0b.SettleData\x1a\r.SettleResult\"\x00\x12)\n\x07shuffle\x12\x0c.ShuffleData\x1a\x0e.ShuffleResult\"\x00\x42\x1c\n\x11zhipai.mode.protoB\x05ZipaiP\x01\x62\x06proto3')
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
            name='banker', full_name='SettleData.banker', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='userSettleData', full_name='SettleData.userSettleData', index=2,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='extraData', full_name='SettleData.extraData', index=3,
            number=4, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
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
    serialized_start=16,
    serialized_end=121,
)

_NIUNIUSETTLEDATA = _descriptor.Descriptor(
    name='NiuniuSettleData',
    full_name='NiuniuSettleData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='playRule', full_name='NiuniuSettleData.playRule', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='doubleRule', full_name='NiuniuSettleData.doubleRule', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='gameRules', full_name='NiuniuSettleData.gameRules', index=2,
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
    serialized_start=123,
    serialized_end=198,
)

_PIBANBANSETTLEDATA = _descriptor.Descriptor(
    name='PiBanBanSettleData',
    full_name='PiBanBanSettleData',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='playType', full_name='PiBanBanSettleData.playType', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='jackpot', full_name='PiBanBanSettleData.jackpot', index=1,
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
    serialized_start=200,
    serialized_end=255,
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
            name='cardlist', full_name='UserSettleData.cardlist', index=1,
            number=2, type=5, cpp_type=1, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='score', full_name='UserSettleData.score', index=2,
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
    serialized_start=257,
    serialized_end=322,
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
    serialized_start=324,
    serialized_end=383,
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
            name='cardValue', full_name='UserSettleResult.cardValue', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='win', full_name='UserSettleResult.win', index=2,
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
    serialized_start=385,
    serialized_end=451,
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
    serialized_start=453,
    serialized_end=483,
)

_SHUFFLERESULT = _descriptor.Descriptor(
    name='ShuffleResult',
    full_name='ShuffleResult',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='cardlist', full_name='ShuffleResult.cardlist', index=0,
            number=1, type=5, cpp_type=1, label=3,
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
    serialized_start=485,
    serialized_end=518,
)

_SETTLEDATA.fields_by_name['userSettleData'].message_type = _USERSETTLEDATA
_SETTLERESULT.fields_by_name['userSettleResule'].message_type = _USERSETTLERESULT
DESCRIPTOR.message_types_by_name['SettleData'] = _SETTLEDATA
DESCRIPTOR.message_types_by_name['NiuniuSettleData'] = _NIUNIUSETTLEDATA
DESCRIPTOR.message_types_by_name['PiBanBanSettleData'] = _PIBANBANSETTLEDATA
DESCRIPTOR.message_types_by_name['UserSettleData'] = _USERSETTLEDATA
DESCRIPTOR.message_types_by_name['SettleResult'] = _SETTLERESULT
DESCRIPTOR.message_types_by_name['UserSettleResult'] = _USERSETTLERESULT
DESCRIPTOR.message_types_by_name['ShuffleData'] = _SHUFFLEDATA
DESCRIPTOR.message_types_by_name['ShuffleResult'] = _SHUFFLERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SettleData = _reflection.GeneratedProtocolMessageType('SettleData', (_message.Message,), dict(
    DESCRIPTOR=_SETTLEDATA,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:SettleData)
))
_sym_db.RegisterMessage(SettleData)

NiuniuSettleData = _reflection.GeneratedProtocolMessageType('NiuniuSettleData', (_message.Message,), dict(
    DESCRIPTOR=_NIUNIUSETTLEDATA,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:NiuniuSettleData)
))
_sym_db.RegisterMessage(NiuniuSettleData)

PiBanBanSettleData = _reflection.GeneratedProtocolMessageType('PiBanBanSettleData', (_message.Message,), dict(
    DESCRIPTOR=_PIBANBANSETTLEDATA,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:PiBanBanSettleData)
))
_sym_db.RegisterMessage(PiBanBanSettleData)

UserSettleData = _reflection.GeneratedProtocolMessageType('UserSettleData', (_message.Message,), dict(
    DESCRIPTOR=_USERSETTLEDATA,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:UserSettleData)
))
_sym_db.RegisterMessage(UserSettleData)

SettleResult = _reflection.GeneratedProtocolMessageType('SettleResult', (_message.Message,), dict(
    DESCRIPTOR=_SETTLERESULT,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:SettleResult)
))
_sym_db.RegisterMessage(SettleResult)

UserSettleResult = _reflection.GeneratedProtocolMessageType('UserSettleResult', (_message.Message,), dict(
    DESCRIPTOR=_USERSETTLERESULT,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:UserSettleResult)
))
_sym_db.RegisterMessage(UserSettleResult)

ShuffleData = _reflection.GeneratedProtocolMessageType('ShuffleData', (_message.Message,), dict(
    DESCRIPTOR=_SHUFFLEDATA,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:ShuffleData)
))
_sym_db.RegisterMessage(ShuffleData)

ShuffleResult = _reflection.GeneratedProtocolMessageType('ShuffleResult', (_message.Message,), dict(
    DESCRIPTOR=_SHUFFLERESULT,
    __module__='zhipai_pb2'
    # @@protoc_insertion_point(class_scope:ShuffleResult)
))
_sym_db.RegisterMessage(ShuffleResult)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(),
                                                _b('\n\021zhipai.mode.protoB\005ZipaiP\001'))

_ZHIPAI = _descriptor.ServiceDescriptor(
    name='Zhipai',
    full_name='Zhipai',
    file=DESCRIPTOR,
    index=0,
    options=None,
    serialized_start=520,
    serialized_end=611,
    methods=[
        _descriptor.MethodDescriptor(
            name='settle',
            full_name='Zhipai.settle',
            index=0,
            containing_service=None,
            input_type=_SETTLEDATA,
            output_type=_SETTLERESULT,
            options=None,
        ),
        _descriptor.MethodDescriptor(
            name='shuffle',
            full_name='Zhipai.shuffle',
            index=1,
            containing_service=None,
            input_type=_SHUFFLEDATA,
            output_type=_SHUFFLERESULT,
            options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_ZHIPAI)

DESCRIPTOR.services_by_name['Zhipai'] = _ZHIPAI

try:
    # THESE ELEMENTS WILL BE DEPRECATED.
    # Please use the generated *_pb2_grpc.py files instead.
    import grpc
    from grpc.beta import implementations as beta_implementations
    from grpc.beta import interfaces as beta_interfaces
    from grpc.framework.common import cardinality
    from grpc.framework.interfaces.face import utilities as face_utilities


    class ZhipaiStub(object):
        # missing associated documentation comment in .proto file
        pass

        def __init__(self, channel):
            """Constructor.

            Args:
              channel: A grpc.Channel.
            """
            self.settle = channel.unary_unary(
                '/Zhipai/settle',
                request_serializer=SettleData.SerializeToString,
                response_deserializer=SettleResult.FromString,
            )
            self.shuffle = channel.unary_unary(
                '/Zhipai/shuffle',
                request_serializer=ShuffleData.SerializeToString,
                response_deserializer=ShuffleResult.FromString,
            )


    class ZhipaiServicer(object):
        # missing associated documentation comment in .proto file
        pass

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


    def add_ZhipaiServicer_to_server(servicer, server):
        rpc_method_handlers = {
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
            'Zhipai', rpc_method_handlers)
        server.add_generic_rpc_handlers((generic_handler,))


    class BetaZhipaiServicer(object):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This class was generated
        only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
        # missing associated documentation comment in .proto file
        pass

        def settle(self, request, context):
            """结算
            """
            context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)

        def shuffle(self, request, context):
            """洗牌函数
            """
            context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


    class BetaZhipaiStub(object):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This class was generated
        only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
        # missing associated documentation comment in .proto file
        pass

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


    def beta_create_Zhipai_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This function was
        generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
        request_deserializers = {
            ('Zhipai', 'settle'): SettleData.FromString,
            ('Zhipai', 'shuffle'): ShuffleData.FromString,
        }
        response_serializers = {
            ('Zhipai', 'settle'): SettleResult.SerializeToString,
            ('Zhipai', 'shuffle'): ShuffleResult.SerializeToString,
        }
        method_implementations = {
            ('Zhipai', 'settle'): face_utilities.unary_unary_inline(servicer.settle),
            ('Zhipai', 'shuffle'): face_utilities.unary_unary_inline(servicer.shuffle),
        }
        server_options = beta_implementations.server_options(request_deserializers=request_deserializers,
                                                             response_serializers=response_serializers,
                                                             thread_pool=pool, thread_pool_size=pool_size,
                                                             default_timeout=default_timeout,
                                                             maximum_timeout=maximum_timeout)
        return beta_implementations.server(method_implementations, options=server_options)


    def beta_create_Zhipai_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This function was
        generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
        request_serializers = {
            ('Zhipai', 'settle'): SettleData.SerializeToString,
            ('Zhipai', 'shuffle'): ShuffleData.SerializeToString,
        }
        response_deserializers = {
            ('Zhipai', 'settle'): SettleResult.FromString,
            ('Zhipai', 'shuffle'): ShuffleResult.FromString,
        }
        cardinalities = {
            'settle': cardinality.Cardinality.UNARY_UNARY,
            'shuffle': cardinality.Cardinality.UNARY_UNARY,
        }
        stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer,
                                                         request_serializers=request_serializers,
                                                         response_deserializers=response_deserializers,
                                                         thread_pool=pool, thread_pool_size=pool_size)
        return beta_implementations.dynamic_stub(channel, 'Zhipai', cardinalities, options=stub_options)
except ImportError:
    pass
# @@protoc_insertion_point(module_scope)
