# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import materials_pb2
from . import robotapi_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='storage.proto',
  package='robominions',
  serialized_pb=_b('\n\rstorage.proto\x12\x0brobominions\x1a\x0fmaterials.proto\x1a\x0erobotapi.proto\";\n\x0bPluginState\x12,\n\x0brobot_state\x18\x01 \x03(\x0b\x32\x17.robominions.RobotState\"\xe4\x01\n\nRobotState\x12\x13\n\x0bplayer_name\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12/\n\x0erobot_location\x18\x04 \x01(\x0b\x32\x17.robominions.Coordinate\x12\x12\n\nworld_name\x18\x05 \x01(\t\x12=\n\x0frobot_direction\x18\x06 \x01(\x0e\x32$.robominions.WorldLocation.Direction\x12/\n\x0frobot_inventory\x18\x07 \x03(\x0b\x32\x16.robominions.ItemStack\"`\n\tItemStack\x12\r\n\x05index\x18\x01 \x01(\x05\x12\'\n\x08material\x18\x02 \x01(\x0b\x32\x15.robominions.Material\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x42.\n\x1e\x61u.id.katharos.robominions.apiB\x0cRobotStorage')
  ,
  dependencies=[materials_pb2.DESCRIPTOR,robotapi_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PLUGINSTATE = _descriptor.Descriptor(
  name='PluginState',
  full_name='robominions.PluginState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_state', full_name='robominions.PluginState.robot_state', index=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=122,
)


_ROBOTSTATE = _descriptor.Descriptor(
  name='RobotState',
  full_name='robominions.RobotState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_name', full_name='robominions.RobotState.player_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='robominions.RobotState.uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='robot_location', full_name='robominions.RobotState.robot_location', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='world_name', full_name='robominions.RobotState.world_name', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='robot_direction', full_name='robominions.RobotState.robot_direction', index=4,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='robot_inventory', full_name='robominions.RobotState.robot_inventory', index=5,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=353,
)


_ITEMSTACK = _descriptor.Descriptor(
  name='ItemStack',
  full_name='robominions.ItemStack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='robominions.ItemStack.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='material', full_name='robominions.ItemStack.material', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='robominions.ItemStack.count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='robominions.ItemStack.data', index=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=451,
)

_PLUGINSTATE.fields_by_name['robot_state'].message_type = _ROBOTSTATE
_ROBOTSTATE.fields_by_name['robot_location'].message_type = robotapi_pb2._COORDINATE
_ROBOTSTATE.fields_by_name['robot_direction'].enum_type = robotapi_pb2._WORLDLOCATION_DIRECTION
_ROBOTSTATE.fields_by_name['robot_inventory'].message_type = _ITEMSTACK
_ITEMSTACK.fields_by_name['material'].message_type = materials_pb2._MATERIAL
DESCRIPTOR.message_types_by_name['PluginState'] = _PLUGINSTATE
DESCRIPTOR.message_types_by_name['RobotState'] = _ROBOTSTATE
DESCRIPTOR.message_types_by_name['ItemStack'] = _ITEMSTACK

PluginState = _reflection.GeneratedProtocolMessageType('PluginState', (_message.Message,), dict(
  DESCRIPTOR = _PLUGINSTATE,
  __module__ = 'storage_pb2'
  # @@protoc_insertion_point(class_scope:robominions.PluginState)
  ))
_sym_db.RegisterMessage(PluginState)

RobotState = _reflection.GeneratedProtocolMessageType('RobotState', (_message.Message,), dict(
  DESCRIPTOR = _ROBOTSTATE,
  __module__ = 'storage_pb2'
  # @@protoc_insertion_point(class_scope:robominions.RobotState)
  ))
_sym_db.RegisterMessage(RobotState)

ItemStack = _reflection.GeneratedProtocolMessageType('ItemStack', (_message.Message,), dict(
  DESCRIPTOR = _ITEMSTACK,
  __module__ = 'storage_pb2'
  # @@protoc_insertion_point(class_scope:robominions.ItemStack)
  ))
_sym_db.RegisterMessage(ItemStack)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036au.id.katharos.robominions.apiB\014RobotStorage'))
# @@protoc_insertion_point(module_scope)