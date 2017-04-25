import numpy as np
import math as mt

def ikine(links, pt):
    #ikine refers to inverse kinematics. ikine() calculates the joint angles needed for the 2D-planar robot to
    #move to the given cartesian co-ordinate. The joint angles range from [-180 to 180]
    
    a1 = links[0,0].astype(float)
    a2 = links[1,0].astype(float) 
    x = pt[0]
    y = pt[1]

    #distance b/w the pt and origin
    dist = mt.sqrt(pow(x,2) + pow(y,2))

    #if the distance is greater than entire link length then pt cannot be reached
    if dist > (a1+a2) :
        print(pt, 'is unreachable by robot')
        return None

    #q1, q2 are the required joint angles. cq2 -> cos(q2) & sq2 -> sin(q2)
    cq2 = float( (pow(x, 2) + pow(y, 2)) - (pow(a1, 2) + pow(a2, 2)) )/(2*a1*a2)
    sq2 = mt.sqrt(1-mt.pow(cq2,2))
    q2 = mt.acos(cq2)

    alpha = np.arctan2(y,x)
    beta = np.arctan2((a2 * sq2),(a1 + (a2 * cq2)))

    #A 2D-planar robot has 2DOF (x, y). Hence it can move to the required pt using 2 diff.
    #configurations. This depends upon q2 being +/- . In this code we've calculated only +ve config.
    #Although you can see the -ve config formula being commented out
    
    q1_pos = alpha - beta
    q2_pos = q2
    ## q1_neg = alpha + beta
    ## q2_neg = -q2

    q1_pos = mt.degrees(q1_pos)
    q2_pos = mt.degrees(q2_pos)
    ## q1_neg = mt.degrees(q1_neg)
    ## q2_neg = mt.degrees(q2_neg)

    joint_angles = np.array([[q1_pos, q2_pos]])

    return joint_angles

def fkine(links, q_list):
    #fkine refers to forward kinematics. fkine() calculates the EE position of the 2D-planar robot, given 
    #its joint angles. It takes a list of joint angles and returns the respective cartesian co-ordinates.
    
    a1 = links[0,0].astype(float)
    a2 = links[1,0].astype(float)

    niter = len(q_list)
    ctraj = np.array([[]], dtype = int)
    i = 0
    
    while i < niter:
        
        q1 = mt.radians(q_list[i,0])
        q2 = mt.radians(q_list[i,1])
        
        tmp = np.array([[mt.cos(q1)*a1 + a2*mt.cos(q2+q1),
                mt.sin(q1)*a1 + a2*mt.sin(q2+q1)]
               ])
        
        if i == 0:
            ctraj = np.hstack((ctraj, tmp))
        else:
            ctraj = np.vstack((ctraj, tmp))
        i = i + 1

    return ctraj


#Debugging code and notes for this module:
#links = np.array([[9], [9]], dtype = float)
#pos = np.array([[-29.927, 151.521]], dtype = float)
##
#print(fkine(pos))
# Note: if floating numbers are not used then there is an considerable
# error in the result, hence pass the arguments in floats
# p1: 9, 0 p2: 6,-3
# need -180:180 (i.e 360 servos) or motors
