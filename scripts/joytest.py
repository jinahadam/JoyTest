#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy

def talker():
    pub = rospy.Publisher('joytester', Joy, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = Joy()
        msg.axes = (1,1,1,1,1,1,1)
        msg.buttons = (0,0,0,0,0,0,0,0,0,0,0)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
