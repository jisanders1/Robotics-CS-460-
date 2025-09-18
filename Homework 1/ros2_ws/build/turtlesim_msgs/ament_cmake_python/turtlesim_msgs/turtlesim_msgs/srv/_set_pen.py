# generated from rosidl_generator_py/resource/_idl.py.em
# with input from turtlesim_msgs:srv/SetPen.idl
# generated code does not contain a copyright notice

from __future__ import annotations

import collections.abc
from os import getenv
import typing

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


if typing.TYPE_CHECKING:
    from ctypes import Structure

    class PyCapsule(Structure):
        pass  # don't need to define the full structure


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SetPen_Request(type):
    """Metaclass of message 'SetPen_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class SetPen_RequestConstants(typing.TypedDict):
        pass

    __constants: SetPen_RequestConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('turtlesim_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'turtlesim_msgs.srv.SetPen_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_pen__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_pen__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_pen__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_pen__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_pen__request

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetPen_Request(metaclass=Metaclass_SetPen_Request):
    """Message class 'SetPen_Request'."""

    __slots__ = [
        '_r',
        '_g',
        '_b',
        '_width',
        '_off',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'r': 'uint8',
        'g': 'uint8',
        'b': 'uint8',
        'width': 'uint8',
        'off': 'uint8',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, *,
                 r: typing.Optional[int] = None,  # noqa: E501
                 g: typing.Optional[int] = None,  # noqa: E501
                 b: typing.Optional[int] = None,  # noqa: E501
                 width: typing.Optional[int] = None,  # noqa: E501
                 off: typing.Optional[int] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.r = r if r is not None else int()
        self.g = g if g is not None else int()
        self.b = b if b is not None else int()
        self.width = width if width is not None else int()
        self.off = off if off is not None else int()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
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
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SetPen_Request):
            return False
        if self.r != other.r:
            return False
        if self.g != other.g:
            return False
        if self.b != other.b:
            return False
        if self.width != other.width:
            return False
        if self.off != other.off:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def r(self) -> int:
        """Message field 'r'."""
        return self._r

    @r.setter
    def r(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'r' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'r' field must be an unsigned integer in [0, 255]"
        self._r = value

    @builtins.property
    def g(self) -> int:
        """Message field 'g'."""
        return self._g

    @g.setter
    def g(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'g' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'g' field must be an unsigned integer in [0, 255]"
        self._g = value

    @builtins.property
    def b(self) -> int:
        """Message field 'b'."""
        return self._b

    @b.setter
    def b(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'b' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'b' field must be an unsigned integer in [0, 255]"
        self._b = value

    @builtins.property
    def width(self) -> int:
        """Message field 'width'."""
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'width' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'width' field must be an unsigned integer in [0, 255]"
        self._width = value

    @builtins.property
    def off(self) -> int:
        """Message field 'off'."""
        return self._off

    @off.setter
    def off(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'off' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'off' field must be an unsigned integer in [0, 255]"
        self._off = value


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_SetPen_Response(type):
    """Metaclass of message 'SetPen_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class SetPen_ResponseConstants(typing.TypedDict):
        pass

    __constants: SetPen_ResponseConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('turtlesim_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'turtlesim_msgs.srv.SetPen_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_pen__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_pen__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_pen__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_pen__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_pen__response

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetPen_Response(metaclass=Metaclass_SetPen_Response):
    """Message class 'SetPen_Response'."""

    __slots__ = [
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
    )

    def __init__(self, *,
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
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
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SetPen_Response):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)


if typing.TYPE_CHECKING:
    from service_msgs.msg import ServiceEventInfo
    import collections


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_SetPen_Event(type):
    """Metaclass of message 'SetPen_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class SetPen_EventConstants(typing.TypedDict):
        pass

    __constants: SetPen_EventConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('turtlesim_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'turtlesim_msgs.srv.SetPen_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_pen__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_pen__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_pen__event
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_pen__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_pen__event

            from service_msgs.msg import ServiceEventInfo
            if ServiceEventInfo._TYPE_SUPPORT is None:
                ServiceEventInfo.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetPen_Event(metaclass=Metaclass_SetPen_Event):
    """Message class 'SetPen_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<turtlesim_msgs/SetPen_Request, 1>',
        'response': 'sequence<turtlesim_msgs/SetPen_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['turtlesim_msgs', 'srv'], 'SetPen_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['turtlesim_msgs', 'srv'], 'SetPen_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[typing.Union[collections.abc.Sequence[SetPen_Request], collections.abc.Set[SetPen_Request], collections.UserList[SetPen_Request]]] = None,  # noqa: E501
                 response: typing.Optional[typing.Union[collections.abc.Sequence[SetPen_Response], collections.abc.Set[SetPen_Response], collections.UserList[SetPen_Response]]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from service_msgs.msg import ServiceEventInfo
        self.info = info if info is not None else ServiceEventInfo()
        self.request = request if request is not None else []
        self.response = response if response is not None else []

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
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
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SetPen_Event):
            return False
        if self.info != other.info:
            return False
        if self.request != other.request:
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def info(self) -> ServiceEventInfo:
        """Message field 'info'."""
        return self._info

    @info.setter
    def info(self, value: ServiceEventInfo) -> None:
        if self._check_fields:
            from service_msgs.msg import ServiceEventInfo
            assert \
                isinstance(value, ServiceEventInfo), \
                "The 'info' field must be a sub message of type 'ServiceEventInfo'"
        self._info = value

    @builtins.property
    def request(self) -> typing.Union[collections.abc.Sequence[SetPen_Request], collections.abc.Set[SetPen_Request], collections.UserList[SetPen_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: typing.Union[collections.abc.Sequence[SetPen_Request], collections.abc.Set[SetPen_Request], collections.UserList[SetPen_Request]]) -> None:
        if self._check_fields:
            from turtlesim_msgs.srv import SetPen_Request
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
                 len(value) <= 1 and
                 all(isinstance(v, SetPen_Request) for v in value) and
                 True), \
                "The 'request' field must be a set or sequence with length <= 1 and each value of type 'SetPen_Request'"
        self._request = value

    @builtins.property
    def response(self) -> typing.Union[collections.abc.Sequence[SetPen_Response], collections.abc.Set[SetPen_Response], collections.UserList[SetPen_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: typing.Union[collections.abc.Sequence[SetPen_Response], collections.abc.Set[SetPen_Response], collections.UserList[SetPen_Response]]) -> None:
        if self._check_fields:
            from turtlesim_msgs.srv import SetPen_Response
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
                 len(value) <= 1 and
                 all(isinstance(v, SetPen_Response) for v in value) and
                 True), \
                "The 'response' field must be a set or sequence with length <= 1 and each value of type 'SetPen_Response'"
        self._response = value


class Metaclass_SetPen(type):
    """Metaclass of service 'SetPen'."""

    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('turtlesim_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'turtlesim_msgs.srv.SetPen')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__set_pen

            from turtlesim_msgs.srv import _set_pen
            if _set_pen.Metaclass_SetPen_Request._TYPE_SUPPORT is None:
                _set_pen.Metaclass_SetPen_Request.__import_type_support__()
            if _set_pen.Metaclass_SetPen_Response._TYPE_SUPPORT is None:
                _set_pen.Metaclass_SetPen_Response.__import_type_support__()
            if _set_pen.Metaclass_SetPen_Event._TYPE_SUPPORT is None:
                _set_pen.Metaclass_SetPen_Event.__import_type_support__()


class SetPen(metaclass=Metaclass_SetPen):
    from turtlesim_msgs.srv._set_pen import SetPen_Request as Request
    from turtlesim_msgs.srv._set_pen import SetPen_Response as Response
    from turtlesim_msgs.srv._set_pen import SetPen_Event as Event

    # type ignore below fixed in mypy 1.0+ see mypy#10342
    def __init__(self) -> typing.NoReturn:  # type: ignore
        raise NotImplementedError('Service classes can not be instantiated')
