import numpy as np
import draw as dw

pts = np.array([[3, 3],[8, 13],[13, 3],[3, 8],[13, 8],[3, 3]], dtype = float)
links = np.array([[9], [9]], dtype = float)
dw.draw(links, pts)
