import rospy

from danasim_controller import BasicDroneController
from drone_video_display import DroneVideoDisplay

# QT libraries

# Finally the GUI libraries
from PySide import QtCore, QtGui

class AutonomousController(DroneVideoDisplay):
    def __init__(self):
        super(AutonomousController, self).__init__()
        
        self.pitch = 0
        self.roll = 0
        self.yaw_velocity = 0
        self.z_velocity = 0
        
    def TestFlight(self):
        controller.sendTakeoff
        rospy.sleep(2)
        controller.sendLand()
        
if __name__ == '__main__':
    import sys
    
    rospy.init_node('takeoff_N_Land')
    controller = BasicDroneController
    display = AutonomousController
    
    display.show()
    rospy.sleep(5)
    TestFlight()
    status = app.exec_()
    
    rospy.signal_shutdown("Done")
    sys.exit(status)
    
    
    
    
    
    
    
    
        