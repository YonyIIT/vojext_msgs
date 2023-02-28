// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from vojext_msgs:msg/RobotGraspingStrategies.idl
// generated code does not contain a copyright notice

#ifndef VOJEXT_MSGS__MSG__DETAIL__ROBOT_GRASPING_STRATEGIES__TRAITS_HPP_
#define VOJEXT_MSGS__MSG__DETAIL__ROBOT_GRASPING_STRATEGIES__TRAITS_HPP_

#include "vojext_msgs/msg/detail/robot_grasping_strategies__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const vojext_msgs::msg::RobotGraspingStrategies & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_yaml(msg.header, out, indentation + 2);
  }

  // member: type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.type.size() == 0) {
      out << "type: []\n";
    } else {
      out << "type:\n";
      for (auto item : msg.type) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: location
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "location: ";
    value_to_yaml(msg.location, out);
    out << "\n";
  }

  // member: timetolift
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timetolift: ";
    value_to_yaml(msg.timetolift, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const vojext_msgs::msg::RobotGraspingStrategies & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<vojext_msgs::msg::RobotGraspingStrategies>()
{
  return "vojext_msgs::msg::RobotGraspingStrategies";
}

template<>
inline const char * name<vojext_msgs::msg::RobotGraspingStrategies>()
{
  return "vojext_msgs/msg/RobotGraspingStrategies";
}

template<>
struct has_fixed_size<vojext_msgs::msg::RobotGraspingStrategies>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<vojext_msgs::msg::RobotGraspingStrategies>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<vojext_msgs::msg::RobotGraspingStrategies>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // VOJEXT_MSGS__MSG__DETAIL__ROBOT_GRASPING_STRATEGIES__TRAITS_HPP_
