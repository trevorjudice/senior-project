#!/usr/bin/env python

"""Returns pixel values of screen mirror"""

__author__      = "Trevor Judice"

import pyscreeze

def GrabScreen():	
	return pyscreeze.screenshot(region=(0,250, 700, 700))


if __name__ == '__main__':
  screenCap()
