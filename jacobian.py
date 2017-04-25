import math as mt
import numpy as np


def jacobian(links, q):
    # jacobian() calculates the "Jacobian matrix" for the given joint angles

    q1 = mt.radians(q[0, 0])
    q2 = mt.radians(q[0, 1])

    a1 = links[0, 0].astype(float)
    a2 = links[1, 0].astype(float)

    J = np.array([[a2 * mt.cos(q1 + q2), a2 * mt.sin(q1 + q2)],
                  [-a1 * mt.cos(q1) - a2 * mt.cos(q1 + q2),  -a1 *
                   mt.sin(q1) - a2 * mt.sin(q1 + q2)]
                  ])
    K = 1 / (a1 * a2 * mt.sin(q2))
    J = J * K

    return J


def motion(links, q_strt, q_end, c_strt, c_end):
    # motion() takes in the current and desired joint angles and returns the set of joint angles
    # required to achieve a straight cartesian path b/w the two points

    # max no.of iterations to find the desired joint angles
    # if this value is changed, then need to change the same inside the below while loop
    niter = 500

    # time interval (deg/sec)
    t_del = np.array([[1]])

    # acceptable error limit
    error = np.array([[1, 1]])

    # linear velocity (x_dot, y_dot)
    vel = c_end - c_strt

    # transpose of the above vel vector
    # need to change to more generic stmt
    vel = np.array([[vel[0]], [vel[1]]])

    # stores the set of all joint angles, b/w current and desired joint angles
    traj = np.array([[]], dtype=float)

    q_curr = q_strt

    while True:

        J = jacobian(links, q_curr)
        q_dot = J.dot(vel)
        q_curr = q_curr + np.transpose(q_dot)  # np.transpose(np.multiply(q_dot, t_del))

        if niter == 500:
            traj = np.hstack((traj, q_curr))
        else:
            traj = np.vstack((traj, q_curr))

        # gets out of the loop if the current joint angle approaches the desired joint angles
        #print(q_curr, q_end)
        if sum(sum((abs(q_curr - q_end) < error).astype(int))) == 2 or niter <= 0:
            break

        niter = niter - 1

    return traj


# Documentaion and notes for this module:
# links = np.array([[5], [5]], dtype=float)
# q_strt = np.array([[26.0, 80.0]])
# q_end = np.array([[-35.0, 114.0]])
# c_strt = np.array([5.0, 2.0])
# c_end = np.array([3.0, 7.0])
#
# print(motion(links, q_strt, q_end, c_strt, c_end))
