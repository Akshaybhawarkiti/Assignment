import tkinter as tk
from math import cos, sin, radians
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def dh_transform(a, alpha_deg, d, theta_deg):
    alpha = radians(alpha_deg)
    theta = radians(theta_deg)
    ca, sa = cos(alpha), sin(alpha)
    ct, st = cos(theta), sin(theta)
    return np.array([[ct, -st*ca,  st*sa, a*ct],[st,  ct*ca, -ct*sa, a*st],[0 ,sa,ca,d],[0 ,0, 0, 1]])


dh_params = [(1.0, -90, 0.0, 0.0), (1.0,  90, 0.0, 0.0), (1.0, -90, 0.0, 0.0),(1.0,  90, 0.0, 0.0)  ]

def compute_fk(theta_list):
    T = np.eye(4)
    positions = [T[:3, 3].copy()] 
    for i, (a, alpha, d, theta_off) in enumerate(dh_params):
        T = T @ dh_transform(a, alpha, d, theta_list[i] + theta_off)
        positions.append(T[:3, 3].copy())
    return positions 

def update_position(_=None):
    theta_vals = [
        slider_theta1.get(),
        slider_theta2.get(),
        slider_theta3.get(),
        slider_theta4.get()
    ]
    positions = compute_fk(theta_vals)
    ee = positions[-1]
    result_label.config(text=f"EE Position: x={ee[0]:.3f} m, y={ee[1]:.3f} m, z={ee[2]:.3f} m")
    plot_robot(positions)

def plot_robot(positions):
    ax.clear()
    ax.set_title("4-DOF Robot Visualization")
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (m)")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_zlim(-4, 4)

    xs, ys, zs = zip(*positions)
    ax.plot(xs, ys, zs, '-o', color='blue', markersize=8, linewidth=2)
    ax.scatter(xs[-1], ys[-1], zs[-1], color='red', s=50, label="End Effector")
    ax.legend()

    canvas.draw()


root = tk.Tk()
root.title("4-DOF Robot Forward Kinematics with Visualization")


slider_theta1 = tk.Scale(root, from_=0, to=180, orient="horizontal", label="Theta 1 (deg)", command=update_position)
slider_theta1.grid(row=0, column=0, columnspan=2)

slider_theta2 = tk.Scale(root, from_=0, to=180, orient="horizontal", label="Theta 2 (deg)", command=update_position)
slider_theta2.grid(row=1, column=0, columnspan=2)

slider_theta3 = tk.Scale(root, from_=0, to=180, orient="horizontal", label="Theta 3 (deg)", command=update_position)
slider_theta3.grid(row=2, column=0, columnspan=2)

slider_theta4 = tk.Scale(root, from_=0, to=180, orient="horizontal", label="Theta 4 (deg)", command=update_position)
slider_theta4.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="EE Position: x= , y= , z= ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)


fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111, projection='3d')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=2, rowspan=6)

update_position()

root.mainloop()
