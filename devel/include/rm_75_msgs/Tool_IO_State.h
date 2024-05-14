// Generated by gencpp from file rm_75_msgs/Tool_IO_State.msg
// DO NOT EDIT!


#ifndef RM_75_MSGS_MESSAGE_TOOL_IO_STATE_H
#define RM_75_MSGS_MESSAGE_TOOL_IO_STATE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rm_75_msgs
{
template <class ContainerAllocator>
struct Tool_IO_State_
{
  typedef Tool_IO_State_<ContainerAllocator> Type;

  Tool_IO_State_()
    : Tool_Digital_Input()
    , Tool_Analog_Input(0.0)  {
      Tool_Digital_Input.assign(false);
  }
  Tool_IO_State_(const ContainerAllocator& _alloc)
    : Tool_Digital_Input()
    , Tool_Analog_Input(0.0)  {
  (void)_alloc;
      Tool_Digital_Input.assign(false);
  }



   typedef boost::array<uint8_t, 2>  _Tool_Digital_Input_type;
  _Tool_Digital_Input_type Tool_Digital_Input;

   typedef float _Tool_Analog_Input_type;
  _Tool_Analog_Input_type Tool_Analog_Input;





  typedef boost::shared_ptr< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> const> ConstPtr;

}; // struct Tool_IO_State_

typedef ::rm_75_msgs::Tool_IO_State_<std::allocator<void> > Tool_IO_State;

typedef boost::shared_ptr< ::rm_75_msgs::Tool_IO_State > Tool_IO_StatePtr;
typedef boost::shared_ptr< ::rm_75_msgs::Tool_IO_State const> Tool_IO_StateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rm_75_msgs::Tool_IO_State_<ContainerAllocator1> & lhs, const ::rm_75_msgs::Tool_IO_State_<ContainerAllocator2> & rhs)
{
  return lhs.Tool_Digital_Input == rhs.Tool_Digital_Input &&
    lhs.Tool_Analog_Input == rhs.Tool_Analog_Input;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rm_75_msgs::Tool_IO_State_<ContainerAllocator1> & lhs, const ::rm_75_msgs::Tool_IO_State_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rm_75_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d7adff68dc996b192b01391906704f92";
  }

  static const char* value(const ::rm_75_msgs::Tool_IO_State_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd7adff68dc996b19ULL;
  static const uint64_t static_value2 = 0x2b01391906704f92ULL;
};

template<class ContainerAllocator>
struct DataType< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rm_75_msgs/Tool_IO_State";
  }

  static const char* value(const ::rm_75_msgs::Tool_IO_State_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool[2] Tool_Digital_Input\n"
"float32 Tool_Analog_Input\n"
;
  }

  static const char* value(const ::rm_75_msgs::Tool_IO_State_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Tool_Digital_Input);
      stream.next(m.Tool_Analog_Input);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Tool_IO_State_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rm_75_msgs::Tool_IO_State_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rm_75_msgs::Tool_IO_State_<ContainerAllocator>& v)
  {
    s << indent << "Tool_Digital_Input[]" << std::endl;
    for (size_t i = 0; i < v.Tool_Digital_Input.size(); ++i)
    {
      s << indent << "  Tool_Digital_Input[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.Tool_Digital_Input[i]);
    }
    s << indent << "Tool_Analog_Input: ";
    Printer<float>::stream(s, indent + "  ", v.Tool_Analog_Input);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RM_75_MSGS_MESSAGE_TOOL_IO_STATE_H
