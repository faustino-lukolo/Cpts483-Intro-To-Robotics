---
layout: post
title: ROS Environment Setup
---

**Environment Setup:**

- Create a new directory e.g. mkdir workspacename/src
- Navigate to /src directory of your workspace
- /src is the directory for all your packages i.e. ROS Package Path
- Create a link to point to /src directory i.e. catkin_init_workspace
- Finally build the workspaces

![stage simulator]({{ site.url }}/assets/images/environment-setup.jpg)

Note! 
This is only done once per workspace. You can have multiple workspace but can only source 
One workspace at a time. 


**Source devel/setup.bash:**

Once you have build your catkin space you can begin using this workspace. First Source your devel folder this allows the terminal to point to your ROS directory when running roscd.

![stage simulator]({{ site.url }}/assets/images/ws-setup.jpg)










