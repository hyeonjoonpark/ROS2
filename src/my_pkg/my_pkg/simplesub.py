import rclpy as rp
import rclpy.node import Node # type: ignore
from geometry_msgs.msg import Twist



class SimpleSub(Node):
    def __init__(self):
        super().__init__('simplesub')
        self.create_subscription(Twist, '/turtle1/cmd_vel', self.sub_callback, 10)

    def sub_callback(self, msg: Twist):
        print("linear.x: ", msg.linear.x)
        print("angular.z: ", msg.angular.z)

def main():
    rp.init()
    node = SimpleSub()
    try:
        rp.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rp.shutdown()
    
if __name__ == '__main__':
    main()
    