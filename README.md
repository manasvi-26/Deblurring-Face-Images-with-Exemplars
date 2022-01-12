# Deblurring Face Images using Exemplars

### Team Name - Newt

### Team Members -

Laksh Nanwani 

Manasvi Vaidyula 

Mehul Mathur

Pooja Desur 

This repository contains all the code for our implementation of the paper [Deblurring Face Images using Exemplars](https://faculty.ucmerced.edu/mhyang/papers/eccv14_deblur.pdf).

## Overview

The paper uses an Exemplar-based approach for kernel estimation and deblurring of a blurred image.

1) Exemplar Matching for the blurred image using cross-correlation

![Untitled](Deblurring%20Face%20Images%20using%20Exemplars%20e6dd073f645645dc8b4d34606664997b/Untitled.png)

2) Salient edges extraction using mask created from salient facial landmarks and exemplar edges

![Untitled](Deblurring%20Face%20Images%20using%20Exemplars%20e6dd073f645645dc8b4d34606664997b/Untitled%201.png)

![Screenshot (265).png](Deblurring%20Face%20Images%20using%20Exemplars%20e6dd073f645645dc8b4d34606664997b/Screenshot_(265).png)

3) Kernel estimation using the obtained exemplar structure using the algorithms given in the paper, one of which involves minimizing a kernel cost function using gradient descent

4) Deconvolution of the deblurred image using the estimated kernel

5) Output analysis using SNR (signal to noise ratio)

## Repository Structure

![Untitled](Deblurring%20Face%20Images%20using%20Exemplars%20e6dd073f645645dc8b4d34606664997b/Untitled%202.png)

## Dependencies

- [Numpy](https://numpy.org/install/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [DLib](https://pypi.org/project/dlib/)
- [ImUtils](https://pypi.org/project/imutils/)
- [Scipy](https://scipy.org/install/)

`pip install numpy opencv-python dlib imutils scipy`

## Running the code

In order to deblur images, our code can be run from the command line.

### Command-line

`python3 main.py <path_to_blurred_image>` 

`python3 main.py <path_to_blurred_image> <path_to_original_image>` (for analysis)

blur_horizontal.jpg is given as a blurred image for convenience.
While running the code a folder 'outputs' will be created which contains the best exemplar chosen, mask formed, salient edges, images of intermediate steps in order to see the gradual improvement and finally the deblurred image.

To view examples of the input, intermediate steps, and respective outputs, we have build a GUI using React, which can be run by - 

### GUI

- Go to the folder *dashboard*

```markdown
# to install the node_modules folder
*npm install 
# running at localhost:3000
npm start*
```

## Dataset

- Used in Paper - http://www.cs.cmu.edu/afs/cs/project/PIE/MultiPie/Multi-Pie/Home.html
    - CIE Dataset
        - 2435 images
        - Faces with different expressions and orientations
        - Issue: paid
- Datasets Tried
    - Multi PIE - http://www.cs.cmu.edu/afs/cs/project/PIE/MultiPie/Multi-Pie/Home.html
        - issue : paid
    - CVL - http://lrv.fri.uni-lj.si/facedb.html
        - Issue: paid
    - http://robotics.csie.ncku.edu.tw/Databases/FaceDetect_PoseEstimate.htm
        - Issue: no expressions
        - Issue: Only 90 images
- **Dataset Used**
    - Extracted 2000 images - [https://drive.google.com/drive/folders/1acmtZQFaZP2D-l3ESXVikd13sIzCJpfa?usp=sharing](https://drive.google.com/drive/folders/1acmtZQFaZP2D-l3ESXVikd13sIzCJpfa?usp=sharing)
    - size of each image - 1024x1024
    - Different expressions - happy, angry, disgust, fear, neutral, sad, surprise
    - Various orientations
    - In order to run the code, create a directory called exemplar_dataset and move the dataset into this directory
    
    ```markdown
    mkdir exemplar_dataset
    mv <path to exemplar images> exemplar_dataset
    ```
    

## Conclusion and Result Evaluation

Our results

![Untitled](Deblurring%20Face%20Images%20using%20Exemplars%20e6dd073f645645dc8b4d34606664997b/Untitled%203.png)

In order to evaluate our results, we compared the SNR ratio between the original, blurred and original, deblurred and found the latter to have a higher value hence showing it has improved from the blurred image.

![Untitled](Deblurring%20Face%20Images%20using%20Exemplars%20e6dd073f645645dc8b4d34606664997b/Untitled%204.png)
