---
layout: default
title: Home
---

# CPTS 483 Fall 2015 Intro to Robotics #



Welcome to Cpts 483 Fall 2015. This repository is intended to be used as a ROS (Robot Operating System) workspace to aid in
learning about ROS and robotics. 

This is an introductory Robotics course in ROS, it will cover an overview of what ROS is, the way it works, and how you use it to control a robot. You will learn to use the command line to launch ROS and control its operation. 


## Usage ##

Clone this repository to your home directory

    $ git clone https://github.com/faustino-lukolo/Cpts483-Intro-To-Robotics.git

Open a terminal window:

Navigate to the src folder of the Repo and initialize the catkin workspace

    $ cd Cpts483-Intro-To-Robotics/src
    $ catkin_init_workspace

Navigate to the Cpts483-Intro-To-Robotics directory and build the workspace:

    $ cd ..
    $ catkin_make
    

### Source your devel folder to use this Repo as a default ROS workspace ###

    $ echo "source ~/Cpts483-Intro-To-Robotics/devel/setup.bash" >> ~/.bashrc
    $ source ~/.bashrc


you can now use this workspace and all the packages within it. Be sure to not push any commits as this is meant to be a standalone workspace hence no need to push your code to this 
repository. Instead create a git-hub account and copy the content of this repository to your own git-hub account





