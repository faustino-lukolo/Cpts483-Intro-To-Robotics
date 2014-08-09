---
layout: post
title: Roslaunch
---


**roslaunch**

Advantages:

- Run everything all at once
- Reduce the number of open terminals
- Easily launch multiple ROS Nodes
- Allows the setting of parameters on Parameter Server
- Automatically re-spawn process which have died
- Can have one or more XML configuration files (.launch)
- Contains information about which nodes to launch and which parameters to set
- How nodes should be loaded

**Using Roslaunch**

Command :

- $ roslaunch [package_name] [filename.launch]

**Creating a launch file:**

- Open text editor
- Save the file in catkin workspace directory

eg. name:

- mimic.launch


**Creating Roslaunch**

Open text editor and type the following

![rostopic type]({{ site.url }}/assets/images/turtle-mimic.jpg)




**Exploring mimic.launch**

- Mimic node 

![rostopic type]({{ site.url }}/assets/images/mimic-node.jpg)

Notice that the mimic Node does not need to be in a namespace because its main purpose is to remap the keys from turtle1 to turtle2 Nodes which are in the turtlesim1 and turtlesim2 namespaces.


**Launching .launch files**

Close all terminals (shutdown nodes and roscore)

- $ cd [catkin workspace directory]
- $ roslaunch turtle_mimic.launch

Note that roscore is running because roslaunch command runs roscore at run time



![rostopic type]({{ site.url }}/assets/images/mimic-turtle.jpg)

The launch file contains definition for 2 turtlesim_nodes hence we have two window
Notice also that the name is the same for both windows


**rqt_graph representation**

- Check which topics are advertised / subscribed
- Try to publish message over /turtlesim/turtle1/cmd_vel topic

e.g. 

- $ rostopic pub -r /turtlesim1/turtle1/cmd_vel geometry_msgs/Twist '[x, y, z]' '[x, y, z]'
- Computation Graph Representation should look similar to this

![rostopic type]({{ site.url }}/assets/images/graph-mimic.jpg)


