---
layout: post
title: ROS Computation Graph
---


**More Graph Concepts**

- rosout – similar to stdout / stderr (standard output )
- Roscore – Master + rosout + parameter server (rosparam)
 - ROS Master must be started before any other node. 


**Navigating ROS File System**

- Filesystem tools
 - Eliminates need to use standard bash commands such as cd and ls to navigate package directories.
 
![ROS Bash command list]({{ site.url }}/assets/images/service-cmds.jpg)


**$ rospack - Command**

- Get information about packages
- list packages currently available
- find the path of packages
- lists dependencies of packages

and more. . .

e.g. 
- $ rospack find turtlesim
- $ /opt/ros/hydro/share/turtlesim



**roscd - Command**

Usage: roscd [package name[/subdir]]

- Change to package directory
- Packages must be within directories listed in ROS PACKAGE PATH
- Executing roscd without specifying a package changes directory to ROS WORKSPACE/devel (if set)

**rosls - Command**

Usage: rosls [package name[/subdir]]

- Allow listing the contents of a package by name rather than by absolute path
- Packages must be within directories listed in ROS PACKAGE PATH

e.g.
![rosls command]({{ site.url }}/assets/images/service-cmds.jpg)




**Understanding ROS Nodes**

**$ rosnode**

- A command line tool for printing information about ROS Nodes currently running

$ rosnode list
 
- Lists the active Nodes

$ rosnode info /<node name>

e.g. 
$ roscore
$ rosnode list - will display a node /rosout
$ rosnode info /rosout - Prints information about node /rosout


**Executing a ROS Node**

- $ rosrun
 - Allows the use of package name to directly run a node (executable program) within the package

- Usage : rosrun [package_name] [node_name]
e.g. 

- $ rosrun turtlesim turtlesim_node

![rosrun command]({{ site.url }}/assets/images/rosrun.jpg)


**Understanding rosnode**

![rosnode command]({{ site.url }}/assets/images/rosnode.jpg)


**Understanding Topics**

![rostopic command]({{ site.url }}/assets/images/rostopic-bash.jpg)

**Understanding rosmsg**
![rosmsg command]({{ site.url }}/assets/images/rosmsg.jpg)

**Understanding rossrv**
![rosserv command]({{ site.url }}/assets/images/rosserv.jpg)



**Calling ROS services**

- With service currently active 
 - Use $ rosservice list : to view active services
 - Use $ rosservice call to call a service

![rosservice command]({{ site.url }}/assets/images/rosservice-call.jpg)

**e.g. **

- $ rosservice call /spawn 1.0 2.0 0.0 turtle2
- Now try to spawn a turtle in a different location.
- Experiment will all the rosservice calls
   

**ROS parameters**

ROS parameter server:

 - Shared Multi-variate dictionary
 - Accessible via network APIs

- Nodes use parameter server to store and retrieve parameters at run time
- Not designed for high performance
- Globally view / runs inside ROS Master via XMLRPC


**rosparam**

A command line tool for getting, setting and deleting parameters from ROS parameter server

![rosparam command]({{ site.url }}/assets/images/rosparam.jpg)

- **Using rosparm**
 - rosparam list: list parameters currently stored
 - rosparam get [param name]: get parameter value
 - rosparam set [param name]: set parameter value


![rosparam list command]({{ site.url }}/assets/images/rosparam-list.jpg)






























