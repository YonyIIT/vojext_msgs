# generated from rosidl_generator_py/resource/_idl.py.em
# with input from vojext_msgs:msg/DetectedObjects.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_DetectedObjects(type):
    """Metaclass of message 'DetectedObjects'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('vojext_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'vojext_msgs.msg.DetectedObjects')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__detected_objects
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__detected_objects
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__detected_objects
            cls._TYPE_SUPPORT = module.type_support_msg__msg__detected_objects
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__detected_objects

            from sensor_msgs.msg import Image
            if Image.__class__._TYPE_SUPPORT is None:
                Image.__class__.__import_type_support__()

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

            from vojext_msgs.msg import DetectedObject
            if DetectedObject.__class__._TYPE_SUPPORT is None:
                DetectedObject.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DetectedObjects(metaclass=Metaclass_DetectedObjects):
    """Message class 'DetectedObjects'."""

    __slots__ = [
        '_header',
        '_detected_objects',
        '_rgb_image',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'detected_objects': 'sequence<vojext_msgs/DetectedObject>',
        'rgb_image': 'sensor_msgs/Image',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['vojext_msgs', 'msg'], 'DetectedObject')),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['sensor_msgs', 'msg'], 'Image'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.detected_objects = kwargs.get('detected_objects', [])
        from sensor_msgs.msg import Image
        self.rgb_image = kwargs.get('rgb_image', Image())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.detected_objects != other.detected_objects:
            return False
        if self.rgb_image != other.rgb_image:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @property
    def detected_objects(self):
        """Message field 'detected_objects'."""
        return self._detected_objects

    @detected_objects.setter
    def detected_objects(self, value):
        if __debug__:
            from vojext_msgs.msg import DetectedObject
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, DetectedObject) for v in value) and
                 True), \
                "The 'detected_objects' field must be a set or sequence and each value of type 'DetectedObject'"
        self._detected_objects = value

    @property
    def rgb_image(self):
        """Message field 'rgb_image'."""
        return self._rgb_image

    @rgb_image.setter
    def rgb_image(self, value):
        if __debug__:
            from sensor_msgs.msg import Image
            assert \
                isinstance(value, Image), \
                "The 'rgb_image' field must be a sub message of type 'Image'"
        self._rgb_image = value
