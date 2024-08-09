#Forward kinematics ex : 2
#ref : frwd_kinematics_ex.png 
#RRP robot , determine the location of the moving reference frame by writing the forward kinematics
#state the values of x,y,and theta of the moving reference frame relative to the fixed reference frame. 
import numpy as np
from numpy import sin,cos,tan
import math

theta=[]
for t in range(1,5):
    t = float(input(f"Enter the theta {t}:"))
    theta.append(t)
theta = np.deg2rad(theta)
theta = np.array(theta)

#along x-axis
dx = []
for d in range(1,5):
    d = float(input(f"Enter the displacement along x-axis {d} :"))
    dx.append(d)
dx = np.array(dx)
#along y-axis
dy = []
for d in range(1,5):
    d = float(input(f"Enter the displacement along y-axis {d} :"))
    dy.append(d)
dx = np.array(dy)
#Homogeneous Transformation matrix
H1 = np.array([[cos(theta[0]),-sin(theta[0]),dx[0]],
              [sin(theta[0]),cos(theta[0]),dy[0]],
               [0,0,1]])
H2 = np.array([[cos(theta[1]),-sin(theta[1]),dx[1]],
               [sin(theta[1]),cos(theta[1]),dy[1]],
               [0,0,1]])
H3 = np.array([[cos(theta[2]),-sin(theta[2]),dx[2]],
               [sin(theta[2]),cos(theta[2]),dy[2]],
               [0,0,1]])
H4 = np.array([[cos(theta[3]),-sin(theta[3]),dx[3]],
               [sin(theta[3]),cos(theta[3]),dy[3]],
               [0,0,1]])
H = H1*H2*H3*H4
print("H : \n", H)
print("X :", H[0,2])
print("Y :", H[1,2])
tantheta = H[0,0]/H[1,0]
theta_ = math.atan(tantheta)
theta_=np.rad2deg(theta_)
print("Theta :",theta_)
