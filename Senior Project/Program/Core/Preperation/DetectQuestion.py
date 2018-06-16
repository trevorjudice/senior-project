#!/usr/bin/env python

"""Returns true if image has question, false if otherwise"""

__author__      = "Trevor Judice"

import cv2
import numpy as np

def DetectQuestion(img):

	im_gray = cv2.cvtColor(np.array(img),cv2.COLOR_BGR2GRAY)
	
	return np.sum(im_gray) > 100000000


if __name__ == "__main__":
	DetectQuestion(sys.argv[0]);



