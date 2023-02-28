# generated from rosidl_generator_py/resource/_idl.py.em
# with input from vojext_msgs:msg/Person.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Person(type):
    """Metaclass of message 'Person'."""

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
                'vojext_msgs.msg.Person')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__person
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__person
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__person
            cls._TYPE_SUPPORT = module.type_support_msg__msg__person
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__person

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

            from vojext_msgs.msg import Hand
            if Hand.__class__._TYPE_SUPPORT is None:
                Hand.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Person(metaclass=Metaclass_Person):
    """Message class 'Person'."""

    __slots__ = [
        '_header',
        '_result_dynamic_left',
        '_result_dynamic_right',
        '_result_static_left',
        '_result_static_right',
        '_final_result_left',
        '_final_result_right',
        '_left_hand',
        '_right_hand',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'result_dynamic_left': 'string',
        'result_dynamic_right': 'string',
        'result_static_left': 'string',
        'result_static_right': 'string',
        'final_result_left': 'string',
        'final_result_right': 'string',
        'left_hand': 'sequence<vojext_msgs/Hand>',
        'right_hand': 'sequence<vojext_msgs/Hand>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['vojext_msgs', 'msg'], 'Hand')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['vojext_msgs', 'msg'], 'Hand')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.result_dynamic_left = kwargs.get('result_dynamic_left', str())
        self.result_dynamic_right = kwargs.get('result_dynamic_right', str())
        self.result_static_left = kwargs.get('result_static_left', str())
        self.result_static_right = kwargs.get('result_static_right', str())
        self.final_result_left = kwargs.get('final_result_left', str())
        self.final_result_right = kwargs.get('final_result_right', str())
        self.left_hand = kwargs.get('left_hand', [])
        self.right_hand = kwargs.get('right_hand', [])

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
        if self.result_dynamic_left != other.result_dynamic_left:
            return False
        if self.result_dynamic_right != other.result_dynamic_right:
            return False
        if self.result_static_left != other.result_static_left:
            return False
        if self.result_static_right != other.result_static_right:
            return False
        if self.final_result_left != other.final_result_left:
            return False
        if self.final_result_right != other.final_result_right:
            return False
        if self.left_hand != other.left_hand:
            return False
        if self.right_hand != other.right_hand:
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
    def result_dynamic_left(self):
        """Message field 'result_dynamic_left'."""
        return self._result_dynamic_left

    @result_dynamic_left.setter
    def result_dynamic_left(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'result_dynamic_left' field must be of type 'str'"
        self._result_dynamic_left = value

    @property
    def result_dynamic_right(self):
        """Message field 'result_dynamic_right'."""
        return self._result_dynamic_right

    @result_dynamic_right.setter
    def result_dynamic_right(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'result_dynamic_right' field must be of type 'str'"
        self._result_dynamic_right = value

    @property
    def result_static_left(self):
        """Message field 'result_static_left'."""
        return self._result_static_left

    @result_static_left.setter
    def result_static_left(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'result_static_left' field must be of type 'str'"
        self._result_static_left = value

    @property
    def result_static_right(self):
        """Message field 'result_static_right'."""
        return self._result_static_right

    @result_static_right.setter
    def result_static_right(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'result_static_right' field must be of type 'str'"
        self._result_static_right = value

    @property
    def final_result_left(self):
        """Message field 'final_result_left'."""
        return self._final_result_left

    @final_result_left.setter
    def final_result_left(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'final_result_left' field must be of type 'str'"
        self._final_result_left = value

    @property
    def final_result_right(self):
        """Message field 'final_result_right'."""
        return self._final_result_right

    @final_result_right.setter
    def final_result_right(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'final_result_right' field must be of type 'str'"
        self._final_result_right = value

    @property
    def left_hand(self):
        """Message field 'left_hand'."""
        return self._left_hand

    @left_hand.setter
    def left_hand(self, value):
        if __debug__:
            from vojext_msgs.msg import Hand
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
                 all(isinstance(v, Hand) for v in value) and
                 True), \
                "The 'left_hand' field must be a set or sequence and each value of type 'Hand'"
        self._left_hand = value

    @property
    def right_hand(self):
        """Message field 'right_hand'."""
        return self._right_hand

    @right_hand.setter
    def right_hand(self, value):
        if __debug__:
            from vojext_msgs.msg import Hand
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
                 all(isinstance(v, Hand) for v in value) and
                 True), \
                "The 'right_hand' field must be a set or sequence and each value of type 'Hand'"
        self._right_hand = value
