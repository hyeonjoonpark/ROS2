import rclpy as rp
import rclpy.node import Node # type: ignore


class SimplePub(Node):
    def __init__(self):
        super().__init__('simplepub')
        self.create_timer(1.0, self.print_hello)

    def print_hello(self):
        print('Hello World!')


def main():
    rp.init()
    node = SimplePub()
    rp.spin(node)
    node.create_timer(1.0, print_hello)
    
if __name__ == '__main__':
    main()
