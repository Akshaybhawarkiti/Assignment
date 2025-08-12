import math
import random
import time
import threading
import tkinter as tk
from tkinter import scrolledtext
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def euler_to_quaternion(roll, pitch, yaw):
    if any(math.isnan(a) or math.isinf(a) for a in [roll, pitch, yaw]):
        raise ValueError("Euler angles must be finite numbers.")
    roll = (roll + math.pi) % (2 * math.pi) - math.pi
    pitch = (pitch + math.pi) % (2 * math.pi) - math.pi
    yaw = (yaw + math.pi) % (2 * math.pi) - math.pi
    cr = math.cos(roll / 2)
    sr = math.sin(roll / 2)
    cp = math.cos(pitch / 2)
    sp = math.sin(pitch / 2)
    cy = math.cos(yaw / 2)
    sy = math.sin(yaw / 2)
    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy
    norm = math.sqrt(w*w + x*x + y*y + z*z)
    return (w / norm, x / norm, y / norm, z / norm)

def quaternion_to_euler(w, x, y, z):
    if any(math.isnan(a) or math.isinf(a) for a in [w, x, y, z]):
        raise ValueError("Quaternion components must be finite numbers.")
    norm = math.sqrt(w*w + x*x + y*y + z*z)
    if norm == 0:
        raise ValueError("Zero-length quaternion is invalid.")
    w, x, y, z = w / norm, x / norm, y / norm, z / norm
    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x * x + y * y)
    roll = math.atan2(sinr_cosp, cosr_cosp)
    sinp = 2 * (w * y - z * x)
    if abs(sinp) >= 1:
        pitch = math.copysign(math.pi / 2, sinp)
    else:
        pitch = math.asin(sinp)
    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y * y + z * z)
    yaw = math.atan2(siny_cosp, cosy_cosp)
    return (roll, pitch, yaw)


def generate_random_euler():
    roll = random.uniform(-math.pi, math.pi)
    pitch = random.uniform(-math.pi/2, math.pi/2)
    yaw = random.uniform(-math.pi, math.pi)
    return roll, pitch, yaw

def generate_random_quaternion():
    u1 = random.random()
    u2 = random.random()
    u3 = random.random()
    w = math.sqrt(1 - u1) * math.sin(2 * math.pi * u2)
    x = math.sqrt(1 - u1) * math.cos(2 * math.pi * u2)
    y = math.sqrt(u1) * math.sin(2 * math.pi * u3)
    z = math.sqrt(u1) * math.cos(2 * math.pi * u3)
    return (w, x, y, z)


def quaternion_to_matrix(q):
    w, x, y, z = q
    return np.array([
        [1 - 2*(y*y + z*z),     2*(x*y - z*w),     2*(x*z + y*w)],
        [    2*(x*y + z*w), 1 - 2*(x*x + z*z),     2*(y*z - x*w)],
        [    2*(x*z - y*w),     2*(y*z + x*w), 1 - 2*(x*x + y*y)]
    ])

def visualize_orientation(quaternions, delay=0.5):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for q in quaternions:
        ax.clear()
        R = quaternion_to_matrix(q)

      
        origin = np.array([0, 0, 0])
     
        axes = np.eye(3)
        colors = ['r', 'g', 'b']
        labels = ['X', 'Y', 'Z']

        for i in range(3):
            vec = R @ axes[:, i]
            ax.quiver(*origin, *vec, color=colors[i], length=1)
            ax.text(*vec, labels[i], color=colors[i], fontsize=12)

        ax.set_xlim([-1.5, 1.5])
        ax.set_ylim([-1.5, 1.5])
        ax.set_zlim([-1.5, 1.5])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title("3D Orientation Visualization")
        plt.pause(delay)

    plt.show()



def run_euler_to_quaternion(output_box, count=3, delay=0.5):
    quats = []
    for _ in range(count):
        roll, pitch, yaw = generate_random_euler()
        quat = euler_to_quaternion(roll, pitch, yaw)
        quats.append(quat)
        output_box.insert(tk.END, f"Euler (rad): roll={roll:.3f}, pitch={pitch:.3f}, yaw={yaw:.3f}\n")
        output_box.insert(tk.END, f"Quaternion: w={quat[0]:.4f}, x={quat[1]:.4f}, y={quat[2]:.4f}, z={quat[3]:.4f}\n\n")
        output_box.see(tk.END)
        time.sleep(delay)
    visualize_orientation(quats, delay)

def run_quaternion_to_euler(output_box, count=3, delay=0.5):
    quats = []
    for _ in range(count):
        quat = generate_random_quaternion()
        quats.append(quat)
        roll, pitch, yaw = quaternion_to_euler(*quat)
        output_box.insert(tk.END, f"Quaternion: w={quat[0]:.4f}, x={quat[1]:.4f}, y={quat[2]:.4f}, z={quat[3]:.4f}\n")
        output_box.insert(tk.END, f"Euler (rad): roll={roll:.3f}, pitch={pitch:.3f}, yaw={yaw:.3f}\n")
        output_box.insert(tk.END, f"Euler (deg): roll={math.degrees(roll):.2f}, pitch={math.degrees(pitch):.2f}, yaw={math.degrees(yaw):.2f}\n\n")
        output_box.see(tk.END)
        time.sleep(delay)
    visualize_orientation(quats, delay)



def start_thread(func, output_box):
    threading.Thread(target=func, args=(output_box,), daemon=True).start()

root = tk.Tk()
root.title("Euler <-> Quaternion Converter")

# Output box
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=("Courier", 10))
output_box.pack(padx=10, pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

btn1 = tk.Button(btn_frame, text="Euler > Quaternion", command=lambda: start_thread(run_euler_to_quaternion, output_box), width=20, height=2)
btn1.grid(row=0, column=0, padx=10, pady=5)

btn2 = tk.Button(btn_frame, text="Quaternion > Euler", command=lambda: start_thread(run_quaternion_to_euler, output_box), width=20, height=2)
btn2.grid(row=0, column=1, padx=10, pady=5)

root.mainloop()
