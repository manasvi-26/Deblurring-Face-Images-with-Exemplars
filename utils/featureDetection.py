import numpy as np
import dlib
import cv2


def draw_lines(image, points, loop=False):

    end = len(points) - 1
    color = (255,255,255)
    thickness = 5

    for index in range(1,len(points)):
        start_point = tuple(points[index - 1])
        end_point = tuple(points[index])

        image = cv2.line(image, start_point, end_point, color, thickness)

    if loop == True:
        image = cv2.line(image, tuple(points[end]), tuple(points[0]), color, thickness)

    return image


def feature_Detection(image):

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("./utils/shape_predictor_68_face_landmarks.dat")

    face = detector(image)[0]
    landmarks = predictor(image, face)
    myPoints = []

    for n in range(68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        myPoints.append([x,y])


    final_image = np.zeros(image.shape)

    if len(myPoints) != 0:
        try:
            contour = myPoints[:17]
            left_eye = myPoints[36:42]
            right_eye = myPoints[42:48]
            lips = myPoints[48:61]
            
            final_image = draw_lines(final_image,contour)
            final_image = draw_lines(final_image,left_eye,loop=True)
            final_image = draw_lines(final_image,right_eye,loop=True)
            final_image = draw_lines(final_image,lips,loop=True)


        except:
            print("failed to detect features")
            pass

    return final_image