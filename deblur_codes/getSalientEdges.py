from utils.featureDetection import *
from utils.utility_functions import *

'''
Create the Mask for the best exemplar,
Get the Salient Edges for this Mask
'''
def get_salient_edges(image):

    mask = feature_Detection(image)
    gradient_image = Prewitt(image,mode="same")

    final_image = np.zeros(image.shape)
    
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            if mask[row][col] != 0:
                final_image[row][col] = gradient_image[row][col]

    return mask, final_image