#Write down the Translational matrix of a link first rotating about the absolute X-axis, then 
#rotating about the body frame z-axis, then rotating about the absolute z-axis and finally 
#translating 7 and 6 units along the x and y-axis respectively. If the initial position of a point on 
#the link is (2,0,3), what will be the new position of that point after the above operations
import numpy as np
# Define the initial point in homogeneous coordinates
P_initial = np.array([2, 0, 3, 1])

# Define the translation matrix (7 units along x, 6 units along y)
T_xy = np.array([
    [1, 0, 0, 7],
    [0, 1, 0, 6],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# Assuming the rotation angles are all zero for simplicity
# Rotation about the X-axis (absolute)
theta1 = 0
R_x = np.array([
    [1, 0, 0, 0],
    [0, np.cos(theta1), -np.sin(theta1), 0],
    [0, np.sin(theta1), np.cos(theta1), 0],
    [0, 0, 0, 1]
])

# Rotation about the z-axis (body frame)
theta2 = 0
R_z_body = np.array([
    [np.cos(theta2), -np.sin(theta2), 0, 0],
    [np.sin(theta2), np.cos(theta2), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# Rotation about the z-axis (absolute)
theta3 = 0
R_z_abs = np.array([
    [np.cos(theta3), -np.sin(theta3), 0, 0],
    [np.sin(theta3), np.cos(theta3), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# Combine all transformations
T_total = T_xy @ R_z_abs @ R_z_body @ R_x

# Calculate the new position
P_new = T_total @ P_initial

P_new[:3]  # Extracting the new coordinates (ignoring the homogeneous coordinate)
