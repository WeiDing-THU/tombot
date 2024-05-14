# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from pick_and_place/DetectedObject.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class DetectedObject(genpy.Message):
  _md5sum = "167a85e1fd80883aabe7acad7edd6a85"
  _type = "pick_and_place/DetectedObject"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float64 x_world
float64 y_world
float64 z_world
float64 width
float64 length
float64 height
string color
"""
  __slots__ = ['x_world','y_world','z_world','width','length','height','color']
  _slot_types = ['float64','float64','float64','float64','float64','float64','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x_world,y_world,z_world,width,length,height,color

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DetectedObject, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.x_world is None:
        self.x_world = 0.
      if self.y_world is None:
        self.y_world = 0.
      if self.z_world is None:
        self.z_world = 0.
      if self.width is None:
        self.width = 0.
      if self.length is None:
        self.length = 0.
      if self.height is None:
        self.height = 0.
      if self.color is None:
        self.color = ''
    else:
      self.x_world = 0.
      self.y_world = 0.
      self.z_world = 0.
      self.width = 0.
      self.length = 0.
      self.height = 0.
      self.color = ''

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
      buff.write(_get_struct_6d().pack(_x.x_world, _x.y_world, _x.z_world, _x.width, _x.length, _x.height))
      _x = self.color
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
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
      end = 0
      _x = self
      start = end
      end += 48
      (_x.x_world, _x.y_world, _x.z_world, _x.width, _x.length, _x.height,) = _get_struct_6d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.color = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.color = str[start:end]
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
      buff.write(_get_struct_6d().pack(_x.x_world, _x.y_world, _x.z_world, _x.width, _x.length, _x.height))
      _x = self.color
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
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
      end = 0
      _x = self
      start = end
      end += 48
      (_x.x_world, _x.y_world, _x.z_world, _x.width, _x.length, _x.height,) = _get_struct_6d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.color = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.color = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6d = None
def _get_struct_6d():
    global _struct_6d
    if _struct_6d is None:
        _struct_6d = struct.Struct("<6d")
    return _struct_6d
