#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
# Declaring X_angle
X_angle = 1.32

def move():
    # Starts a new node
    rospy.init_node('turtlesim', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Declaring Variables
    speed = 1
    distance = 2
    distance_1 = 0
    vel_msg.linear.x = 1

    # Initialising Robot
    while not rospy.is_shutdown():

        #Setting the current time for distance calculation
        t0 = rospy.Time.now().to_sec()
        current_distance = 0
	
#Loop to move the turtle linearly
        while(current_distance < distance):
            #Velocity publishing
            velocity_publisher.publish(vel_msg)
            #Current Time
            t1=rospy.Time.now().to_sec()
            #Distance Calculation
            current_distance= speed*(t1-t0)

	# Variable to measure total distance covered
	distance_1 = distance_1 + current_distance
	
	#After the loop, stops the robot linearly
        vel_msg.linear.x = 0
	
# Turtle motion at the End :-
	#Rotating Robot to initial Orientation at the End
	if distance_1 > 10:
		t0 = rospy.Time.now().to_sec()
		current_angle = 0
		angular_speed = 0.5
		vel_msg.angular.z = 1.05
		while(current_angle < 0.1):
	        	velocity_publisher.publish(vel_msg)
	        	t1 = rospy.Time.now().to_sec()
	        	current_angle = angular_speed*(t1-t0)

	#Stopping Robot after completing path of 10m i.e., Pentagon path
		velocity_publisher.publish(vel_msg)
    		rospy.spin()
         

# Rotation start
	
        vel_msg.angular.z = 2
	angular_speed = 0.5
	current_angle = 0

	while(current_angle < X_angle):
        	velocity_publisher.publish(vel_msg)
        	t1 = rospy.Time.now().to_sec()
        	current_angle = angular_speed*(t1-t0)
	vel_msg.angular.z = 0
   	vel_msg.linear.x = 1
    	         

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
