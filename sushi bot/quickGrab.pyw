from PIL import ImageGrab
import os
import time

"""
Screen resolution of 1280x1024 using Chrome
"""

#x_pad = 155
#y_pad = 255
x_pad = 357
y_pad = 255

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+641, y_pad+479)
    im = ImageGrab.grab(box) # box
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()
