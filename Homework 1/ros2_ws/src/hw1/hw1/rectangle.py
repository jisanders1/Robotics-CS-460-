import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RectangleController(Node):
    def __init__(self):
        super().__init__('rectangle_controller')
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
        if self.time < 5: #first line
            msg = self.create_twist(2.0, 0.0)
        elif self.time >= 5 and self.time < 7: #turn 1
            msg = self.create_twist(0.0, 1.574)
        elif self.time >= 10 and self.time < 15: #second line
            msg = self.create_twist(1.0, 0.0)
        elif self.time >= 15 and self.time < 17:
            msg = self.create_twist(0.0, 1.574)
        elif self.time >= 17 and self.time < 22:#third line
            msg = self.create_twist(2.0, 0.0)
        elif self.time >= 22 and self.time < 24:
            msg = self.create_twist(0.0, 1.574)
        elif self.time >= 24 and self.time < 29:#fourth line
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

    rectangle_controller = RectangleController()

    rclpy.spin(rectangle_controller)
    
    rectangle_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
