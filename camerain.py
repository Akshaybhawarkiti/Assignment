#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class WebcamPublisher(Node):
    def __init__(self):
        super().__init__('webcam_publisher')
        self.publisher_ = self.create_publisher(Image, 'rawfeed', 10)
        self.bridge = CvBridge()

        # Open the webcam (0 = default camera)
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.get_logger().error("Could not open webcam.")
            exit(1)

        # Publish at ~30 FPS
        timer_period = 1/30
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info("Webcam publisher started, publishing on /rawfeed")

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().warning("Failed to grab frame from webcam")
            return

        # Convert from OpenCV (BGR) to ROS2 Image
        ros_image = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        self.publisher_.publish(ros_image)

    def destroy_node(self):
        self.cap.release()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = WebcamPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

