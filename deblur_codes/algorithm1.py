import numpy as np
from numpy.fft import fft2, ifft2
from scipy.signal import convolve2d

from utils.utility_functions import *

# function to calculate latent image I given blur image and blur kernel
def algorithm1(y, k, lam, beta=1, beta_rate=2*np.sqrt(2), beta_max=256):
    
    y = np.array(y)
    k = np.array(k)

    k = pad_to_odd(k)
    k = k / np.sum(k)  # kernel should be normalized

    alpha = 2/3  
    n1, d1, d2 = precompute_fft_terms(y, k) #precompute fourier terms
    xr = y

    # while loop till beta reaches max value
    while beta < beta_max:
        # get circular difference
        v1 = circ_diff_1(xr)
        v2 = circ_diff_2(xr)

        #compute w
        w1 = get_w(v1, beta)
        w2 = get_w(v2, beta)

        #get latent image using fourier formula
        xr = get_I(n1, d1, d2, w1, w2, lam, beta)

        #adjust for even sized
        xr = np.roll(xr, (k.shape[0]//2-1, k.shape[1]//2-1), axis=(0, 1))

        beta *= beta_rate
    
    return xr

# function to precompute some fourier transform terms
def precompute_fft_terms(y, k) -> tuple:
    kp = pad_to_shape(k, y.shape)
    FK = fft2(kp)
    n1 = np.conj(FK) * fft2(y)
    d1 = np.abs(FK)**2
    FF1 = fft2(pad_to_shape([[1, -1]], y.shape))
    FF2 = fft2(pad_to_shape([[1], [-1]], y.shape))
    d2 = np.abs(FF1)**2 + np.abs(FF2)**2
    return (n1, d1, d2)


#function to apply the fourier formula to get latent image
def get_I(n1, d1, d2, w1, w2, lam, beta):
    
    gamma = beta / lam
    denom = d1 + gamma * d2
    w11 = -circ_diff_1(w1)
    w22 = -circ_diff_2(w2)
    nomin2 = w11 + w22
    nomin = n1 + gamma * fft2(nomin2)
    xr = np.real(ifft2(nomin / denom))
    return xr


# lookup table implementation to get w
def get_w(v, beta):
    
    eps = 1e-6
    m = 8/(27*beta**3)
    t1 = -9/8*v**2
    t2 = v**3/4
    t3 = -1/8*m*v**2
    t4 = -t3/2 + np.sqrt(0j - m**3/27 + (m*v**2)**2/256)
    t5 = np.power(t4, 1/3)
    t6 = 2*(-5/18*t1 + t5 + m/(3*t5))
    t7 = np.sqrt(t1/3 + t6)
    r1 = 3*v/4 + np.sqrt(t7 + np.sqrt(0j-(t1+t6+t2/t7)))/2
    r2 = 3*v/4 + np.sqrt(t7 - np.sqrt(0j-(t1+t6+t2/t7)))/2
    r3 = 3*v/4 + np.sqrt(-t7 + np.sqrt(0j-(t1+t6-t2/t7)))/2
    r4 = 3*v/4 + np.sqrt(-t7 - np.sqrt(0j-(t1+t6-t2/t7)))/2
    r = [r1, r2, r3, r4]
    c1 = np.abs(np.imag(r)) < eps
    c2 = np.real(r)*np.sign(v) > np.abs(v)/2
    c3 = np.real(r)*np.sign(v) < np.abs(v)
    wstar = np.max((c1 & c2 & c3) * np.real(r)*np.sign(v), axis=0)*np.sign(v)
    return wstar






