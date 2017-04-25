import numpy as np
import cv2
import imutils as imt
import draw as dw

im = cv2.imread('22.JPG', 0)
im = cv2.resize(im, None, fx=0.035, fy=0.035, interpolation=cv2.INTER_AREA)
im = cv2.GaussianBlur(im, (11, 11), 0)
im = cv2.Canny(im, 0, 50)


print(im.shape)
bool_pts = im == 255
height, width = bool_pts.shape

pts = np.array([[]], dtype=float)

for row in range(height):
    for col in range(width):
        if im[row, col]:
            tmp = np.array([[row, col]])
            if pts.shape == (1, 0):
                pts = np.hstack((pts, tmp))
            else:
                pts = np.vstack((pts, tmp))

links = np.array([[30], [30]], dtype=float)
pts = pts / 4
dw.draw(links, pts)
cv2.imshow('img', im)
if cv2.waitKey(0) & 0xFF == ord('q'):
    exit(0)
