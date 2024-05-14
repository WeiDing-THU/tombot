// Generated by gencpp from file rm_75_msgs/Tool_Digital_Output.msg
// DO NOT EDIT!


#ifndef RM_75_MSGS_MESSAGE_TOOL_DIGITAL_OUTPUT_H
#define RM_75_MSGS_MESSAGE_TOOL_DIGITAL_OUTPUT_H


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
struct Tool_Digital_Output_
{
  typedef Tool_Digital_Output_<ContainerAllocator> Type;

  Tool_Digital_Output_()
    : num(0)
    , state(false)  {
    }
  Tool_Digital_Output_(const ContainerAllocator& _alloc)
    : num(0)
    , state(false)  {
  (void)_alloc;
    }



   typedef uint8_t _num_type;
  _num_type num;

   typedef uint8_t _state_type;
  _state_type state;





  typedef boost::shared_ptr< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> const> ConstPtr;

}; // struct Tool_Digital_Output_

typedef ::rm_75_msgs::Tool_Digital_Output_<std::allocator<void> > Tool_Digital_Output;

typedef boost::shared_ptr< ::rm_75_msgs::Tool_Digital_Output > Tool_Digital_OutputPtr;
typedef boost::shared_ptr< ::rm_75_msgs::Tool_Digital_Output const> Tool_Digital_OutputConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator1> & lhs, const ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator2> & rhs)
{
  return lhs.num == rhs.num &&
    lhs.state == rhs.state;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator1> & lhs, const ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rm_75_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> >
{
  static const char* value()
  {
    return "65c6f886a7277e2391d226ec90152e72";
  }

  static const char* value(const ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x65c6f886a7277e23ULL;
  static const uint64_t static_value2 = 0x91d226ec90152e72ULL;
};

template<class ContainerAllocator>
struct DataType< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rm_75_msgs/Tool_Digital_Output";
  }

  static const char* value(const ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 num\n"
"bool state\n"
;
  }

  static const char* value(const ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.num);
      stream.next(m.state);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Tool_Digital_Output_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rm_75_msgs::Tool_Digital_Output_<ContainerAllocator>& v)
  {
    s << indent << "num: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.num);
    s << indent << "state: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.state);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RM_75_MSGS_MESSAGE_TOOL_DIGITAL_OUTPUT_H
