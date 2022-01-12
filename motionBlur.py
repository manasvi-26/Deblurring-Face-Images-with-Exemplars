import cv2
import numpy as np
from scipy.signal import convolve2d


images = ['./final/input1.png', './final/input2.png', './final/input3.png', './final/input4.png']

def streak_kernel(shape):
    # Example kernel simulating horizontal motion blur
    ny, nx = shape
    k = np.zeros(shape)
    k[ny//2-1, :] = 0.5
    k[ny//2+0, :] = 1.
    k[ny//2+1, :] = 0.5
    k[:, 0] *= 0.
    k[:, 1] *= 0.5
    k[:, -2] *= 0.5
    k[:, -1] *= 0.
    k /= np.sum(k)
    return k

k = streak_kernel((31,31))
count = 1


for file in images:

    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    y =  convolve2d(img, k, mode='same', boundary='wrap')
    path = './final/final' + str(count) + '.jpg'
    cv2.imwrite(path, y)

# y =  convolve2d(img, k, mode='same', boundary='wrap')
# path = 'final' + str(count) + '.jpg'
# cv2.imwrite(path, y)
# count += 1

# image = "adcd.png"


