import numpy as np
from utils.utility_functions import *
from deblur_codes.algorithm1 import *
from tqdm import tqdm

# function to crop out borders of  an image
def crop_image(a, shape):
    
    val = (a.shape[0] - shape[0]) // 2
    cropped_image = a[val:a.shape[0] - val, val:a.shape[1] - val]

    return cropped_image
    
# function that runs conjugate gradient descent to obtain a blur kernel given salient edges and blurred image
def estimate_kernel(del_B, del_S, gamma = 1, lr = 0.1, epochs = 20, tol = 1e-10):
    
    print("Estimate kernels")
    k = np.ones((31,31))
    for i in tqdm(range(epochs)):
        
        val1 = convolve(del_S, flip_matrix(k))          # 1024 - 1024 - 31 + 1 = 994
        val2 = val1 - crop_image(del_B , val1.shape)    # 994 - 994
        val3 = convolve(del_S, val2)                    # 994 - 31

        del_k = 2 * (val3 + gamma*k)
        if (del_k < tol).all():
            break

        k = k - lr * del_k
        k = k/np.sum(k)
        
    return k

# the main algorithm that runs all other sub parts
# estimates blur kernel k and outputs the final deblurred size changed - output
def algorithm2(blur_image, delta_S, n_iters):
    I = np.zeros(shape=(500,500))
    print("Iterations")
    for l in range(n_iters):
        delta_B = Prewitt(blur_image,mode="valid")
        blur_kernel = estimate_kernel(delta_B, delta_S , epochs=100)
        blur_kernel = format_kernel(blur_kernel , (31,31) , l , n_iters)
        I = algorithm1(blur_image,blur_kernel,lam=1e6)
        cv2.imwrite('./outputs/intermediate_latent_image' + str(l) + '.png', I)  
        delta_S = Prewitt(I,mode="same")

    return blur_kernel, I
