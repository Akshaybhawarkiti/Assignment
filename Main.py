import pybullet as p
import pybullet_data
import time
import math
import tkinter as tk
from threading import Thread

# Shared variable for coordinates
coords = [0.0, 0.0, 0.0]

def pybullet_loop():
    global coords

    # ---- PyBullet setup ----
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    robot = p.loadURDF(
        r"C:\Users\HP\Desktop\Mowito Assignment\maths\visualize forward kinematics\mowito\mowito.urdf",
        useFixedBase=True
    )

    joint_indices = [0, 1, 2, 3]
    link_index_for_ball = 4

    joint_sliders = [
        p.addUserDebugParameter(f"Joint {i+1} angle (deg)", -180, 180, 0)
        for i in range(len(joint_indices))
    ]

    radius = 0.03
    ball_vis = p.createVisualShape(p.GEOM_SPHERE, radius=radius, rgbaColor=[1, 0, 0, 1])
    ball = p.createMultiBody(baseMass=0, baseVisualShapeIndex=ball_vis, basePosition=[0, 0, 0])

    while True:
        # Read sliders and move joints
        for idx, slider_id in zip(joint_indices, joint_sliders):
            angle_deg = p.readUserDebugParameter(slider_id)
            angle_rad = math.radians(angle_deg)
            p.resetJointState(robot, idx, angle_rad)

        # Get ball position
        link_state = p.getLinkState(robot, link_index_for_ball)
        link_pos = link_state[0]
        coords = list(link_pos)  # update shared variable

        # Move ball
        p.resetBasePositionAndOrientation(ball, link_pos, [0, 0, 0, 1])

        p.stepSimulation()
        time.sleep(0.01)

# ---- Tkinter UI ----
root = tk.Tk()
root.title("Ball Coordinates")
root.geometry("250x120")

label_x = tk.Label(root, text="X = 0.000", font=("Arial", 14))
label_x.pack(pady=5)

label_y = tk.Label(root, text="Y = 0.000", font=("Arial", 14))
label_y.pack(pady=5)

label_z = tk.Label(root, text="Z = 0.000", font=("Arial", 14))
label_z.pack(pady=5)

def update_labels():
    label_x.config(text=f"X = {coords[0]:.3f}")
    label_y.config(text=f"Y = {coords[1]:.3f}")
    label_z.config(text=f"Z = {coords[2]:.3f}")
    root.after(50, update_labels)  # update every 50 ms

# Start PyBullet in another thread
Thread(target=pybullet_loop, daemon=True).start()

# Start updating labels
update_labels()

# Run Tkinter main loop in the main thread
root.mainloop()
