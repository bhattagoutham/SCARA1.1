from matplotlib import pyplot as plt
import numpy as np

def plot(ctraj):
    #gets list of all x-co-ordinates
    x_pt = ctraj[:,0]
    #gets list of all y-co-ordinates
    y_pt = ctraj[:,1]
    
    plt.plot(x_pt, y_pt, 'g.')   
    plt.show()
    
##Documentation and notes for this module:
##x = np.array(
##    [[1, 2],
##     [2, 4],
##     [5, 8]]);
####plt.plot([1,2,3], [4,5,6], 'bo')
####plt.plot([6,8,0], [4,5,6], 'go')
##x_pt = x[0:len(x),0]
##y_pt = x[0:len(x),1]
##plt.plot(x_pt, y_pt, 'bo')
##plt.axis([0,10,0,10])
#plt.axis([min(x)-k,max(x)+k,min(y)-k,max(y)+k])
##plt.show()
##print('x_pt: ',np.shape(x_pt))
##print('y_pt: ',np.shape(y_pt))
