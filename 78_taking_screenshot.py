
import pyautogui
import numpy as np
import cv2 as cv

image = pyautogui.screenshot()

image.save('my_screenshot.png')

image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)

cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()