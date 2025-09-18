import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DiamondController(Node):
    def __init__(self):
        super().__init__('diamond_controller')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.time = 0

    def create_twist(self, linear_x, angular_z):
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        return msg

    def get_twist_msg(self):
        if self.time < 2:
            msg = self.create_twist(0.0, 0.787)
        elif self.time >= 2 and self.time < 7:
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 7 and self.time < 9:
            msg = self.create_twist(0.0, 1.574)
        elif self.time >= 9 and self.time < 14:
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 14 and self.time < 16:
            msg = self.create_twist(0.0, 1.574)
        elif self.time >= 16 and self.time < 21:
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 21 and self.time < 23:
            msg = self.create_twist(0.0, 1.574)
        elif self.time >= 23 and self.time < 28:
            msg = self.create_twist(1.0, 0.0)
        else:
            msg = self.create_twist(0.0, 0.0)
        return msg
    
    def timer_callback(self):
        msg = self.get_twist_msg()       
        self.publisher.publish(msg)
        self.time += 1

def main(args=None):
    rclpy.init(args=args)

    diamond_controller = DiamondController()

    rclpy.spin(diamond_controller)
    
    diamond_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
