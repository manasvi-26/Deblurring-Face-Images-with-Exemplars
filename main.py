import os
import sys
import cv2
from deblur_codes.getBestExemplar import *
from deblur_codes.getSalientEdges import *
from deblur_codes.algorithm2 import *
from deblur_codes.algorithm1 import *
from utils.analysis import *


def saveOutputs(image, image_path):
    cv2.imwrite(image_path, image)    


if __name__ == "__main__":
 
    try:
        os.mkdir('outputs')
    except FileExistsError:
        pass

   
    image_path = sys.argv[1]
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    

    """ 
        Step 1: Get Best matching exemplar 
    """

    exemplar = get_best_exemplar(gray_image, "./exemplar_dataset")
    gray_exemplar = cv2.cvtColor(exemplar, cv2.COLOR_RGB2GRAY)
    saveOutputs(exemplar,"./outputs/Best_Exemplar.png")

    
    """ 
        Step 2: Get Salient edges of the best matched exemplar image
    """
    
    mask , salient_edges = get_salient_edges(gray_exemplar)
    print(salient_edges.shape)

    saveOutputs(mask,"./outputs/Mask.png")
    saveOutputs(salient_edges,"./outputs/Salient_Edges.png")

    """ 
        Step 3: Predict the best Blur kernel and get the best Image using a non blind deconvultion method
    """

    blur_kernel,I = algorithm2(gray_image , salient_edges , n_iters = 50)
    saveOutputs(I, "./outputs/Final_Image.png")


    """
        Step 4: Evaluate Results Using SNR Ratios and the distribution of the gradient before and after deblurring
    """ 
    
    try:
        og_image_path = sys.argv[2]
        og_image = cv2.imread(og_image_path)
        og_image = cv2.cvtColor(og_image, cv2.COLOR_BGR2RGB)
        gray_og_image = cv2.cvtColor(og_image, cv2.COLOR_RGB2GRAY)

        plot_results(gray_og_image, blur_kernel, gray_image, I)
        
    except:
        pass

    
