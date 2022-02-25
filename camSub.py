
#import rospy

#from sensor_msgs.msg import Image

#from cv_bridge import CvBridge,CvBridgeError
import cv2 as cv

import numpy as np

"""

dependencies cv2,numpy,ros,cv_bridge
"""
"""


cap = cv2.VideoCapture("webcamIp")
print(cap.isOpened())
bridge = CvBridge() 




"""
def startVideoCapture():
        #pub  = rospy.Publisher("webcam",Image,queue_size = 1)
        #rospy.init_node("spektrometer",anonymous = False)
        #rate = rospy.Rate(10)
        """
        while not rospy.is_shutdown():
            ret,frame  =cap.read()
            if not ret:
                break
            msg = bridge.cv2_to_imgmsg(frame,"bgr8")
            pub.publish(msg)
            
            if cv2.waitkey(1) & 0xFF == ord('q')
                break
            if rospy.is_shutdown():
                cap.release()
                
        
        if __name__ == '__main__':
            try:
                talker()
            except rospy.ROSInterruptException:
                pass
        
        
        
        
        
        """
    
        
        
startVideoCapture()
