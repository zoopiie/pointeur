import cv2
from time import sleep



img = cv2.imread("image_test_apres.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gauss = cv2.GaussianBlur(gray, (5, 5), 0)

canny = cv2.Canny(gauss, 50, 210)

cont = canny.copy()

contr, hier = cv2.findContours(cont, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
i = 0
for cnt in contr:
    area = cv2.contourArea(cnt)
    # print(area)

    peri = cv2.arcLength(cnt, True)
    #print(peri)
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
    objcor = len(approx)
    print(len(approx))
    x, y, w, h = cv2.boundingRect(approx)
    print(x, w)
    print(y, h)
    ratio = w / float(h)

    font = cv2.FONT_HERSHEY_SIMPLEX

    org = (x, y)

    fontScale = 1

    color = (255, 0, 0)

    thickness = 2

    image = cv2.putText(img, str(i), org, font,
                        fontScale, color, thickness, cv2.LINE_AA)

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.drawContours(img, cnt, -1, (0, 0, 255), 1)

    cv2.imwrite("contour.png", img)

