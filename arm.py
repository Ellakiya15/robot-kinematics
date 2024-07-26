import numpy as np
from numpy import sin,cos
import math

l1 = int(input("Enter the link 1 length :"))
l2 = int(input("Enter the link 2 length :"))
pi = math.pi

#r = math.sqrt((l1*l1)+(l2*l2)-2*l1*l2*cos(alpha))
r = math.sqrt((l1*l1)+(l2*l2))
print("r :",r)
L1 = l1*l1
L2 = l2*l2
R = r*r
alpha = math.acos((R-L2-L1)/(-2*l1*l2))
print("Alpha :",alpha)
Theta2 = pi - alpha
print("Theta 2 :",Theta2)
