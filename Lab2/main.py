import cv2
import numpy as np


def empty_callback(value):
    print(f'Trackbar reporting for duty with value: {value}')
    pass


dogeImg = cv2.imread("doge.jpg", cv2.IMREAD_COLOR)
dogeGrey = cv2.cvtColor(dogeImg, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Display normal doge', dogeGrey)

ret, thresh1 = cv2.threshold(dogeGrey, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Doge', thresh1)

# create a black image, a window
img = np.zeros((300, 512, 3), dtype=np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R', 'image', 0, 255, empty_callback)
cv2.createTrackbar('G', 'image', 0, 255, empty_callback)
cv2.createTrackbar('B', 'image', 0, 255, empty_callback)

# create trackbar for treshhold change
cv2.createTrackbar('Treshold', 'Doge', 0, 255, empty_callback)
cv2.createTrackbar('Typ', 'Doge', 0, 4, empty_callback)

# create switch for ON/OFF functionality
switch_trackbar_name = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch_trackbar_name, 'image', 0, 1, empty_callback)

#Read cube image
QR = cv2.imread("qr.jpg", cv2.IMREAD_COLOR)
cv2.imshow("QR", QR)

#Scale cube image
scaledCube = cv2.resize(QR, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Linear QR", scaledCube)
scaledCube = cv2.resize(QR, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_NEAREST)
cv2.imshow("Nearest QR", scaledCube)
scaledCube = cv2.resize(QR, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_AREA)
cv2.imshow("Area QR", scaledCube)
scaledCube = cv2.resize(QR, (0, 0), fx=2.75, fy=2.75, interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Lanczos4 QR", scaledCube)

Img1 = cv2.imread('img1.png', cv2.IMREAD_COLOR)
Img2 = cv2.imread('index.png', cv2.IMREAD_COLOR)

dst = cv2.addWeighted(Img1, 0.3, Img2, 0.7, 0)
cv2.imshow('dst', dst)

while True:
    cv2.imshow('image', img)
    cv2.imshow('Doge', thresh1)
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
    thresh = cv2.getTrackbarPos('Treshold', 'Doge')
    typ_interpolacji = cv2.getTrackbarPos('Typ', 'Doge')

    if s == 0:
        # assign zeros to all pixels
        img[:] = 0
    else:
        # assign the same BGR color to all pixels
        img[:] = [b, g, r]

    if typ_interpolacji == 0 :
        ret, thresh1 = cv2.threshold(dogeGrey, thresh, 255, cv2.THRESH_BINARY)
    elif typ_interpolacji == 1 :
        ret, thresh1 = cv2.threshold(dogeGrey, thresh, 255, cv2.THRESH_BINARY_INV)
    elif typ_interpolacji == 2 :
        ret, thresh1 = cv2.threshold(dogeGrey, thresh, 255, cv2.THRESH_TRUNC)
    elif typ_interpolacji == 3 :
        ret, thresh1 = cv2.threshold(dogeGrey, thresh, 255, cv2.THRESH_TOZERO)
    elif typ_interpolacji == 4 :
        ret, thresh1 = cv2.threshold(dogeGrey, thresh, 255, cv2.THRESH_TOZERO_INV)


# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()


if __name__ == '__main__':
    pass