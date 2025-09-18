import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleController(Node):
    # Initializing Publisher
    def __init__(self):
        super().__init__('circle_controller')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.time = 0
        
    # Singular message that tells turtle where to go
    def create_twist(self, linear_x, angular_z):
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        return msg

    # Controls overall shape drawing
    def get_twist_msg(self):
        # Drawing the full circle only takes 4 seconds
        if self.time <= 4:
            # Progress with drawing
            msg = self.create_twist(2.5, 2.5)
        else:
            # Stop drawing
            msg = self.create_twist(0.0, 0.0)
        return msg
    
    # Function called after timer period has elapsed
    def timer_callback(self):
        msg = self.get_twist_msg()       
        self.publisher.publish(msg)
        self.time += 1

def main(args=None):
    # Program can be stopped via CTRL + C
    try:
        with rclpy.init(args=args):
            circle_controller = CircleController()
            rclpy.spin(circle_controller) # Starts turtle
    except (KeyboardInterrupt, ExternalShutdownException):
        circle_controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
