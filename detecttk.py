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

f = open('data.txt', 'w+')
f.write((str(0)))
f.write("\n")
f.write(str(0))
f.close()

while (1):

    cap, imageFrame = webcam.read()

    #cv2.imwrite("init.png", imageFrame)

    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    red_lower = np.array([52, 0, 200], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)



    kernal = np.ones((5, 5), "uint8")

    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame,
                              mask=red_mask)


    contours, hierarchy = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    if varcolor == 1:
        cv2.imwrite("image_test_apres.png", imageFrame)

        #colorpixel.testcolor(x, y, w, h, "image_test_apres.png")
        if colorpixel.testwhite(x, y, w, h, "image_test_apres.png") == 0:

            f = open('data.txt', 'w+')
            f.write((str(int((x - 16)/613*1000))))
            f.write("\n")
            f.write(str((int((y - 81)/343*600))))
            f.close()
            print(str(int((x - 16)/613*1000)), str((int((y - 81)/343*600))))




    varcolor = 0
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (500 > area > 100):
            varcolor = 1
            x, y, w, h = cv2.boundingRect(contour)



            cv2.imwrite("image_test_avant.png", imageFrame)
            sleep(0.2)




    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break