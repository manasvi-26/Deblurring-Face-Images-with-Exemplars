import os 
from utils.crossCorrelation import *
import numpy as np
import cv2
from tqdm import tqdm

def get_best_exemplar(image, exemplar_directory):

    exemplar_files = [str(exemplar_directory) + "/" + ele for ele in list(os.listdir(exemplar_directory))]
    
    best_result = 0
    best_exemplar = np.zeros(shape=(500,500))
    
    print("Finding Best Exemplar Image")
    
    for file_path in tqdm(exemplar_files[:200]):
        exemplar = cv2.imread(file_path)
        gray_exemplar = cv2.cvtColor(exemplar, cv2.COLOR_RGB2GRAY)
        
        curr_result = get_cross_correlation(image, gray_exemplar)
        

        if (curr_result > best_result):
            best_result = curr_result
            best_exemplar = exemplar
            
        
    return best_exemplar

    