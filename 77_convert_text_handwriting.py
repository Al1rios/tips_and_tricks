
import pywhatkit
import cv2 as cv

text = 'Python is great'

pywhatkit.text_to_handwriting(text, save_to='new_text.png')

hand_text = cv.imread('new_text.png')
cv.imshow('hand_text', hand_text)
cv.waitKey(0)
cv.destroyAllWindows()

