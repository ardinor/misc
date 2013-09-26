from PIL import ImageGrab, ImageOps
from numpy import *
import os
import time
import win32api
import win32con

"""
Screen resolution of 1280x1024 using Chrome
http://www.miniclip.com/games/sushi-go-round/en/
"""

#x_pad = 155
#y_pad = 255
x_pad = 357
y_pad = 255

class Cord:
    #ingredients
    f_shrimp = (35, 332)
    f_rice = (91, 332)
    f_nori = (35, 389)
    f_roe = (91, 389)
    f_salmon = (35, 444)
    f_unagi = (91, 444)

    #phone menu
    phone = (556, 365)
    menu_toppings = (508, 275)
    menu_rice = (518, 296)
    menu_sake = (509, 317)
    t_shrimp = (495, 225)
    t_unagi = (577, 220)
    t_nori = (493, 278)
    t_roe = (575, 278)
    t_salmon = (495, 330)
    t_back = (559, 329)
    t_exit = (592, 333)
    rice_rice = (542, 280)
    rice_exit = (585, 336)
    sake_sake = (545, 279)
    sake_exit = (584, 336)
    deliver_normal = (491, 294)
    deliver_express = (577, 293)

class SeatOne:
    served = False
    empty = True
    
class SeatTwo:
    served = False
    empty = True

empty_seats = {(27, 59): 6524,
               (128, 59): 5922,
               (229, 59): 10917,
               (330, 59): 10660,
               (431, 59): 6844,
               (532, 59): 7991}

foodOnHand = {'shrimp': 5,
              'rice': 10,
              'nori': 10,
              'roe': 10,
              'salmon': 5,
              'unagi': 5,
              'sake': 2}

foodLocations = {'shrimp': Cord.f_shrimp,
                 'rice': Cord.f_rice,
                 'nori': Cord.f_nori,
                 'roe': Cord.f_roe,
                 'salmon': Cord.f_salmon,
                 'unagi': Cord.f_unagi}

foodTypes = {2853: 'caliroll',
             2387: 'gunkan',
             2380: 'onigiri',
             2184: 'salmonroll',
             2631: 'shrimpsushi',
             2603: 'unagiroll',
             3017: 'dragonroll'}

seat_one = (27, 59) #(26, 60)
seat_two = (128, 59) #(127, 60)
seat_three = (229, 59) #(228, 60)
seat_four = (330, 59) #(329, 60)
seat_five = (431, 59) #(430, 60)
seat_six = (532, 59) #(531, 60)

seats = [seat_one, seat_two, seat_three,
         seat_four, seat_five, seat_six]
    

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #print 'lclick'


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    #print 'left down'


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    #print 'left release'


def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

                   
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y


def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+641, y_pad+479)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def grab():
    box = (x_pad+1, y_pad+1, x_pad+641, y_pad+479)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print a
    return a

def arraySum(a, b):
    
    box = (x_pad+a[0], y_pad+a[1], x_pad+b[0], y_pad+b[1])
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    return a


def getSeat(seat, no):
    box = (x_pad+seat[0], y_pad+seat[1], x_pad+59+seat[0], y_pad+16+seat[1])
    im = ImageOps.grayscale(ImageGrab.grab(box))
    #im = ImageGrab.grab(box)
    a = array(im.getcolors())
    a = a.sum()
    #print a
    #im.save(os.getcwd() + '\\' + no + '_' + str(int(time.time())) + '.png', 'PNG')
    return a


def getAllSeats():

    t  = 1            
    for i in seats:        
        a = getSeat(i, str(t))
        print a
        t+=1


def startGame():
    #play game button
    mousePos((307, 206))
    leftClick()
    #iPhone app skip
    mousePos((328, 387))
    leftClick()
    #skip tutorial
    time.sleep(.1)  # this menu seems to take longer to load?
    mousePos((576, 451))
    leftClick()
    #continue
    mousePos((310, 378))
    leftClick()


def clearTables():
    """ empty plates
    81, 203
    182, 207
    283, 209
    383, 204
    483, 208
    577. 210
    """
     
    tables = [(81, 203), (182, 207), (283, 209),
              (383, 204), (483, 208), (577, 210)]

    for i in tables:
        mousePos(i)
        leftClick()
    time.sleep(0.1)


def foldMat():

    mousePos((Cord.f_rice[0]+45, Cord.f_rice[1]))
    leftClick()
    time.sleep(.1)


def makeFood(food):
    ingredients = []
    if food == 'caliroll':
        print 'Making a caliroll'
        #ingredients = [Cord.f_rice, Cord.f_nori, Cord.f_roe]
        ingredients = ['rice', 'nori', 'roe']

    elif food == 'onigiri':
        print 'Making onigiri'
        #ingredients = [Cord.f_rice, Cord.f_rice, Cord.f_nori]
        ingredients = ['rice', 'rice', 'nori']

    elif food == 'gunkan':
        print 'Making gunkan'
        #ingredients = [Cord.f_rice, Cord.f_nori, Cord.f_roe, Cord.f_roe]
        ingredients = ['rice', 'nori', 'roe', 'roe']

    elif food == 'salmonroll':
        print 'Making salmon roll'
        ingredients = ['rice', 'nori', 'salmon', 'salmon']

    elif food == 'shrimpsushi':
        print 'Making shrimp sushi'
        ingredients = ['rice', 'nori', 'shrimp', 'shrimp']

    elif food == 'unagiroll':
        print 'Making unagi roll'
        ingredients = ['rice', 'nori' ,'unagi', 'unagi']

    elif food == 'dragonroll':
        print 'Making a dragon roll'
        ingredients = ['rice', 'rice', 'nori', 'roe',
                       'unagi', 'unagi']

    if ingredients:
        while arraySum((127, 313), (280, 464)) != 24463:
            time.sleep(.1)
        for i in ingredients:
            foodOnHand[i] -= 1
            mousePos(foodLocations[i])
            leftClick()
            time.sleep(.5)
        foldMat()
        time.sleep(.5)


def buyFood(food):  
    
    if food == 'rice':
        menu_loc = Cord.menu_rice
        item_loc = Cord.rice_rice
        unavailable_val = (127, 127, 127)
        exit_loc = Cord.rice_exit
        buy_amount = 10
    elif food == 'nori':
        menu_loc = Cord.menu_toppings
        item_loc = Cord.t_nori
        unavailable_val = (33, 30, 11)
        exit_loc = Cord.t_exit
        buy_amount = 10
    elif food == 'roe':
        menu_loc = Cord.menu_toppings
        item_loc = Cord.t_roe
        unavailable_val = (127, 61, 0)
        exit_loc = Cord.t_exit
        buy_amount = 10
    elif food == 'salmon':
        menu_loc = Cord.menu_toppings
        item_loc = Cord.t_salmon
        unavailable_val = (127, 71, 47)
        exit_loc = Cord.t_exit
        buy_amount = 5
    elif food == 'shrimp':
        menu_loc = Cord.menu_toppings
        item_loc = Cord.t_shrimp
        unavailable_val = (127, 71, 47)
        exit_loc = Cord.t_exit
        buy_amount = 5
    elif food == 'unagi':
        menu_loc = Cord.menu_toppings
        item_loc = Cord.t_unagi
        unavailable_val = (94, 49, 8)
        exit_loc = Cord.t_exit
        buy_amount = 5
    elif food == 'sake':
        menu_loc = Cord.menu_sake
        item_loc = Cord.sake_sake
        unavailable_val = (109, 123, 127)
        exit_loc = Cord.sake_exit
        buy_amount = 2

    mousePos(Cord.phone)
    #time.sleep(1)
    leftClick()
    
    mousePos(menu_loc)
    leftClick()
    time.sleep(.1)
    s = screenGrab()
    if s.getpixel(item_loc) != unavailable_val:
        print '%s is available' % food
        mousePos(item_loc)        
        leftClick()
        time.sleep(.5)
        mousePos(Cord.deliver_normal)
        foodOnHand[food] += buy_amount
        time.sleep(.5)
        leftClick()
        time.sleep(.5)
    else:
        print '%s not available' % food        
        mousePos(exit_loc)
        leftClick()
        time.sleep(1)


def checkFood():

    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
                print '%s is low and needs to be replenished' % i
                buyFood(i)
        elif i == 'salmon' or i == 'unagi' or i == 'shrimp':
            if j <= 2:
                print '%s is low and needs to be replenished' % i
                buyFood(i)


def checkContinue():

    box = (x_pad+177, y_pad+362, x_pad+463, y_pad+395)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()

    if a == 10608:
        return True
    else:
        return False


def startNextGame():

    mousePos((311, 377))
    leftClick()
    time.sleep(.1)
    leftClick()

##def checkServed(seat):
##
##    if seat == 1:
##        return SeatOne.served
##    elif seat == 2:
##        return SeatTwo.served
##    elif seat == 3:
##        return SeatThree.served
##    elif seat == 4:
##        return SeatFour.served
##    elif seat == 5:
##        return SeatFive.served
##    elif seat == 6:
##        return SeatSix.served


def checkCustomers():

    checkFood()
    for i in seats:
        seat_no = seats.index(i)+1
        item = getSeat(i, seat_no)
        if empty_seats[i] != item:
        
            if foodTypes.has_key(item):
                print 'table %s is occupied and needs %s' % (seat_no, foodTypes[item])
                makeFood(foodTypes[item])

        else:
            pass
                
        if seat_no % 3 == 0:
            clearTables()
            checkFood()
            
        

def main():
    #startGame()
    while True:
        checkCustomers()
        if checkContinue():
            startNextGame()
            
    pass

if __name__ == '__main__':
    main()
