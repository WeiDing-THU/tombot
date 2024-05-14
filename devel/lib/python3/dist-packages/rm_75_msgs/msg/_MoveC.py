# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rm_75_msgs/MoveC.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class MoveC(genpy.Message):
  _md5sum = "6450bf023cd7a5f30a68c51718bc4f21"
  _type = "rm_75_msgs/MoveC"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """geometry_msgs/Pose Mid_Pose
geometry_msgs/Pose End_Pose
float32 speed

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['Mid_Pose','End_Pose','speed']
  _slot_types = ['geometry_msgs/Pose','geometry_msgs/Pose','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       Mid_Pose,End_Pose,speed

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MoveC, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.Mid_Pose is None:
        self.Mid_Pose = geometry_msgs.msg.Pose()
      if self.End_Pose is None:
        self.End_Pose = geometry_msgs.msg.Pose()
      if self.speed is None:
        self.speed = 0.
    else:
      self.Mid_Pose = geometry_msgs.msg.Pose()
      self.End_Pose = geometry_msgs.msg.Pose()
      self.speed = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_14df().pack(_x.Mid_Pose.position.x, _x.Mid_Pose.position.y, _x.Mid_Pose.position.z, _x.Mid_Pose.orientation.x, _x.Mid_Pose.orientation.y, _x.Mid_Pose.orientation.z, _x.Mid_Pose.orientation.w, _x.End_Pose.position.x, _x.End_Pose.position.y, _x.End_Pose.position.z, _x.End_Pose.orientation.x, _x.End_Pose.orientation.y, _x.End_Pose.orientation.z, _x.End_Pose.orientation.w, _x.speed))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.Mid_Pose is None:
        self.Mid_Pose = geometry_msgs.msg.Pose()
      if self.End_Pose is None:
        self.End_Pose = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 116
      (_x.Mid_Pose.position.x, _x.Mid_Pose.position.y, _x.Mid_Pose.position.z, _x.Mid_Pose.orientation.x, _x.Mid_Pose.orientation.y, _x.Mid_Pose.orientation.z, _x.Mid_Pose.orientation.w, _x.End_Pose.position.x, _x.End_Pose.position.y, _x.End_Pose.position.z, _x.End_Pose.orientation.x, _x.End_Pose.orientation.y, _x.End_Pose.orientation.z, _x.End_Pose.orientation.w, _x.speed,) = _get_struct_14df().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_14df().pack(_x.Mid_Pose.position.x, _x.Mid_Pose.position.y, _x.Mid_Pose.position.z, _x.Mid_Pose.orientation.x, _x.Mid_Pose.orientation.y, _x.Mid_Pose.orientation.z, _x.Mid_Pose.orientation.w, _x.End_Pose.position.x, _x.End_Pose.position.y, _x.End_Pose.position.z, _x.End_Pose.orientation.x, _x.End_Pose.orientation.y, _x.End_Pose.orientation.z, _x.End_Pose.orientation.w, _x.speed))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.Mid_Pose is None:
        self.Mid_Pose = geometry_msgs.msg.Pose()
      if self.End_Pose is None:
        self.End_Pose = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 116
      (_x.Mid_Pose.position.x, _x.Mid_Pose.position.y, _x.Mid_Pose.position.z, _x.Mid_Pose.orientation.x, _x.Mid_Pose.orientation.y, _x.Mid_Pose.orientation.z, _x.Mid_Pose.orientation.w, _x.End_Pose.position.x, _x.End_Pose.position.y, _x.End_Pose.position.z, _x.End_Pose.orientation.x, _x.End_Pose.orientation.y, _x.End_Pose.orientation.z, _x.End_Pose.orientation.w, _x.speed,) = _get_struct_14df().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_14df = None
def _get_struct_14df():
    global _struct_14df
    if _struct_14df is None:
        _struct_14df = struct.Struct("<14df")
    return _struct_14df
