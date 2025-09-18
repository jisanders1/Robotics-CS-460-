# generated from rosidl_generator_py/resource/_idl.py.em
# with input from turtlesim_msgs:action/RotateAbsolute.idl
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

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RotateAbsolute_Goal(type):
    """Metaclass of message 'RotateAbsolute_Goal'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class RotateAbsolute_GoalConstants(typing.TypedDict):
        pass

    __constants: RotateAbsolute_GoalConstants = {
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
                'turtlesim_msgs.action.RotateAbsolute_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__rotate_absolute__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__rotate_absolute__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__rotate_absolute__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__rotate_absolute__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__rotate_absolute__goal

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RotateAbsolute_Goal(metaclass=Metaclass_RotateAbsolute_Goal):
    """Message class 'RotateAbsolute_Goal'."""

    __slots__ = [
        '_theta',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'theta': 'float',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, *,
                 theta: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.theta = theta if theta is not None else float()

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
        if not isinstance(other, RotateAbsolute_Goal):
            return False
        if self.theta != other.theta:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def theta(self) -> float:
        """Message field 'theta'."""
        return self._theta

    @theta.setter
    def theta(self, value: float) -> None:
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'theta' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'theta' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._theta = value


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_RotateAbsolute_Result(type):
    """Metaclass of message 'RotateAbsolute_Result'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class RotateAbsolute_ResultConstants(typing.TypedDict):
        pass

    __constants: RotateAbsolute_ResultConstants = {
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
                'turtlesim_msgs.action.RotateAbsolute_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__rotate_absolute__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__rotate_absolute__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__rotate_absolute__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__rotate_absolute__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__rotate_absolute__result

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RotateAbsolute_Result(metaclass=Metaclass_RotateAbsolute_Result):
    """Message class 'RotateAbsolute_Result'."""

    __slots__ = [
        '_delta',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'delta': 'float',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, *,
                 delta: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.delta = delta if delta is not None else float()

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
        if not isinstance(other, RotateAbsolute_Result):
            return False
        if self.delta != other.delta:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def delta(self) -> float:
        """Message field 'delta'."""
        return self._delta

    @delta.setter
    def delta(self, value: float) -> None:
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'delta' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'delta' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._delta = value


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_RotateAbsolute_Feedback(type):
    """Metaclass of message 'RotateAbsolute_Feedback'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class RotateAbsolute_FeedbackConstants(typing.TypedDict):
        pass

    __constants: RotateAbsolute_FeedbackConstants = {
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
                'turtlesim_msgs.action.RotateAbsolute_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__rotate_absolute__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__rotate_absolute__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__rotate_absolute__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__rotate_absolute__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__rotate_absolute__feedback

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RotateAbsolute_Feedback(metaclass=Metaclass_RotateAbsolute_Feedback):
    """Message class 'RotateAbsolute_Feedback'."""

    __slots__ = [
        '_remaining',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'remaining': 'float',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, *,
                 remaining: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.remaining = remaining if remaining is not None else float()

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
        if not isinstance(other, RotateAbsolute_Feedback):
            return False
        if self.remaining != other.remaining:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def remaining(self) -> float:
        """Message field 'remaining'."""
        return self._remaining

    @remaining.setter
    def remaining(self, value: float) -> None:
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'remaining' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'remaining' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._remaining = value


if typing.TYPE_CHECKING:
    from unique_identifier_msgs.msg import UUID


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_RotateAbsolute_SendGoal_Request(type):
    """Metaclass of message 'RotateAbsolute_SendGoal_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class RotateAbsolute_SendGoal_RequestConstants(typing.TypedDict):
        pass

    __constants: RotateAbsolute_SendGoal_RequestConstants = {
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
                'turtlesim_msgs.action.RotateAbsolute_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__rotate_absolute__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__rotate_absolute__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__rotate_absolute__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__rotate_absolute__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__rotate_absolute__send_goal__request

            from turtlesim_msgs.action import RotateAbsolute
            if RotateAbsolute.Goal._TYPE_SUPPORT is None:
                RotateAbsolute.Goal.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID._TYPE_SUPPORT is None:
                UUID.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RotateAbsolute_SendGoal_Request(metaclass=Metaclass_RotateAbsolute_SendGoal_Request):
    """Message class 'RotateAbsolute_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'turtlesim_msgs/RotateAbsolute_Goal',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['turtlesim_msgs', 'action'], 'RotateAbsolute_Goal'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[UUID] = None,  # noqa: E501
                 goal: typing.Optional[RotateAbsolute_Goal] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()
        from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_Goal
        self.goal = goal if goal is not None else RotateAbsolute_Goal()

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
        if not isinstance(other, RotateAbsolute_SendGoal_Request):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.goal != other.goal:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self) -> UUID:
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value: UUID) -> None:
        if self._check_fields:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def goal(self) -> RotateAbsolute_Goal:
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value: RotateAbsolute_Goal) -> None:
        if self._check_fields:
            from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_Goal
            assert \
                isinstance(value, RotateAbsolute_Goal), \
                "The 'goal' field must be a sub message of type 'RotateAbsolute_Goal'"
        self._goal = value


if typing.TYPE_CHECKING:
    from builtin_interfaces.msg import Time


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_RotateAbsolute_SendGoal_Response(type):
    """Metaclass of message 'RotateAbsolute_SendGoal_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class RotateAbsolute_SendGoal_ResponseConstants(typing.TypedDict):
        pass

    __constants: RotateAbsolute_SendGoal_ResponseConstants = {
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
                'turtlesim_msgs.action.RotateAbsolute_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__rotate_absolute__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__rotate_absolute__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__rotate_absolute__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__rotate_absolute__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__rotate_absolute__send_goal__response

            from builtin_interfaces.msg import Time
            if Time._TYPE_SUPPORT is None:
                Time.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RotateAbsolute_SendGoal_Response(metaclass=Metaclass_RotateAbsolute_SendGoal_Response):
    """Message class 'RotateAbsolute_SendGoal_Response'."""

    __slots__ = [
        '_accepted',
        '_stamp',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'accepted': 'boolean',
        'stamp': 'builtin_interfaces/Time',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
    )

    def __init__(self, *,
                 accepted: typing.Optional[bool] = None,  # noqa: E501
                 stamp: typing.Optional[Time] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.accepted = accepted if accepted is not None else bool()
        from builtin_interfaces.msg import Time
        self.stamp = stamp if stamp is not None else Time()

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
        if not isinstance(other, RotateAbsolute_SendGoal_Response):
            return False
        if self.accepted != other.accepted:
            return False
        if self.stamp != other.stamp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def accepted(self) -> bool:
        """Message field 'accepted'."""
        return self._accepted

    @accepted.setter
    def accepted(self, value: bool) -> None:
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'accepted' field must be of type 'bool'"
        self._accepted = value

    @builtins.property
    def stamp(self) -> Time:
        """Message field 'stamp'."""
        return self._stamp

    @stamp.setter
    def stamp(self, value: Time) -> None:
        if self._check_fields:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'stamp' field must be a sub message of type 'Time'"
        self._stamp = value


if typing.TYPE_CHECKING:
    from service_msgs.msg import ServiceEventInfo
    import collections


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_RotateAbsolute_SendGoal_Event(type):
    """Metaclass of message 'RotateAbsolute_SendGoal_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class RotateAbsolute_SendGoal_EventConstants(typing.TypedDict):
        pass

    __constants: RotateAbsolute_SendGoal_EventConstants = {
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
                'turtlesim_msgs.action.RotateAbsolute_SendGoal_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__rotate_absolute__send_goal__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__rotate_absolute__send_goal__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__rotate_absolute__send_goal__event
            cls._TYPE_SUPPORT = module.type_support_msg__action__rotate_absolute__send_goal__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__rotate_absolute__send_goal__event

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


class RotateAbsolute_SendGoal_Event(metaclass=Metaclass_RotateAbsolute_SendGoal_Event):
    """Message class 'RotateAbsolute_SendGoal_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<turtlesim_msgs/RotateAbsolute_SendGoal_Request, 1>',
        'response': 'sequence<turtlesim_msgs/RotateAbsolute_SendGoal_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['turtlesim_msgs', 'action'], 'RotateAbsolute_SendGoal_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['turtlesim_msgs', 'action'], 'RotateAbsolute_SendGoal_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[typing.Union[collections.abc.Sequence[RotateAbsolute_SendGoal_Request], collections.abc.Set[RotateAbsolute_SendGoal_Request], collections.UserList[RotateAbsolute_SendGoal_Request]]] = None,  # noqa: E501
                 response: typing.Optional[typing.Union[collections.abc.Sequence[RotateAbsolute_SendGoal_Response], collections.abc.Set[RotateAbsolute_SendGoal_Response], collections.UserList[RotateAbsolute_SendGoal_Response]]] = None,  # noqa: E501
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
        if not isinstance(other, RotateAbsolute_SendGoal_Event):
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
    def request(self) -> typing.Union[collections.abc.Sequence[RotateAbsolute_SendGoal_Request], collections.abc.Set[RotateAbsolute_SendGoal_Request], collections.UserList[RotateAbsolute_SendGoal_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: typing.Union[collections.abc.Sequence[RotateAbsolute_SendGoal_Request], collections.abc.Set[RotateAbsolute_SendGoal_Request], collections.UserList[RotateAbsolute_SendGoal_Request]]) -> None:
        if self._check_fields:
            from turtlesim_msgs.action import RotateAbsolute_SendGoal_Request
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
                 all(isinstance(v, RotateAbsolute_SendGoal_Request) for v in value) and
                 True), \
                "The 'request' field must be a set or sequence with length <= 1 and each value of type 'RotateAbsolute_SendGoal_Request'"
        self._request = value

    @builtins.property
    def response(self) -> typing.Union[collections.abc.Sequence[RotateAbsolute_SendGoal_Response], collections.abc.Set[RotateAbsolute_SendGoal_Response], collections.UserList[RotateAbsolute_SendGoal_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: typing.Union[collections.abc.Sequence[RotateAbsolute_SendGoal_Response], collections.abc.Set[RotateAbsolute_SendGoal_Response], collections.UserList[RotateAbsolute_SendGoal_Response]]) -> None:
        if self._check_fields:
            from turtlesim_msgs.action import RotateAbsolute_SendGoal_Response
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
                 all(isinstance(v, RotateAbsolute_SendGoal_Response) for v in value) and
                 True), \
                "The 'response' field must be a set or sequence with length <= 1 and each value of type 'RotateAbsolute_SendGoal_Response'"
        self._response = value


class Metaclass_RotateAbsolute_SendGoal(type):
    """Metaclass of service 'RotateAbsolute_SendGoal'."""

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
                'turtlesim_msgs.action.RotateAbsolute_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__rotate_absolute__send_goal

            from turtlesim_msgs.action import _rotate_absolute
            if _rotate_absolute.Metaclass_RotateAbsolute_SendGoal_Request._TYPE_SUPPORT is None:
                _rotate_absolute.Metaclass_RotateAbsolute_SendGoal_Request.__import_type_support__()
            if _rotate_absolute.Metaclass_RotateAbsolute_SendGoal_Response._TYPE_SUPPORT is None:
                _rotate_absolute.Metaclass_RotateAbsolute_SendGoal_Response.__import_type_support__()
            if _rotate_absolute.Metaclass_RotateAbsolute_SendGoal_Event._TYPE_SUPPORT is None:
                _rotate_absolute.Metaclass_RotateAbsolute_SendGoal_Event.__import_type_support__()


class RotateAbsolute_SendGoal(metaclass=Metaclass_RotateAbsolute_SendGoal):
    from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_SendGoal_Request as Request
    from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_SendGoal_Response as Response
    from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_SendGoal_Event as Event

    # type ignore below fixed in mypy 1.0+ see mypy#10342
    def __init__(self) -> typing.NoReturn:  # type: ignore
        raise NotImplementedError('Service classes can not be instantiated')


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_RotateAbsolute_GetResult_Request(type):
    """Metaclass of message 'RotateAbsolute_GetResult_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class RotateAbsolute_GetResult_RequestConstants(typing.TypedDict):
        pass

    __constants: RotateAbsolute_GetResult_RequestConstants = {
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
                'turtlesim_msgs.action.RotateAbsolute_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__rotate_absolute__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__rotate_absolute__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__rotate_absolute__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__rotate_absolute__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__rotate_absolute__get_result__request

            from unique_identifier_msgs.msg import UUID
            if UUID._TYPE_SUPPORT is None:
                UUID.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RotateAbsolute_GetResult_Request(metaclass=Metaclass_RotateAbsolute_GetResult_Request):
    """Message class 'RotateAbsolute_GetResult_Request'."""

    __slots__ = [
        '_goal_id',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[UUID] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()

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
        if not isinstance(other, RotateAbsolute_GetResult_Request):
            return False
        if self.goal_id != other.goal_id:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self) -> UUID:
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value: UUID) -> None:
        if self._check_fields:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_RotateAbsolute_GetResult_Response(type):
    """Metaclass of message 'RotateAbsolute_GetResult_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class RotateAbsolute_GetResult_ResponseConstants(typing.TypedDict):
        pass

    __constants: RotateAbsolute_GetResult_ResponseConstants = {
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
                'turtlesim_msgs.action.RotateAbsolute_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__rotate_absolute__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__rotate_absolute__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__rotate_absolute__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__rotate_absolute__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__rotate_absolute__get_result__response

            from turtlesim_msgs.action import RotateAbsolute
            if RotateAbsolute.Result._TYPE_SUPPORT is None:
                RotateAbsolute.Result.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RotateAbsolute_GetResult_Response(metaclass=Metaclass_RotateAbsolute_GetResult_Response):
    """Message class 'RotateAbsolute_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'status': 'int8',
        'result': 'turtlesim_msgs/RotateAbsolute_Result',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['turtlesim_msgs', 'action'], 'RotateAbsolute_Result'),  # noqa: E501
    )

    def __init__(self, *,
                 status: typing.Optional[int] = None,  # noqa: E501
                 result: typing.Optional[RotateAbsolute_Result] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.status = status if status is not None else int()
        from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_Result
        self.result = result if result is not None else RotateAbsolute_Result()

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
        if not isinstance(other, RotateAbsolute_GetResult_Response):
            return False
        if self.status != other.status:
            return False
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def status(self) -> int:
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'status' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'status' field must be an integer in [-128, 127]"
        self._status = value

    @builtins.property
    def result(self) -> RotateAbsolute_Result:
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value: RotateAbsolute_Result) -> None:
        if self._check_fields:
            from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_Result
            assert \
                isinstance(value, RotateAbsolute_Result), \
                "The 'result' field must be a sub message of type 'RotateAbsolute_Result'"
        self._result = value


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_RotateAbsolute_GetResult_Event(type):
    """Metaclass of message 'RotateAbsolute_GetResult_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class RotateAbsolute_GetResult_EventConstants(typing.TypedDict):
        pass

    __constants: RotateAbsolute_GetResult_EventConstants = {
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
                'turtlesim_msgs.action.RotateAbsolute_GetResult_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__rotate_absolute__get_result__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__rotate_absolute__get_result__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__rotate_absolute__get_result__event
            cls._TYPE_SUPPORT = module.type_support_msg__action__rotate_absolute__get_result__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__rotate_absolute__get_result__event

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


class RotateAbsolute_GetResult_Event(metaclass=Metaclass_RotateAbsolute_GetResult_Event):
    """Message class 'RotateAbsolute_GetResult_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<turtlesim_msgs/RotateAbsolute_GetResult_Request, 1>',
        'response': 'sequence<turtlesim_msgs/RotateAbsolute_GetResult_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['turtlesim_msgs', 'action'], 'RotateAbsolute_GetResult_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['turtlesim_msgs', 'action'], 'RotateAbsolute_GetResult_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[typing.Union[collections.abc.Sequence[RotateAbsolute_GetResult_Request], collections.abc.Set[RotateAbsolute_GetResult_Request], collections.UserList[RotateAbsolute_GetResult_Request]]] = None,  # noqa: E501
                 response: typing.Optional[typing.Union[collections.abc.Sequence[RotateAbsolute_GetResult_Response], collections.abc.Set[RotateAbsolute_GetResult_Response], collections.UserList[RotateAbsolute_GetResult_Response]]] = None,  # noqa: E501
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
        if not isinstance(other, RotateAbsolute_GetResult_Event):
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
    def request(self) -> typing.Union[collections.abc.Sequence[RotateAbsolute_GetResult_Request], collections.abc.Set[RotateAbsolute_GetResult_Request], collections.UserList[RotateAbsolute_GetResult_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: typing.Union[collections.abc.Sequence[RotateAbsolute_GetResult_Request], collections.abc.Set[RotateAbsolute_GetResult_Request], collections.UserList[RotateAbsolute_GetResult_Request]]) -> None:
        if self._check_fields:
            from turtlesim_msgs.action import RotateAbsolute_GetResult_Request
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
                 all(isinstance(v, RotateAbsolute_GetResult_Request) for v in value) and
                 True), \
                "The 'request' field must be a set or sequence with length <= 1 and each value of type 'RotateAbsolute_GetResult_Request'"
        self._request = value

    @builtins.property
    def response(self) -> typing.Union[collections.abc.Sequence[RotateAbsolute_GetResult_Response], collections.abc.Set[RotateAbsolute_GetResult_Response], collections.UserList[RotateAbsolute_GetResult_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: typing.Union[collections.abc.Sequence[RotateAbsolute_GetResult_Response], collections.abc.Set[RotateAbsolute_GetResult_Response], collections.UserList[RotateAbsolute_GetResult_Response]]) -> None:
        if self._check_fields:
            from turtlesim_msgs.action import RotateAbsolute_GetResult_Response
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
                 all(isinstance(v, RotateAbsolute_GetResult_Response) for v in value) and
                 True), \
                "The 'response' field must be a set or sequence with length <= 1 and each value of type 'RotateAbsolute_GetResult_Response'"
        self._response = value


class Metaclass_RotateAbsolute_GetResult(type):
    """Metaclass of service 'RotateAbsolute_GetResult'."""

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
                'turtlesim_msgs.action.RotateAbsolute_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__rotate_absolute__get_result

            from turtlesim_msgs.action import _rotate_absolute
            if _rotate_absolute.Metaclass_RotateAbsolute_GetResult_Request._TYPE_SUPPORT is None:
                _rotate_absolute.Metaclass_RotateAbsolute_GetResult_Request.__import_type_support__()
            if _rotate_absolute.Metaclass_RotateAbsolute_GetResult_Response._TYPE_SUPPORT is None:
                _rotate_absolute.Metaclass_RotateAbsolute_GetResult_Response.__import_type_support__()
            if _rotate_absolute.Metaclass_RotateAbsolute_GetResult_Event._TYPE_SUPPORT is None:
                _rotate_absolute.Metaclass_RotateAbsolute_GetResult_Event.__import_type_support__()


class RotateAbsolute_GetResult(metaclass=Metaclass_RotateAbsolute_GetResult):
    from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_GetResult_Request as Request
    from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_GetResult_Response as Response
    from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_GetResult_Event as Event

    # type ignore below fixed in mypy 1.0+ see mypy#10342
    def __init__(self) -> typing.NoReturn:  # type: ignore
        raise NotImplementedError('Service classes can not be instantiated')


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_RotateAbsolute_FeedbackMessage(type):
    """Metaclass of message 'RotateAbsolute_FeedbackMessage'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class RotateAbsolute_FeedbackMessageConstants(typing.TypedDict):
        pass

    __constants: RotateAbsolute_FeedbackMessageConstants = {
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
                'turtlesim_msgs.action.RotateAbsolute_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__rotate_absolute__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__rotate_absolute__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__rotate_absolute__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__rotate_absolute__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__rotate_absolute__feedback_message

            from turtlesim_msgs.action import RotateAbsolute
            if RotateAbsolute.Feedback._TYPE_SUPPORT is None:
                RotateAbsolute.Feedback.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID._TYPE_SUPPORT is None:
                UUID.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RotateAbsolute_FeedbackMessage(metaclass=Metaclass_RotateAbsolute_FeedbackMessage):
    """Message class 'RotateAbsolute_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'turtlesim_msgs/RotateAbsolute_Feedback',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['turtlesim_msgs', 'action'], 'RotateAbsolute_Feedback'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[UUID] = None,  # noqa: E501
                 feedback: typing.Optional[RotateAbsolute_Feedback] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()
        from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_Feedback
        self.feedback = feedback if feedback is not None else RotateAbsolute_Feedback()

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
        if not isinstance(other, RotateAbsolute_FeedbackMessage):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.feedback != other.feedback:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self) -> UUID:
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value: UUID) -> None:
        if self._check_fields:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def feedback(self) -> RotateAbsolute_Feedback:
        """Message field 'feedback'."""
        return self._feedback

    @feedback.setter
    def feedback(self, value: RotateAbsolute_Feedback) -> None:
        if self._check_fields:
            from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_Feedback
            assert \
                isinstance(value, RotateAbsolute_Feedback), \
                "The 'feedback' field must be a sub message of type 'RotateAbsolute_Feedback'"
        self._feedback = value


class Metaclass_RotateAbsolute(type):
    """Metaclass of action 'RotateAbsolute'."""

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
                'turtlesim_msgs.action.RotateAbsolute')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__rotate_absolute

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from turtlesim_msgs.action import _rotate_absolute
            if _rotate_absolute.Metaclass_RotateAbsolute_SendGoal._TYPE_SUPPORT is None:
                _rotate_absolute.Metaclass_RotateAbsolute_SendGoal.__import_type_support__()
            if _rotate_absolute.Metaclass_RotateAbsolute_GetResult._TYPE_SUPPORT is None:
                _rotate_absolute.Metaclass_RotateAbsolute_GetResult.__import_type_support__()
            if _rotate_absolute.Metaclass_RotateAbsolute_FeedbackMessage._TYPE_SUPPORT is None:
                _rotate_absolute.Metaclass_RotateAbsolute_FeedbackMessage.__import_type_support__()


class RotateAbsolute(metaclass=Metaclass_RotateAbsolute):

    # The goal message defined in the action definition.
    from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_Goal as Goal
    # The result message defined in the action definition.
    from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_Result as Result
    # The feedback message defined in the action definition.
    from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_Feedback as Feedback

    class Impl:

        # The send_goal service using a wrapped version of the goal message as a request.
        from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_SendGoal as SendGoalService
        # The get_result service using a wrapped version of the result message as a response.
        from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_GetResult as GetResultService
        # The feedback message with generic fields which wraps the feedback message.
        from turtlesim_msgs.action._rotate_absolute import RotateAbsolute_FeedbackMessage as FeedbackMessage

        # The generic service to cancel a goal.
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
        # The generic message for get the status of a goal.
        from action_msgs.msg._goal_status_array import GoalStatusArray as GoalStatusMessage

    # type ignore below fixed in mypy 1.0+ see mypy#10342
    def __init__(self) -> typing.NoReturn:  # type: ignore
        raise NotImplementedError('Action classes can not be instantiated')
