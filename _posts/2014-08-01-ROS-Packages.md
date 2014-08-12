---
layout: post
title: ROS Packages 
---

**ROS Packages**

- ROS packages must contain
- CMakeList.txt file
- package.xml

There can be no more than 1 package per folder


**Folder structure of a catkin_ws**

![rostopic type]({{ site.url }}/assets/images/catkin-folder-structure.jpg)

**dana_sim package**

- Create a package called dana_sim
 - $ roscreate_pkg dana_sim roscpp rospy std_msgs

- First order dependency check
 - $ rospack depends1 dana_sim

- Show all dependencies
 - $ rospack depends dana_sim
 
**Configuring catkin packages**

- You can edit package.xml to change the following information:
 
 ![rostopic type]({{ site.url }}/assets/images/config-packages.jpg
 
 
CMakeList.txt

 - CMake build system input for building software packages
 - How to build and where to place binaries (code)

 
**CMakeList.txt structure and Ordering**
 
 ![rostopic type]({{ site.url }}/assets/images/cmakelist.jpg 
 

**CMakeList.txt Break Down**

- CMake version
- Catkin requires version 2.8.3 or higher

Package Name

- Name of package
- Must match name in package.xml
- Also name of package director 
 
find_package() 

- specifies other CMake packages needed to build package
- At least one dependency on catkin

e.g.

- find_package(catkin REQUIRED)
- Other wet (catkin) packages are also components 
 - find_package(catkin REQUIRED COMPONENTS rocpp rospy)
- Boost, OpenCV and PCL are not catkin components
 - find_package(Boost REQUIRED COMPONENTS signals thread)
 

**Customizing CMakeList**

catkin_package()

- CMake macro
- Required to specify catkin-specific info to the build system
- Generates pkg-config and CMake files
- Called before declaring targets

**Args:**

- INCLUDE_DIRS: export include paths
- LIBRARIES: export libraries
- CATKIN_DEPENDS: other catkin packages
- DEPENDS: non-catkin CMake (system) dependencies
- CFG_EXTRAS: additional configurations options

Include paths
 
- Include_directories(include ${Boost_INCLUDE_DIRS} ${catkin_INCLUDE_DIRS})
- Shared library targets
- add_library (dana src/dana.cpp)
- Execitable targets
 - add_executable( dana_node src/main.cpp src/some_functions.cpp)
- target_link_libraries
 - target_link_libraries(dana ${catkin_LIBRARIES})
 - target_link_libraries(dana_node dummy ${Boost_LIBRARIES})















 
 
 