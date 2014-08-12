---
layout: post
title: ROS Filesystem
--- 

**ROS Packages**

- Lowest level of ROS software organization
- Single functionality 
    - (e.g. acquisition and publication of laser data messages)
- Only one package per folder per workspace

Types of packages:

- Rosbuild packages (also known as dry packages)
- Catkin Packages (recommended aka wet packages)

**Rosbuild Packages (dry! deprecated)**

Maifest.xml:

- Information about the package
    - e.g. Author, License etc.
- Defines the dependencies on other packages

Makefile:

- Make build specifications

CMakeLists.txt:

- CMake build specifications

Catkin Packages (wet):

Package.xml:

- Information about the package
    - e.g. Author, License etc.
    
CMakeLists.txt:

- Contains CMake build specifications 
- Uses catkin macros

Note!!! Catkin packages cannot depend on Rosbuild packages


**Stacks – rosbuild (deprecated!):**

- Group packages to provide a more abstract functionality
- Packages within stack folder are consider part of the stack

Stack.xml:

- Metadata and declared dependencies on other stacks


**Metapackages – catkin (recommended):**

- Grouping packages as a single logical package

package.xml:

- Includes meta data
- Can only have dependencies on packages grouped by the metapackage
- Packages which are not in the metapackage can not depend on the meta package 

**A typical catkin package:**

my_pkg/

- CmakeLists.txt: CMake build settings for my_pkg
- manifest.xml:   Metadata and dependencies required by my_pkg/
- mainpage.dox:   Doxygen info of package my_pkg
- Include/my_pkg: C++ header files
- Src/:           source code directory


**ROS Commandline Tools:**

![stage simulator]({{ site.url }}/assets/images/rosbash.jpg)