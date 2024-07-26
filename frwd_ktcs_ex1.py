#Forward kinematics using homogeneous transformation matrix
#arm has 2 links also with fixed base - 3 joints

import numpy as np
import math
from numpy import cos,sin

#homogeneous transformation 

theta1 = float(input("Enter the Theta1 :"))
theta2 = float(input("Enter the theta 2 :"))
theta3 = float(input("Enter the theta 3 : "))
theta1 = np.deg2rad(theta1)
theta2 = np.deg2rad(theta2)
theta3 = np.deg2rad(theta3)
#along x-axis
d1 = float(input("Entet the displacement 1:"))
d2 = float(input("Enter the displacement 2 :"))
d3 = float(input("Enter the displacement 3 :"))

H1 = np.array([[cos(theta1),-sin(theta1),d1],
               [sin(theta1),cos(theta1),0],
               [0,0,1]])
H2 = np.array([[cos(theta2),-sin(theta2),d2],
               [sin(theta2),cos(theta2),0],
               [0,0,1]])
H3 = np.array([[cos(theta3),-sin(theta3),d3],
               [sin(theta3),cos(theta3),0],
               [0,0,1]])
print(H1)
print(H2)
print(H3)
H = H1*H2*H3
print(H)

