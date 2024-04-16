import rclpy as rp
import rclpy.node import Node # type: ignore
from geometry_msgs.msg import Twist



class SimplePub(Node):
    def __init__(self):
        super().__init__('simplepub')
        self.create_timer(1, self.print_hello)
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def print_hello(self):
        msg = Twist()
        msg.linear.x = 0.5
        msg.linear.z = 0.0
        self.pub.publish(msg)


def main():
    rp.init()
    node = SimplePub()
    rp.spin(node)
    node.create_timer(1.0, print_hello)
    
if __name__ == '__main__':
    main()
