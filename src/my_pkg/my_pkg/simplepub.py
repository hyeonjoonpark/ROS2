import rclpy as rp
import rclpy.node import Node # type: ignore

def print_hello():
    print('Hello World!')


def main():
    rp.init()
    node = Node('simplepub')

    rp.spin(node)
    node.create_timer(1.0, print_hello)
    
if __name__ == '__main__':
    main()
