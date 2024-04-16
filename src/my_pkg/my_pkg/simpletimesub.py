import rclpy as rp
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Header

class SimpleTimePub(Node):
    def __init__(self):
        super().__init__('simpleTimepub')
        self.create_timer(1, self.timer_callback)
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def timer_callback(self):
        msg = Header()
        msg.frame_id = 'time' + str(self.count)
        msg.stamp = self.get_clock().now().to_msg()
        self.pub.publish(msg)


def main():
    rp.init()
    node = SimpleTimePub()
    rp.spin(node)
    
if __name__ == '__main__':
    main()
