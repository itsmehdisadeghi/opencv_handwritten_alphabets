import cv2
from random import randint
import numpy as np;

img = np.ones((350, 700, 3), dtype = np.uint8)
img = 255* img
inp = list(str(input()))
print(inp)

k = 25
j = 25
for i in inp:
    if i == "a":
        r = randint(14 , 63)
        print(r)
        u = "D:\\GITHUB\\bye_homework\\a\\{}.jpg".format(r)
        simg = cv2.imread(u)
        img[j : j+simg.shape[0] , k : k+simg.shape[1]] = simg
        k+=simg.shape[1] + 5
    if i == "b":
        r = randint(2 , 61)
        print(r)
        u = "D:\\GITHUB\\bye_homework\\b\\{}.jpg".format(r)
        simg = cv2.imread(u)
        img[j : j+simg.shape[0] , k : k+simg.shape[1]] = simg
        k+=simg.shape[1] + 5
    if i == " ":
        k+=25



cv2.imshow("k"  , img)
cv2.waitKey(0)



# x1 = 20
# x2 = 75

# y1 = 425
# y2 = 479

# i = 6

# j = 1
# while j <= 10:
#     croped_image = img[y1:y2 , x1:x2]
#     name = str(i) + " " + str(j) + ".jpg"
#     url = "D:\\GITHUB\\bye_homework\\b\\{}".format(name)
#     cv2.imwrite(url , croped_image)
#     x1 += 90
#     x2 += 90
#     j += 1

# contours , hierarchy = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
# for cnt in contours:
#     area = cv2.contourArea(cnt)
#     cv2.drawContours(img , cnt , -1 , (255 , 0 , 0) , 1)



# i = 14
# while i <= 63:
#     u = "D:\\GITHUB\\bye_homework\\a\\a_{}.jpg".format(i)
#     img = cv2.imread(u)
#     imgg = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
#     imeg = cv2.Canny(imgg , 50 , 50 )
#     contours , hierarchy = cv2.findContours(imeg , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area>5:
#             cv2.drawContours(imeg , cnt , -1 , (0,255,255) , 4)
#             per = cv2.arcLength(cnt , True)
#             approx = cv2.approxPolyDP(cnt , 0.02*per , True)
#             x1 , y1 , w , h = cv2.boundingRect(approx)
#             x2 = x1+w
#             y2 = y1+h
#             croped_image = img[y1:y2 , x1:x2]
#             name = str(i) + ".jpg"
#             url = "D:\\GITHUB\\bye_homework\\a\\{}".format(name)
#             cv2.imwrite(url , croped_image)
#     i += 1