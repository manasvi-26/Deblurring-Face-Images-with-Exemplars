import cv2
import numpy as np
import scipy
from scipy import signal



def flip_matrix(matrix):
    new_matrix = np.flip(matrix,1)
    new_matrix = np.flip(new_matrix,0)
    return new_matrix

def convolve(matrix_a, matrix_b , mode='valid'):
    return  signal.convolve2d(matrix_a,matrix_b,mode=mode)

def Prewitt(image, direction=None, mode='valid'):

    image = image.astype('float64')
    kernelx = np.array([[-1, 0, 1],
                        [-1, 0, 1],
                        [-1, 0, 1]])

    kernely = np.array([[1, 1, 1],
                        [0, 0, 0],
                        [-1,-1,-1]])

    grad_x = convolve(image,flip_matrix(kernelx),mode)
    grad_y = convolve(image,flip_matrix(kernely),mode)
    if (direction == 'x'): return grad_x
        
    if (direction == 'y'): return grad_y
    
    return np.sqrt((grad_x ** 2) + (grad_y ** 2)).astype("uint8")

def format_kernel(blur_k , shape , i , n):
    c = (1 - (i / (n-1)))
    ny, nx = shape
    blur_k = np.zeros(shape)
    blur_k[ny//2-1, :] = 0.5
    blur_k[ny//2+0, :] = 1.
    blur_k[ny//2+1, :] = 0.5
    blur_k[:, 0] *= 0.
    blur_k[:, 1] *= 0.5
    blur_k[:, -2] *= 0.5
    blur_k[:, -1] *= 0.
    blur_k /= np.sum(blur_k)
    blur_k += 0.01 * c
    return blur_k


def pad_to_shape(a, shape):
    a = np.array(a)
    b = np.zeros(shape)
    ny, nx = a.shape
    b[:ny, :nx] = a
    return b

def pad_to_odd(k):
    k_shape = list(k.shape)
    if k_shape[0] % 2 == 0:
        k_shape[0] += 1
    if k_shape[1] % 2 == 0:
        k_shape[1] += 1
    k = pad_to_shape(k, k_shape)
    return k


def circ_diff_1(a):
    return np.hstack([np.diff(a, axis=1), a[:, 0, np.newaxis] - a[:, -1, np.newaxis]])

def circ_diff_2(a):
    return np.vstack([np.diff(a, axis=0), a[0, :] - a[-1, :]])