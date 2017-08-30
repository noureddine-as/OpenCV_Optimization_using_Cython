import cv2

import cython


def threshold_slow(T, image):
    # grab the image dimensions
    h = image.shape[0]
    w = image.shape[1]

    # loop over the image, pixel by pixel
    for y in range(0, h):
        for x in range(0, w):
            # threshold the pixel
            image[y, x] = 255 if image[y, x] >= T else 0

    # return the thresholded image
    return image


f = cv2.getTickFrequency() / 1000
t1 = cv2.getTickCount()

image = cv2.imread("example.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_slow(5, image)

t2 = cv2.getTickCount()
print("Spent %f ms in execution." % ((t2 - t1) / f))

cv2.imshow("SLOW PYTHON", image)
cv2.waitKey()
cv2.destroyAllWindows()

