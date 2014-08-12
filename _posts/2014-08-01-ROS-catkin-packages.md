---
layout: post
title: Creating catkin packages
---


**Overview:**

**rosed:**

Quickly see/edit a file of a given package rosed is part of the rosbash suite. 

- $ echo $EDITOR (default is vi, if blank)
- $ export EDITOR=gedit
- $ rosed <pkg name> <file name>
    - e.g. $ rosed turtlesim package.xml


**Catkin Create: **

![stage simulator]({{ site.url }}/assets/images/catkin-create.jpg)

**Examining my_pkg:/**

![stage simulator]({{ site.url }}/assets/images/examine-package.jpg)

- $ rospack profile : displays all the directories that contain packages

Read more: *http://wiki.ros.org/rospack*


**Building ROS packages**

Before you can user your new packages you must first build your package.
Change directorys to catkin workspace directory

- $ cd ~/catkin_ws
- $ catkin_make















