#!/usr/bin/env python
import rospy
from std_msgs.msg import Empty

if __name__ == "__main__":
    
    rospy.init_node("takeoff_node", anonymous = True)
    
    # publish std_msgs Empty to /ardrone/takeoff topic
    pub_takeoff = rospy.Publisher("/ardrone/takeoff", Empty)
    pub_land = rospy.Publisher("/ardrone/land", Empty)
    pub_reset = rospy.Publisher("/ardrone/reset", Empty)
    
    
    print("Ignition")
    rospy.sleep(1)
    
    # Take off
    pub_takeoff.publish(Empty())
    rospy.sleep(10)
    
    # land
    pub_land.publish(Empty())
   
    print("Success")
     
    
    
    