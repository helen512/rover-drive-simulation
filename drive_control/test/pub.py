import time
import rospy
from geometry_msgs.msg import Twist
from drive_control.msg import WheelSpeed
    

def pub():
    robot_twist = Twist()
    robot_twist.angular.z = 45
    robot_twist.linear.x = 30
    # robot_twist.angular.z = 1500
    twist_pub = rospy.Publisher("rover_velocity_controller/cmd_vel", Twist, queue_size=10)
    
    feedback = WheelSpeed()
    feedback.left[0] = 0
    feedback.left[1] = 0
    feedback.right[0] = 200
    feedback.right[1] = 200
    feedback_pub = rospy.Publisher('/feedback_velocity', WheelSpeed, queue_size=10)

    rospy.init_node('test_pub', anonymous=True)
    i = 0
    while not rospy.is_shutdown():
        robot_twist.linear.x = 30 + i
        twist_pub.publish(robot_twist)
        feedback_pub.publish(feedback)
        time.sleep(0.5)
        i += 10
        




if __name__ == "__main__":
    pub()

    