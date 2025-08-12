# Task 2 - Forward Kinematics Visualization with Live Coordinates

This Python program uses PyBullet to visualize a robot arm's forward kinematics in 3D, while a Tkinter GUI displays the live coordinates (X, Y, Z) of a specific link in real-time.
It allows you to move the robot joints using on-screen sliders and instantly see both the robot’s movement and the corresponding position values of the link.

# Main Features:

- Interactive PyBullet 3D simulation of a robot arm.  
- Adjustable joint angles using on-screen sliders (degrees).  
- A red ball marker is attached to the chosen link for easy position tracking.  
- Live X, Y, Z coordinate display in a separate Tkinter window.  
- Forward kinematics visualization without needing manual math calculations.  
- Real-time updates with smooth motion.  
- GUI and simulation run simultaneously via multi-threading.

# Dependencies or Libraries to Download

pybullet
pybullet_data
time
math
tkinter
threading

# How to use (Main Code)

1. Copy the program from the .py file and paste it in your compiler (I used VS Code).
   Note: Update the .urdf file path in the code to your robot’s URDF file location.

3. Download all dependencies mentioned above.
4. Run the program — PyBullet will open the 3D simulation window, and Tkinter will open the coordinate display window.
5. Adjust the sliders in PyBullet to move the robot and watch the coordinates update live.
