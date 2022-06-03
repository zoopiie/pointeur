import numpy as np
import cv2
import colorpixel
import tabnb
import testtab
from time import sleep

varcolor = 0

var = 0
webcam = cv2.VideoCapture(0)
tabcerx = []
tabcery = []
tabcerw = []
tabcerh = []


while (1):

    cap, imageFrame = webcam.read()


    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    red_lower = np.array([52, 0, 200], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)



    kernal = np.ones((5, 5), "uint8")

    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, hsvFrame,
                              mask=red_mask)


    contours, hierarchy = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    """if varcolor == 1:
        cv2.imwrite("image_test_apres.png", imageFrame)

        #colorpixel.testcolor(x, y, w, h, "image_test_apres.png")
        colorpixel.testonepoint(x, y, w, h, "image_test_apres.png")"""


    #varcolor = 0
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (500 > area > 100):
            varcolor = 1
            x, y, w, h = cv2.boundingRect(contour)
            #imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)


            cv2.imwrite("image_test_avant.jpg", imageFrame)
            cv2.imwrite("image_test_avant1.jpg", imageFrame)
            cv2.imwrite("image_test_avant2.jpg", imageFrame)
            cv2.imwrite("image_test_avant4.jpg", imageFrame)
            """x = colorpixel.testuncolor(x, y, w, h, "image_test_avant.png")
            print(x)
            f = open('toucher.txt', 'w+')
            f.write(str(x))
            f.close()
            sleep(0.2)"""




    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break