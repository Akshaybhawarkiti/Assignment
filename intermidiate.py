#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Int32
from cv_bridge import CvBridge
import cv2


class FeedEditor(Node):
    def __init__(self):
        super().__init__('feed_editor')

        # Subscribes to /rawfeed
        self.create_subscription(
            Image,
            'rawfeed',
            self.image_callback,
            10)

        # Subscribes to /mode (1 = grayscale, 2 = RGB, 3 = Canny edge detection)
        self.create_subscription(
            Int32,
            'mode',
            self.mode_callback,
            10)

        # Publishes to /editfeed
        self.publisher_ = self.create_publisher(Image, 'editfeed', 10)

        self.bridge = CvBridge()
        self.mode = 2  # Default: RGB

        self.get_logger().info("Feed Editor started: Subscribing to /rawfeed and /mode, publishing to /editfeed")

    def mode_callback(self, msg: Int32):
        if msg.data in [1, 2, 3]:
            self.mode = msg.data
            mode_name = {1: "Grayscale", 2: "RGB", 3: "Canny Edge"}[self.mode]
            self.get_logger().info(f"Mode changed: {mode_name}")
        else:
            self.get_logger().warn(f"Invalid mode received: {msg.data}")

    def image_callback(self, msg: Image):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        if self.mode == 1:  # Grayscale
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ros_image = self.bridge.cv2_to_imgmsg(frame, encoding="mono8")

        elif self.mode == 2:  # RGB (original)
            ros_image = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")

        elif self.mode == 3:  # Canny edge detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray_frame, 100, 200)
            ros_image = self.bridge.cv2_to_imgmsg(edges, encoding="mono8")

        self.publisher_.publish(ros_image)


def main(args=None):
    rclpy.init(args=args)
    node = FeedEditor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

