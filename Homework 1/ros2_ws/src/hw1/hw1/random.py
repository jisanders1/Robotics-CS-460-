import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RandomController(Node):
    # Initializing Publisher
    def __init__(self):
        super().__init__('random_controller')
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
        if self.time < 5:
            # Initial angle offset
            msg = self.create_twist(0.0, 1.7)
        elif self.time >= 5 and self.time < 10:
            # First side
            msg = self.create_twist(2.0, 0.0)
        elif self.time >= 10 and self.time < 15:
            # Rotate
            msg = self.create_twist(0.0, 1.0)
        elif self.time >= 15 and self.time < 20:
            # Second side
            msg = self.create_twist(2.0, 0.0)
        elif self.time >= 20 and self.time < 25:
            # Rotate
            msg = self.create_twist(0.0, 1.0)
        elif self.time >= 25 and self.time < 30:
            # Third side
            msg = self.create_twist(2.0, 0.0)
        elif self.time >= 30 and self.time < 35:
            # Rotate
            msg = self.create_twist(0.0, 1.0)
        elif self.time >= 35 and self.time < 40:
            # Fourth side
            msg = self.create_twist(2.0, 0.0)
        elif self.time >= 40 and self.time < 45:
            # Rotate
            msg = self.create_twist(0.0, 1.01)
        elif self.time >= 45 and self.time < 50:
            # Fifth side
            msg = self.create_twist(2.0, 0.0)
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
            random_controller = RandomController()
            rclpy.spin(random_controller) # Starts turtle
    except (KeyboardInterrupt):
        random_controller.destroy_node()

if __name__ == '__main__':
    main()
