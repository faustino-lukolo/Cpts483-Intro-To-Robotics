#!/usr/bin/env python
import rospy

# Messages
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist, Vector3
from ardrone_autonomy.msg import Navdata


def callback(navdata):
    # reassign the variable to t
    t = navdata    
    # print navdata message
    print("received odometry messages:  battery=%f vx=%f vy=%f z=%f yaw=%f"(t.batteryPercent,t.vx,t.vy,t.altd,t.rotZ))

# Main method start
if __name__ == "__main__":
    # initialize the node
    rospy.init_node('fly_square_node', anonymous = True)
    
    # subscribe to navdata (receive from quadrotor)
    rospy.Subscriber("/ardrone/navdata", Navdata, callback)
    
    # publish commands (send to quadrotor)
    pub_velocity = rospy.Publisher('/cmd_vel', Twist)
    pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty)
    pub_land = rospy.Publisher('/ardrone/land', Empty)
    pub_reset = rospy.Publisher('/ardrone/reset', Empty)  
     
    # Publishing messages
    print("ready!")
    rospy.sleep(2.0)
    
    print("takeoff..")
    pub_takeoff.publish(Empty())
    rospy.sleep(5.0)
    
    # Increase Altitude
    pub_velocity.publish(Twist(Vector3(0,0.8,0),Vector3(0,0,0)))
    rospy.sleep(5.0)
      
    while not rospy.is_shutdown():
      # fly forward..
      pub_velocity.publish(Twist(Vector3(1,0,0),Vector3(0,0,0)))
      rospy.sleep(5.0)
      
      # Hover for 2 seconds
      pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0.1,0.1,0)))
      rospy.sleep(2.0)
     
      # Turn 
      pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0,0,1)))
      rospy.sleep(2.0)
      
      
      # Hover for 2 seconds
      pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0.1,0.1,0)))
      rospy.sleep(2.0)

      # fly forward..
      pub_velocity.publish(Twist(Vector3(1,0,0),Vector3(0,0,0)))
      rospy.sleep(5.0)
      

      # Hover for 2 seconds
      pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0.01,0.01,0)))
      rospy.sleep(2.0)

      
      # Turn
      pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0,0,1)))
      rospy.sleep(2.0)


      # Hover for 2 seconds
      pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0.1,0.1,0)))
      rospy.sleep(2.0)

      # fly forward..
      pub_velocity.publish(Twist(Vector3(1,0,0),Vector3(0,0,0)))
      rospy.sleep(5.0)


     # Hover for 2 seconds
      pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0.01,0.01,0)))
      rospy.sleep(2.0)


      # Turn
      pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0,0,1)))
      rospy.sleep(2.0)


      # Hover for 2 seconds
      pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0.1,0.1,0)))
      rospy.sleep(2.0)

      # fly forward..
      pub_velocity.publish(Twist(Vector3(1,0,0),Vector3(0,0,0)))
      rospy.sleep(5.0)


      pub_land.publish(Empty())
