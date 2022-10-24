import cv2
import numpy as np


def empty_callback(value):
    # print(f'Trackbar reporting for duty with value: {value}')
    pass


def thresholdChangeCallBack(value):
    ret, thresh1 = cv2.threshold(dogeGrey, value, 255, cv2.THRESH_BINARY)
    cv2.imshow('Display normal doge, after', thresh1)


def typeChange(value):
    switch(value):


dogeImg = cv2.imread("fiut.jpg", cv2.IMREAD_COLOR)
dogeGrey = cv2.cvtColor(dogeImg[300:1000][200:800], cv2.COLOR_BGR2GRAY)
cv2.imshow('Display normal doge', dogeGrey)

ret, thresh1 = cv2.threshold(dogeGrey, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Display normal doge, after', thresh1)

# create a black image, a window
img = np.zeros((300, 512, 3), dtype=np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R', 'image', 0, 255, empty_callback)
cv2.createTrackbar('G', 'image', 0, 255, empty_callback)
cv2.createTrackbar('B', 'image', 0, 255, empty_callback)

# create trackbar for treshhold change
cv2.createTrackbar('Granica Pajaca', 'image', 0, 255, thresholdChangeCallBack)
cv2.createTrackbar('Typ Pajaca', 'image', 0, 5, thresholdChangeCallBack)

# create switch for ON/OFF functionality
switch_trackbar_name = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch_trackbar_name, 'image', 0, 1, empty_callback)

while True:
    cv2.imshow('image', img)

    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch_trackbar_name, 'image')

    if s == 0:
        # assign zeros to all pixels
        img[:] = 0
    else:
        # assign the same BGR color to all pixels
        img[:] = [b, g, r]

# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()


if __name__ == '__main__':
    pass
