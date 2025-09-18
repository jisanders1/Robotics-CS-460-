import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DiamondController(Node):
    # Initializing Publisher
    def __init__(self):
        super().__init__('diamond_controller')
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
        if self.time < 2:
            # Initial angle offset
            msg = self.create_twist(0.0, 0.787)
        elif self.time >= 2 and self.time < 7:
            # First side
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 7 and self.time < 9: 
            # Rotate
            msg = self.create_twist(0.0, 1.574)
        elif self.time >= 9 and self.time < 14:
            # Second side
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 14 and self.time < 16:
            # Rotate
            msg = self.create_twist(0.0, 1.574)
        elif self.time >= 16 and self.time < 21:
            # Third side
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 21 and self.time < 23:
            # Rotate
            msg = self.create_twist(0.0, 1.574)
        elif self.time >= 23 and self.time < 28:
            # Fourth side
            msg = self.create_twist(1.0, 0.0)
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
            diamond_controller = DiamondController()
            rclpy.spin(diamond_controller) # Starts turtle
    except (KeyboardInterrupt):
        diamond_controller.destroy_node()

if __name__ == '__main__':
    main()
