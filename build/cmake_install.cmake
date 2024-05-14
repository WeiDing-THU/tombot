# Install script for directory: /home/lfh/catkin_ws/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/lfh/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/lfh/catkin_ws/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/lfh/catkin_ws/install" TYPE PROGRAM FILES "/home/lfh/catkin_ws/build/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/lfh/catkin_ws/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/lfh/catkin_ws/install" TYPE PROGRAM FILES "/home/lfh/catkin_ws/build/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/lfh/catkin_ws/install/setup.bash;/home/lfh/catkin_ws/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/lfh/catkin_ws/install" TYPE FILE FILES
    "/home/lfh/catkin_ws/build/catkin_generated/installspace/setup.bash"
    "/home/lfh/catkin_ws/build/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/lfh/catkin_ws/install/setup.sh;/home/lfh/catkin_ws/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/lfh/catkin_ws/install" TYPE FILE FILES
    "/home/lfh/catkin_ws/build/catkin_generated/installspace/setup.sh"
    "/home/lfh/catkin_ws/build/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/lfh/catkin_ws/install/setup.zsh;/home/lfh/catkin_ws/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/lfh/catkin_ws/install" TYPE FILE FILES
    "/home/lfh/catkin_ws/build/catkin_generated/installspace/setup.zsh"
    "/home/lfh/catkin_ws/build/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/lfh/catkin_ws/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/lfh/catkin_ws/install" TYPE FILE FILES "/home/lfh/catkin_ws/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/lfh/catkin_ws/build/gtest/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/aws-robomaker-small-house-world/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/cobot_moveit_config/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/SLAM/openslam_gmapping/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/ranger_mini_V2/ranger_mini_control/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/ranger_mini_V2/ranger_mini_v2_gazebo/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/rm_75_robot/rm_75_bringup/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/rm_75_robot/rm_75_moveit_config/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/rm_75_robot/rm_75_robot/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/SLAM/slam_gmapping/slam_gmapping/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/ranger_mini_V2/four_wheel_steering_msgs/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/hello_world/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/rm_75_robot/rm_75_msgs/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/rm_75_robot/rm_75_demo/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/rm_75_robot/rm_75_driver/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/rm_75_robot/rm_75_description/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/rm_75_robot/rm_75_control/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/SLAM/depthimage_to_laserscan/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_nav/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/SLAM/slam_gmapping/gmapping/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/SLAM/localizer/rf2o_laser_odometry/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/install/robot_pose_ekf/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/dh_ag95_description/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/rm_75_robot/rm_75_gazebo/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/cobot_description/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/ranger_mini_V2/ranger_mini_v2/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/sim912/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/moveit_tutorials/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/ranger_mini_V2/urdf_geometry_parser/cmake_install.cmake")
  include("/home/lfh/catkin_ws/build/cobot_s_sim/ranger_mini_V2/four_wheel_steering_controller/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/lfh/catkin_ws/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
