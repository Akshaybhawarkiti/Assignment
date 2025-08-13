#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import tkinter as tk


class ModePublisher(Node):
    def __init__(self):
        super().__init__('mode_publisher_ui')
        self.publisher_ = self.create_publisher(Int32, 'mode', 10)

    def publish_mode(self, mode_value: int):
        msg = Int32()
        msg.data = mode_value
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published mode: {mode_value}")


def main(args=None):
    rclpy.init(args=args)
    node = ModePublisher()

    # Tkinter UI
    root = tk.Tk()
    root.title("Feed Mode Controller")
    root.geometry("300x200")

    tk.Label(root, text="Select Feed Mode", font=("Arial", 14)).pack(pady=10)

    btn_rgb = tk.Button(
        root,
        text="Normal Feed",
        font=("Arial", 12),
        width=15,
        command=lambda: node.publish_mode(2)  # 2 = RGB
    )
    btn_rgb.pack(pady=5)

    btn_gray = tk.Button(
        root,
        text="Grayscale Feed",
        font=("Arial", 12),
        width=15,
        command=lambda: node.publish_mode(1)  # 1 = Gray
    )
    btn_gray.pack(pady=5)

    btn_canny = tk.Button(
        root,
        text="Canny Edge",
        font=("Arial", 12),
        width=15,
        command=lambda: node.publish_mode(3)  # 3 = Canny edge detection
    )
    btn_canny.pack(pady=5)

    # Integrate ROS2 spinning into Tkinter loop
    def tk_loop():
        rclpy.spin_once(node, timeout_sec=0.01)
        root.after(10, tk_loop)

    root.after(10, tk_loop)
    root.mainloop()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

