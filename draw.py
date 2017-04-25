#This program tries to draw a star shape using 2d-2-link planar robot
#(similar to SCARA)

import numpy as np
import move as mv
import jacobian as jb
import plot as plt


#these are the list of the points which form the shape of a "star"
#we have repeated the 1st point in the end of the list to form a complete loop

def draw(links, pts):

    ctraj_list = np.array([[]], dtype = float)

    for i in range(len(pts)-1):
        
        print('pt',pts[i],'-->','pt',pts[i+1])
        
        #obtain joint angles (config) for the start and end points
        q_strt= mv.ikine(links, pts[i])
        q_end= mv.ikine(links, pts[i+1])
        if q_strt == None or q_end == None:
            exit(0)
        #obtain the list of joint angles (trajectory) needed to
        #get a straight line path from start to end point
        qtraj = jb.motion(links, q_strt, q_end, pts[i], pts[i+1])

        #obtain cartesian co-ordinates for the correspoinding joint angles
        #which can be plotted on a graph to undestand visually
        if pts[i+1][0] > pts[i][0] or (pts[i+1][1] - pts[i][1]) > 0.5:
            skip_pt = np.array([pts[i], pts[i+1]])
            if ctraj_list.shape == (1,0):
                ctraj_list = skip_pt
            else:
                ctraj_list = np.vstack((ctraj_list, skip_pt))
            continue
        ctraj = mv.fkine(links, qtraj)      

        #stores the list of co-ordinates, which form the path b/w all pairs of the points
        if ctraj_list.shape == (1,0):
            ctraj_list = ctraj[0,:]
            ctraj_list = np.vstack((ctraj_list, ctraj[1:len(ctraj),:]))
        else:
            ctraj_list = np.vstack((ctraj_list, ctraj))

    #plots all the co-ordinates obtained from the trajectory
    plt.plot(ctraj_list)
