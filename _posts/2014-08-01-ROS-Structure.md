---
layout: post
title: ROS Structure
---

**Nodes**

- Process which perform specific computation

e.g.:
- Control robot wheel motors / servos etc.
- Obtain data from sensor i.e. laser sensor, vision etc.
- Acquire image and sound i.e. from camera / microphone
- Perform localization (later topic) / compute path planning
- Graphical representation of the overall system

- Exchange Data via Ros messages
- Can run multiple Nodes via Nodelets

**Advantages to Nodelets (multiple Nodes):**

- Provide a way to run multiple nodes (algorithms) on:
- Single machine
- Single process
- Reduce cost interprocess message passing

Note! Master is the core / main node for ROS, called roscore!



**ROS Master (roscore)**

- Akin to Internet DNS (domain name server)
- Core node of ROS 
- Provides name registration and lookup to the rest of the computation computation graph(the visual -  representation of the system)
- Every node registers with Master upon startup / at runtime
    - Fetch registration information (subscribe or publish to a given topic) 
    - Establish direct connections as appropriate
    - Make callbacks to nodes when registration information changes (i.e. Event handler)
    - Allows nodes to dynamically create connections as necessary (i.e. new nodes are run)



**ROS Parameter Server**

- Akin to dictionary in c# or python
- Shared
- Accessible via network APIs
- Belongs to ROS Master
- Storage space for parameters
- Accessed by Nodes at runtime
- Not designed for high performance / Better suited for configuration parameters (arguments / data passed to functions)
- Follows ROS naming (namespaces) convention to Avoid conflicts

![ROS Parameter Server Diagram]({{ site.url }}/assets/images/param-server.jpg)



**Parameter Server Example:**

Commands : list and get

Open a terminal window and run:
- $ roscore

**In a new terminal windows / tab**

- List parameters
    - $ rosparam list

- Get distribution /  version 
    - $ rosparam get /rosdistro



**ROS Messages**

Message
- A data structure which consists of typed fields

Data types Supported:

- Primitive types:
    - Int{8, 16, 32, 64} i.e. short uint int long unsigned long 
    - Float {32, 64}
    - String
    - Time
    - Duration (seconds)
    - Array [ ]
    
- Nodes communicate by exchanging Messages. 
- Messages are routed via transport system with publish / subscribe semantics
- Non-blocking when used with topic *.msg (n:n)
- You can have as many ROS topics publishing and subscribing
- Blocking when used with service *.serv (1:1 request + respond)
- Services must only provide and request the same type


**ROS Messages Commands**

- $ rosmsg list : lists the current messages
- $ rosmsg show <message name>/Type : Show the contents of message i.e. Message type :
- e.g.
 - $ rosmsg show geometry_msgs/Vector3

![msg show vector3]({{ site.url }}/assets/images/msg-show-vector3.jpg)

- $ rosmsg show geometry_msgs/Twist

![msg show vector3]({{ site.url }}/assets/images/msg-show-vector3.jpg)



**ROS Topics**

- Nodes send messages by publishing it to a given ROS Topic
- Topic type must match the message type
    - Defined by the message type published to it
- If a Node needs a certain type of data it must subscribe to the appropriate Topic
- Multiple Nodes can publish and subscribe to the same topic
- A single Node may publish / subscribe to multiple Topics
- Publishers and Subscribers are unaware of each other's existence WHY?
- Publish / Subscribe model flexible paradigm i.e. many-to-many one way transport
- There is no order of execution


![ROS topics diagram]({{ site.url }}/assets/images/ros-topicdiagram.jpg)



**ROS Services**

- ROS services implement the request / reply functionality
- Pair of message struct : {reply, request}
- Node provider (Server) offer service under specific names
- A client node uses the service by sending the request message and awaits a reply
 - e.g. Remote procedure call

![ROS Services Diagram]({{ site.url }}/assets/images/ros-topicdiagram.jpg)

- The Listener Node request service from ROS Master
- Talker Node publishes service to ROS master

**ROS Services Commands**

To View details of ROS services
- $ rossrv list	: lists all available services 
- $ rossrv show <Node_name>/<service name or double tab to list all avaialble>
e.g.

![ROS Services Commands]({{ site.url }}/assets/images/service-cmds.jpg)



















