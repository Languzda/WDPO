import cv2 as cv2


def cameraLive():

    # camera = cv2.VideoCapture() # open default camera
    camera = cv2.imread("doge.png", cv2.IMREAD_COLOR) # open default camera

    print(camera)
    key = ord('a')

    while key != ord('q'):
        # ret, frame = camera.read() # capture frame by frame
        frame = camera
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # blur the image
        img_filtered = cv2.GaussianBlur(img_gray, (7, 7), 1.5)
        # detect edges on blurred img
        img_edges = cv2.Canny(img_filtered, 0, 30, 3)

        cv2.imshow('Rezultat', img_edges)
        key = cv2.waitKey(30)

    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    cameraLive();