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
pybullet_date  
time  
math  
tkinter  
threading

# How to use (Main Code)

1. Copy the program from the .py file and paste it in your compiler (I used VS Code).

  Note: Update the .urdf file path in the code to your robot’s URDF file location.   
  main code link : https://github.com/Akshaybhawarkiti/Assignment/blob/forward-kinematics-of-the-robot/Main.py     
  Meshes and urdf : https://github.com/Akshaybhawarkiti/Assignment/blob/Meshes/README.md   
  
3. Download all dependencies mentioned above.
4. Run the program — PyBullet will open the 3D simulation window, and Tkinter will open the coordinate display window.
5. Adjust the sliders in PyBullet to move the robot and watch the coordinates update live.

# My Test Videos

1. Urdf Visualization    : https://github.com/Akshaybhawarkiti/Assignment/blob/forward-kinematics-of-the-robot/urdf.mp4
2. Operating in Pybullet : https://github.com/Akshaybhawarkiti/Assignment/blob/forward-kinematics-of-the-robot/movement%20visualized.mp4
3. Manual Mathametically : https://github.com/Akshaybhawarkiti/Assignment/blob/forward-kinematics-of-the-robot/mathematically.mp4
   
   Or   

1. Urdf Visualization    : https://drive.google.com/file/d/1Awl1yGFxE2n95alId7zvfr6Lt5RJiHfk/view?usp=drive_link
2. Operating in Pybullet : https://drive.google.com/file/d/18No_jR2iH69wTz1cSE7jdTtPWPwJnyl_/view?usp=drive_link
3. Manual Mathametically : https://github.com/Akshaybhawarkiti/Assignment/blob/forward-kinematics-of-the-robot/mathematically.mp4

# Manual Matematically 

1. Copy the program from the .py file and paste it in your compiler (I used VS Code).
 
  manual code link : https://github.com/Akshaybhawarkiti/Assignment/blob/forward-kinematics-of-the-robot/manual%20Mathematically.py

3. Download all dependencies mentioned above.
4. Run the program —  3D window will pop up with sliders form 0 to 180 range.
5. Adjust the sliders in window to move the robot and watch the coordinates update live.

