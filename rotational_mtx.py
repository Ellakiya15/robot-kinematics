import numpy as np
from numpy import sin,cos
t=int(input("Enter the Theta:"))
t = np.deg2rad(t)
Rx = np.array([[1,0,0],
               [0,cos(t),-sin(t)],
               [0,sin(t),cos(t)]])
Ry = np.array([[cos(t),0,sin(t)],
               [0,1,0],
               [-sin(t),0,cos(t)]])
Rz = np.array([[cos(t),-sin(t),0],
              [sin(t),cos(t),0],
              [0,0,1]])
Trans_rx = np.transpose(Rx)
Trans_ry = np.transpose(Ry)
Trans_rz = np.transpose(Rz)
print("Rotational matrix of x \n",Rx)
print("Transponse of Rotational matrix of x \n",Trans_rx)
print("Rotational matrix of y \n",Ry)
print("Transponse of Rotational matrix of y \n",Trans_ry)
print("Rotational matrix of z \n",Rz)
print("Transponse of Rotational matrix of z \n",Trans_rz)