#!/usr/bin/env python

"""Returns true if image has question, false if otherwise"""

__author__      = "Trevor Judice"

import pytesseract

import numpy as np
import cv2

from PIL import Image

def QuestionOCR(img):

	im_gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
	return pytesseract.image_to_string(Image.fromarray(im_gray))

if __name__ == "__main__":
	QuestionOCR(Sys.argv[0])