import cv2
import numpy as np
cap = cv2.VideoCapture(0)
xer = 0
pts = []
while (1):

    # Take each frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 255, 0])
    upper_red = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(mask)
    #print(minVal, maxVal, minLoc, maxLoc)

    #if maxLoc != (0,0):
        #cv2.circle(frame, maxLoc, 20, (0, 0, 255), 2, cv2.LINE_AA)
        #cv2.imwrite("fond_tir.png",frame)


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gauss = cv2.GaussianBlur(gray, (5, 5), 0)

    canny = cv2.Canny(gauss, 50, 210)

    cont = canny.copy()

    contr, hier = cv2.findContours(cont, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    i = 0
    truc = 0
    for cnt in contr:

        area = cv2.contourArea(cnt)
        # print(area)

        peri = cv2.arcLength(cnt, True)
        # print(peri)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        objcor = len(approx)
        # print(len(approx))
        x, y, w, h = cv2.boundingRect(approx)
        # print(x, w)
        # print(y, h)
        ratio = w / float(h)

        font = cv2.FONT_HERSHEY_SIMPLEX

        org = (x, y)

        fontScale = 1

        color = (255, 0, 0)

        thickness = 2

        """image = cv2.putText(img, str(i), org, font,
                            fontScale, color, thickness, cv2.LINE_AA)"""

        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if len(approx) == 8 and area > 1000:
            truc += 1
            cv2.putText(frame, str(truc), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
            #print(x, w, y, h, area, len(approx))
            if x < maxLoc[0] < x + w and y < maxLoc[1] < y + h:
                if truc == 1:
                    print("j'aime les pates", xer)
                else :
                    print("j'aime les loukoum", xer)

                xer += 1


            cv2.drawContours(frame, cnt, -1, (0, 0, 255), 3)
    cv2.imshow('Track Laser', frame)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()