import numpy as np

def dh_parameter(theta,a,alpha,d):
    #DH Parameter for 6 dof 
    dh_parameter=np.array([[np.cos(theta), -np.sin(theta) * np.cos(alpha), np.sin(theta) * np.sin(alpha), a * np.cos(theta)],
        [np.sin(theta), np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), a * np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]])
num_joints=6 #Number of joints of robot
links=num_joints #number of joints=number of links

dh_list=[]
#Getting input of Joint angle,Offset,Twist angle, Displacement
for i in range(num_joints):
    theta=float(input(f"Enter the theta {i} :")) #Joint angle
    a=float(input(f"Enter the displacement 'a' {i} :")) #prismatic displacement
    d=float(input(f"Enter the offset {i} :")) #Offset
    alpha=float(input(f"Enter the twist angles{i} :"))
#DH PARAMETER
    dh=dh_parameter(theta, a, alpha, d)
dh_list.append(dh)

Transform=np.eye(4) #Assigning transformation matrix
#TRANSFORMATION MATRIX
Transformation_matrix=np.dot(Transform,dh_list)
#DISPLAYING DH PARAMETER
for i,dh in enumerate(dh_list):
    print(dh)
    print("Overall Transformation matrix :")
    print(Transformation_matrix)