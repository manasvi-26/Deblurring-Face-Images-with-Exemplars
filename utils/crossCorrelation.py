import os
import sys
import cv2
from utils.utility_functions import *
import numpy as np

def translation(image, valx, valy):
    T = np.float32([[1, 0, valx], [0, 1, valy]])
    img_translation = cv2.warpAffine(image, T, (image.shape[1], image.shape[0]))
    return img_translation

def get_cross_correlation(blurred_image, template_image):
    
    template_image = cv2.resize(template_image, (blurred_image.shape[1] , blurred_image.shape[0]))
    
    blurred_gradient = Prewitt(blurred_image)
    
    translations = [(0,0) , (15,0) , (-15,0) , (0,15) , (0,-15)]

    result = 0
    
    for trans in translations:
        
        translated_image = translation(template_image , trans[0], trans[1])
        template_gradient = Prewitt(translated_image)
        result = max(result,cv2.matchTemplate(blurred_gradient,template_gradient,cv2.TM_CCORR_NORMED))

    return result
