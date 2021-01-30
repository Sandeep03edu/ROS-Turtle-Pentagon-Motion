#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897
X_angle = 1.32
# X_angle = 1.318

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    speed = 1
    distance = 2
    distance_1 = 0
    vel_msg.linear.x = 1

    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)

	distance_1 = distance_1 + current_distance
	# print ("Distance 1 is " + str(distance_1))

        #After the loop, stops the robot
        vel_msg.linear.x = 0

	if distance_1 > 10:
		t0 = rospy.Time.now().to_sec()
		current_angle = 0
		angular_speed = 0.5
		vel_msg.angular.z = 1.05
		while(current_angle < 0.1):
	        	velocity_publisher.publish(vel_msg)
	        	t1 = rospy.Time.now().to_sec()
	        	current_angle = angular_speed*(t1-t0)

		velocity_publisher.publish(vel_msg)
    		rospy.spin()
         

# Path 1 Rotate start
	
        vel_msg.angular.z = 2
	angular_speed = 0.5
	current_angle = 0
	

	while(current_angle < X_angle):
        	velocity_publisher.publish(vel_msg)
        	t1 = rospy.Time.now().to_sec()
        	current_angle = angular_speed*(t1-t0)
		

	

	#Forcing our robot to stop
	vel_msg.angular.z = 0
	
#New

   	vel_msg.linear.x = 1
    	speed_2 = 1
    	distance_2 = 2

        #Setting the current time for distance calculus
    
    current_distance_2 = 0
    
    #Loop to move the turtle in an specified distance
    while(current_distance_2 < 2):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            
	    current_distance_2 = speed_2*(t1-t0)
	   
        #After the loop, stops the robot
            vel_msg.linear.x = 0
	 
	#Stopping complete robot
    velocity_publisher.publish(vel_msg)
    rospy.spin()
         

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
