#!/bin/bash

# create catkin workspace for husky_fei in /home/user
cd $HOME
mkdir -p catkin_ws/src
cd $HOME/catkin_ws/src
catkin_init_workspace
cd $HOME/catkin_ws
catkin_make

# make sure husky_fei_ws is sourced when new terminals are opened
echo ``source $HOME/catkin_ws/devel/setup.bash'' >> $HOME/.bashrc

# configure gazebo environment variables
echo ``source /usr/share/gazebo-1.9/setup.sh'' >> $HOME/.bashrc

echo ``declare -x GAZEBO_MASTER_URI="http://localhost:11345" ''  >> $HOME/.bashrc
echo ``declare -x GAZEBO_MODEL_DATABASE_URI="/usr/share/gazebo_models" ''  >> $HOME/.bashrc
echo ``declare -x GAZEBO_MODEL_PATH="/home/gazebo_models:/usr/share/gazebo_models" ''  >> $HOME/.bashrc
echo ``declare -x GAZEBO_PLUGIN_PATH="/usr/lib/gazebo-1.9/plugins" ''  >> $HOME/.bashrc
echo ``declare -x GAZEBO_RESOURCE_PATH="/home/gazebo_models:/usr/share/gazebo-1.9:/usr/share/gazebo_models" ''  >> $HOME/.bashrc

