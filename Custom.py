import math
import threading
import tkinter as tk
from tkinter import scrolledtext
import numpy as np
import matplotlib.pyplot as plt

# ---------------- Conversion Functions ---------------- #

def euler_to_quaternion(roll, pitch, yaw):
    roll = math.radians(roll)
    pitch = math.radians(pitch)
    yaw = math.radians(yaw)
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

# ---------------- Visualization ---------------- #

def quaternion_to_matrix(q):
    w, x, y, z = q
    return np.array([
        [1 - 2*(y*y + z*z),     2*(x*y - z*w),     2*(x*z + y*w)],
        [    2*(x*y + z*w), 1 - 2*(x*x + z*z),     2*(y*z - x*w)],
        [    2*(x*z - y*w),     2*(y*z + x*w), 1 - 2*(x*x + y*y)]
    ])

def visualize_orientation(q):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

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
    plt.show()

# ---------------- Action Function ---------------- #

def convert_and_visualize(output_box, roll_entry, pitch_entry, yaw_entry):
    try:
        roll = float(roll_entry.get())
        pitch = float(pitch_entry.get())
        yaw = float(yaw_entry.get())

        quat = euler_to_quaternion(roll, pitch, yaw)

        output_box.insert(tk.END, f"Input Euler (deg): roll={roll:.2f}, pitch={pitch:.2f}, yaw={yaw:.2f}\n")
        output_box.insert(tk.END, f"Quaternion: w={quat[0]:.4f}, x={quat[1]:.4f}, y={quat[2]:.4f}, z={quat[3]:.4f}\n\n")
        output_box.see(tk.END)

        visualize_orientation(quat)

    except ValueError:
        output_box.insert(tk.END, "Invalid input! Please enter numbers.\n")
        output_box.see(tk.END)

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Euler → Quaternion Converter")

# Input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Roll (°):").grid(row=0, column=0)
roll_entry = tk.Entry(input_frame, width=10)
roll_entry.grid(row=0, column=1)

tk.Label(input_frame, text="Pitch (°):").grid(row=0, column=2)
pitch_entry = tk.Entry(input_frame, width=10)
pitch_entry.grid(row=0, column=3)

tk.Label(input_frame, text="Yaw (°):").grid(row=0, column=4)
yaw_entry = tk.Entry(input_frame, width=10)
yaw_entry.grid(row=0, column=5)

# Output box
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15, font=("Courier", 10))
output_box.pack(padx=10, pady=10)

# Button
convert_button = tk.Button(root, text="Convert & Visualize",
    command=lambda: threading.Thread(target=convert_and_visualize, args=(output_box, roll_entry, pitch_entry, yaw_entry), daemon=True).start(),
    width=20, height=2)
convert_button.pack(pady=10)

root.mainloop()
