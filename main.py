import turtle # To draw
import random # For if you want a random card
import sys # For exit()

class Card(object):
    '''Models a card
        Attributes: Suit, Number'''
    def __init__(self, suit, number):
        '''Initializes a playing card object'''
        self.suit = suit
        self.number = number
    def __str__(self):
        '''Returns the card as a string'''
        if self.number == "K":
            return "King of " + self.suit +"s"
        elif self.number == "Q":
            return "Queen of " + self.suit + "s"
        elif self.number == "J":
            return "Jack of " + self.suit + "s"
        elif self.number == "A":
            return "Ace of " + self.suit + "s"
        else:
            return self.number + " of " + self.suit + "s"

# Building Blocks
def card_outline(turtle):
    '''Creates a Card Outline'''
    turtle.pu()
    turtle.fd(50)
    turtle.circle(60, 90)
    turtle.fd(75)
    turtle.pd()
    for i in range(2):
        turtle.circle(45, 90)
        turtle.fd(150)
        turtle.circle(45, 90)
        turtle.fd(300)
    turtle.pu()
    turtle.seth(0) # Sets direction to 0 to reduce line count

def draw_spade(turtle):
        '''Draws a Spade'''
        turtle.pd()
        turtle.begin_fill()
        turtle.rt(90)
        turtle.circle(10, 135)
        turtle.rt(135)
        turtle.circle(-17.5, 90)
        turtle.rt(180)
        turtle.fd(35)
        turtle.rt(180)
        turtle.circle(-17.5, 90)
        turtle.rt(135)
        turtle.circle(10, 135)
        turtle.lt(40)
        turtle.fd(26.56)
        turtle.lt(100)
        turtle.fd(26.56)
        turtle.end_fill()
        turtle.pu()
        turtle.seth(0) # Sets direction to 0 to reduce line count

def draw_diamond(turtle):
    '''Draws a Diamond'''
    turtle.pd()
    turtle.color("red")
    turtle.begin_fill()
    turtle.rt(45)
    for i in range(2):
        turtle.circle(-35, 45)
        turtle.lt(180)
    turtle.lt(90)
    for t in range(2):
        turtle.lt(180)
        turtle.circle(-35,45)
    turtle.end_fill()
    turtle.pu()
    turtle.seth(0) # Sets direction to 0 to reduce line count

def draw_club(turtle):
    '''Draws a Club'''
    turtle.pd()
    turtle.begin_fill()
    turtle.rt(60)
    for i in range(3):
        turtle.circle(10, 300)
        if i != 2:
            turtle.lt(150)
    turtle.rt(135)
    turtle.circle(-10, 30)
    turtle.fd(10)
    turtle.rt(255)
    turtle.fd(15.18)
    turtle.rt(255)
    turtle.fd(10)
    turtle.circle(-10, 30)
    turtle.end_fill()
    turtle.pu()
    turtle.seth(0) # Sets direction to 0 to reduce line count

def draw_heart(turtle):
    '''Draws a Heart <3'''
    turtle.pd()
    turtle.color("red")
    turtle.begin_fill()
    turtle.rt(90)
    turtle.circle(-10, -210)
    turtle.lt(190.5)
    turtle.fd(25)
    turtle.lt(96.5)
    turtle.fd(24.14)
    turtle.circle(10,210)
    turtle.end_fill()
    turtle.pu()
    turtle.seth(0) # Sets direction to 0 to reduce line count

def draw_a(turtle):
    '''Draws the letter "A" in both corners of the card'''
    i = 1
    while i<=2:
        if i == 1: # Top Right
            turtle.goto(-112.5,125)
            turtle.pd()
            turtle.seth(60)
            turtle.width(width=2.5)
            turtle.fd(45)
            turtle.rt(120)
            turtle.fd(45)
            turtle.rt(180)
            turtle.fd(15)
            turtle.lt(60)
            turtle.fd(27.5)
            turtle.pu()
            i+=1
        else: # Bottom Left
            turtle.goto(95, -147.5)
            turtle.pd()
            turtle.seth(240)
            turtle.fd(45)
            turtle.rt(120)
            turtle.fd(45)
            turtle.rt(180)
            turtle.fd(15)
            turtle.lt(60)
            turtle.fd(27.5)
            turtle.width(width=1)
            turtle.pu()
            i += 1

def draw_k(turtle):
    '''Draws the letter "K" in both corners of the card'''
    i = 1
    while i<=2:
        if i == 1: # Top Right
            turtle.goto(-100, 115)
            turtle.pd()
            turtle.seth(90)
            turtle.width(width=2.5)
            turtle.fd(45)
            turtle.rt(180)
            turtle.fd(22.5)
            turtle.lt(135)
            turtle.fd(31.82)
            turtle.rt(180)
            turtle.fd(31.82)
            turtle.lt(90)
            turtle.fd(31.82)
            turtle.pu()
            i+=1
        else: # Bottom Left
            turtle.goto(82, -145)
            turtle.pd()
            turtle.seth(270)
            turtle.fd(45)
            turtle.rt(180)
            turtle.fd(22.5)
            turtle.lt(135)
            turtle.fd(31.82)
            turtle.rt(180)
            turtle.fd(31.82)
            turtle.lt(90)
            turtle.fd(31.82)
            turtle.width(width=1)
            turtle.pu()
            i+=1

def draw_q(turtle):
    '''Draws the letter "Q" in both corners of the card'''
    i = 1
    while i <= 2:
        if i == 1: # Top Right
            turtle.goto(-75, 135)
            turtle.pd()
            turtle.seth(90)
            turtle.width(width=2.5)
            turtle.circle(15,360)
            turtle.circle(15,-45)
            turtle.rt(90)
            turtle.fd(10)
            turtle.rt(180)
            turtle.fd(20)
            turtle.pu()
            i+=1
        else: # Bottom Left
            turtle.goto(55,-160)
            turtle.pd()
            turtle.seth(270)
            turtle.circle(15, 360)
            turtle.circle(15, -45)
            turtle.rt(90)
            turtle.fd(10)
            turtle.rt(180)
            turtle.fd(20)
            turtle.width(width=1)
            i+=1

def draw_j(turtle):
    '''Draws the letter "J" in both corners of the card'''
    i = 1
    while i <= 2:
        if i == 1: # Top Right
            turtle.goto(-80, 150)
            turtle.pd()
            turtle.seth(270)
            turtle.width(width=2.5)
            turtle.fd(30)
            turtle.rt(180)
            turtle.circle(12.5,-180)
            turtle.pu()
            i+=1
        else: # Bottom Left
            turtle.goto(60,-175)
            turtle.pd()
            turtle.seth(90)
            turtle.fd(30)
            turtle.rt(180)
            turtle.circle(12.5, -180)
            turtle.pu()
            i += 1

def draw_10(turtle):
    '''Draws a "10" in both corners of the card'''
    i = 1
    while i <= 2:
        if i == 1: # Top Right
            turtle.goto(-100, 160)
            turtle.pd()
            turtle.seth(270)
            turtle.width(width=2.5)
            turtle.fd(25)
            turtle.pu()
            turtle.lt(90)
            turtle.fd(25)
            turtle.pd()
            turtle.circle(12.5,360)
            turtle.pu()
            i  += 1
        else: # Bottom Left
            turtle.goto(80,-190)
            turtle.pd()
            turtle.seth(90)
            turtle.fd(25)
            turtle.pu()
            turtle.lt(90)
            turtle.fd(25)
            turtle.pd()
            turtle.circle(12.5, 360)
            turtle.width(width=1)
            i += 1

def draw_9(turtle):
    '''Draws a "9" in both corners of the card'''
    i = 1
    while i <=2:
        if i == 1: # Top Right
            turtle.goto(-95, 155)
            turtle.seth(0)
            turtle.pd()
            turtle.width(width=2.5)
            turtle.circle(-10, 480)
            turtle.fd(25)
            turtle.pu()
            i+=1
        else: # Bottom Left
            turtle.goto(75, -178)
            turtle.seth(180)
            turtle.pd()
            turtle.circle(-10, 480)
            turtle.fd(25)
            turtle.width(width=1)
            i+=1

def draw_8(turtle):
    '''Draws an "8" in both corners of the card'''
    i = 1
    while i <= 2:
        if i == 1: # Top Right
            turtle.goto(-95, 155)
            turtle.seth(0)
            turtle.pd()
            turtle.width(width=2.5)
            turtle.circle(-10, 540)
            turtle.circle(11, 360)
            turtle.pu()
            i+= 1
        else: # Bottom Left
            turtle.goto(75, -180)
            turtle.seth(180)
            turtle.pd()
            turtle.circle(-10, 540)
            turtle.circle(11, 360)
            turtle.width(width=1)
            i+=1

def draw_7(turtle):
    '''Draws a "7" in both corners of the card'''
    i = 1
    while i <= 2:
        if i == 1: # Top Right
            turtle.goto(-100, 150)
            turtle.seth(0)
            turtle.pd()
            turtle.width(width=2.5)
            turtle.fd(25)
            turtle.lt(240)
            turtle.fd(37.5)
            turtle.pu()
            i+=1
        else: # Bottom Left
            turtle.goto(75, -180)
            turtle.seth(180)
            turtle.pd()
            turtle.fd(25)
            turtle.lt(240)
            turtle.fd(37.5)
            turtle.width(width=1)
            turtle.pu()
            i+=1

def draw_6(turtle):
    '''Draws a "6" in both corners of the card'''
    i = 1
    while i <= 2:
        if i == 1: # Top Right
            turtle.goto(-95, 130)
            turtle.seth(180)
            turtle.pd()
            turtle.width(width=2.5)
            turtle.circle(-10, 480)
            turtle.fd(25)
            turtle.pu()
            i += 1
        else: # Bottom Left
            turtle.goto(75, -153)
            turtle.seth(0)
            turtle.pd()
            turtle.circle(-10, 480)
            turtle.fd(25)
            turtle.width(width=1)
            i += 1

def draw_5(turtle):
    '''Draws a "5" in both corners of the card'''
    i=1
    while i <= 2:
        if i == 1: # Top Right
            turtle.goto(-85, 150)
            turtle.seth(0)
            turtle.pd()
            turtle.width(width=2.5)
            turtle.bk(17.5)
            turtle.rt(90)
            turtle.fd(15)
            turtle.lt(120)
            turtle.fd(9)
            turtle.rt(210)
            turtle.circle(10.5,-240)
            turtle.pu()
            i+=1
        else: # Bottom Left
            turtle.goto(60, -180)
            turtle.seth(180)
            turtle.pd()
            turtle.bk(17.5)
            turtle.rt(90)
            turtle.fd(15)
            turtle.lt(120)
            turtle.fd(9)
            turtle.rt(210)
            turtle.circle(10.5, -240)
            turtle.width(width=1)
            turtle.pu()
            i+=1

def draw_4(turtle):
    '''Draws a "4" in both corners of the card'''
    i = 1
    while i <= 2:
        if i == 1: # Top Right
            turtle.goto(-90, 130)
            turtle.pd()
            turtle.seth(90)
            turtle.width(width=2.5)
            turtle.fd(30)
            turtle.lt(135)
            turtle.fd(22.5)
            turtle.rt(225)
            turtle.fd(20)
            turtle.pu()
            i+=1
        else: # Bottom Left
            turtle.goto(65, -160)
            turtle.pd()
            turtle.seth(270)
            turtle.fd(30)
            turtle.lt(135)
            turtle.fd(22.5)
            turtle.rt(225)
            turtle.fd(20)
            turtle.width(width=1)
            turtle.pu()
            i += 1

def draw_3(turtle):
    '''Draws a very scuffed "3" in both corners of the card'''
    i = 1
    while i <= 2:
        if i == 1: # Top Right
            turtle.goto(-95, 155)
            turtle.seth(15)
            turtle.pd()
            turtle.width(width=2.5)
            turtle.circle(-7.5, 195)
            turtle.circle(-7.5,-15)
            turtle.seth(0)
            turtle.circle(-8.5, 210)
            turtle.pu()
            i += 1
        else: # Bottom Left
            turtle.goto(75, -180)
            turtle.seth(195)
            turtle.pd()
            turtle.circle(-7.5, 195)
            turtle.circle(-7.5,-15)
            turtle.seth(180)
            turtle.circle(-8.5, 210)
            turtle.width(width=1)
            i += 1

def draw_2(turtle):
    '''Draws a "2" in both corners of the card'''
    i = 1
    while i <= 2:
        if i == 1: # Top Right
            turtle.goto(-100,150)
            turtle.seth(90)
            turtle.pd()
            turtle.width(width=2.5)
            turtle.circle(-7.5,225)
            turtle.fd(17.5)
            turtle.rt(225)
            turtle.fd(16)
            turtle.pu()
            i+=1
        else: # Bottom Left
            turtle.goto(80, -175)
            turtle.seth(270)
            turtle.pd()
            turtle.circle(-7.5, 225)
            turtle.fd(17.5)
            turtle.rt(225)
            turtle.fd(16)
            turtle.width(width=1)
            turtle.pu()
            i += 1

# Cards
def ace_spade(turtle):
    '''Draws The Ace of Spades'''
    card_outline(turtle)
    turtle.seth(0)
    turtle.goto(-60,0)
    turtle.pd()
    turtle.begin_fill()
    turtle.rt(90)
    turtle.circle(30,135)
    turtle.seth(270)
    turtle.circle(-45,90)
    turtle.seth(0)
    turtle.fd(90)
    turtle.seth(180)
    turtle.circle(-45,90)
    turtle.rt(135)
    turtle.circle(30,135)
    turtle.lt(40)
    turtle.fd(79.677)
    turtle.lt(100)
    turtle.fd(79.677)
    turtle.end_fill()
    turtle.pu()
    draw_a(turtle)

def ace_diamond(turtle):
    '''Draws The Ace of Diamonds'''
    card_outline(turtle)
    turtle.goto(-40,-15)
    turtle.seth(0)
    turtle.pd()
    turtle.color("red")
    turtle.begin_fill()
    turtle.rt(45)
    for i in range(2):
        turtle.circle(-120, 45)
        turtle.lt(180)
    turtle.lt(90)
    for t in range(2):
        turtle.lt(180)
        turtle.circle(-120, 45)
    turtle.end_fill()
    turtle.pu()
    draw_a(turtle)

def ace_club(turtle):
    '''Draws The Ace of Clubs'''
    card_outline(turtle)
    turtle.goto(0,-20)
    turtle.seth(0)
    turtle.pd()
    turtle.begin_fill()
    turtle.rt(60)
    for i in range (3):
        turtle.circle(15,300)
        if i !=2:
            turtle.lt(150)
    turtle.rt(135)
    turtle.circle(-15, 30)
    turtle.fd(15)
    turtle.rt(255)
    turtle.fd(22.76)
    turtle.rt(255)
    turtle.fd(15)
    turtle.circle(-15, 30)
    turtle.end_fill()
    turtle.pu()
    draw_a(turtle)

def ace_heart(turtle):
    '''Draws The Ace of Hearts <3'''
    card_outline(turtle)
    turtle.goto(-7.5,0)
    turtle.seth(0)
    turtle.pd()
    turtle.color("red")
    turtle.begin_fill()
    turtle.rt(90)
    turtle.circle(-30, -210)
    turtle.lt(190)
    turtle.fd(81.84)
    turtle.lt(97.45)
    turtle.fd(77.5)
    turtle.circle(30, 220)
    turtle.end_fill()
    turtle.pu()
    draw_a(turtle)

def spade_2(turtle):
    '''Draws the 2 of Spades'''
    card_outline(turtle)
    turtle.goto(-25,100)
    draw_spade(turtle)
    turtle.goto(10,-125)
    turtle.seth(180)
    draw_spade(turtle)
    draw_2(turtle)

def diamond2(turtle): # Used to reduce length
    '''Draws 2 diamonds'''
    card_outline(turtle)
    turtle.goto(-17.5, 100)
    draw_diamond(turtle)
    turtle.goto(-17.5, -125)
    draw_diamond(turtle)

def diamond_2(turtle):
    '''Draws the 2 of Diamonds'''
    diamond2(turtle)
    draw_2(turtle)

def club_2(turtle):
    '''Draws the 2 of Clubs'''
    card_outline(turtle)
    turtle.goto(-5,100)
    draw_club(turtle)
    turtle.goto(-15,-125)
    turtle.seth(180)
    draw_club(turtle)
    draw_2(turtle)

def heart_2(turtle):
    '''Draws the 2 of Hearts <3'''
    card_outline(turtle)
    turtle.goto(-10,100)
    draw_heart(turtle)
    turtle.goto(-10,-125)
    turtle.seth(180)
    draw_heart(turtle)
    draw_2(turtle)

def spade_3(turtle):
    '''Draws the 3 of Spades'''
    card_outline(turtle)
    turtle.goto(-25,100)
    draw_spade(turtle)
    turtle.goto(-25,-125)
    draw_spade(turtle)
    turtle.goto(-25, -12.5)
    draw_spade(turtle)
    draw_3(turtle)

def diamond_3(turtle):
    '''Draws the 3 of Diamonds'''
    diamond2(turtle)
    turtle.goto(-20,-12.5)
    draw_diamond(turtle)
    draw_3(turtle)

def club_3(turtle):
    '''Draws the 3 of Clubs'''
    card_outline(turtle)
    turtle.goto(-5,100)
    draw_club(turtle)
    turtle.goto(-5,-15)
    draw_club(turtle)
    turtle.goto(-5,-127.5)
    draw_club(turtle)
    draw_3(turtle)

def heart_3(turtle):
    '''Draws the 3 of Hearts <3'''
    card_outline(turtle)
    turtle.goto(-10,100)
    draw_heart(turtle)
    turtle.goto(-10,-12.5)
    draw_heart(turtle)
    turtle.goto(-10,-125)
    draw_heart(turtle)
    draw_3(turtle)

def spade4(turtle): # Used to reduce length
    '''Draws 4 spades'''
    card_outline(turtle)
    turtle.goto(-80,100)
    draw_spade(turtle)
    turtle.goto(-45, -125)
    turtle.seth(180)
    draw_spade(turtle)
    turtle.goto(25,100)
    draw_spade(turtle)
    turtle.goto(60,-125)
    turtle.seth(180)
    draw_spade(turtle)

def spade_4(turtle):
    '''Draws the 4 of Spades'''
    spade4(turtle)
    draw_4(turtle)

def diamond4(turtle): # Used to reduce length
    '''Draws 4 diamonds'''
    card_outline(turtle)
    turtle.goto(-75, 100)
    draw_diamond(turtle)
    turtle.goto(-75,-125)
    draw_diamond(turtle)
    turtle.goto(30, 100)
    draw_diamond(turtle)
    turtle.goto(30,-125)
    draw_diamond(turtle)

def diamond_4(turtle):
    '''Draws the 4 of Diamonds'''
    diamond4(turtle)
    draw_4(turtle)

def club4(turtle): # Used to reduce length
    '''Draws 4 clubs'''
    card_outline(turtle)
    turtle.goto(-45,100)
    draw_club(turtle)
    turtle.goto(-55,-127.5)
    turtle.seth(180)
    draw_club(turtle)
    turtle.goto(35,100)
    draw_club(turtle)
    turtle.goto(25,-127.5)
    turtle.seth(180)
    draw_club(turtle)

def club_4(turtle):
    '''Draws the 4 of Clubs'''
    club4(turtle)
    draw_4(turtle)

def heart4(turtle): # Used to reduce length
    '''Draws 4 hearts'''
    card_outline(turtle)
    turtle.goto(-57.5,100)
    draw_heart(turtle)
    turtle.goto(-60,-125)
    turtle.seth(180)
    draw_heart(turtle)
    turtle.goto(40,100)
    draw_heart(turtle)
    turtle.goto(37.5,-125)
    turtle.seth(180)
    draw_heart(turtle)

def heart_4(turtle):
    '''Draws the 4 of Hearts'''
    heart4(turtle)
    draw_4(turtle)

def spade_5(turtle):
    '''Draws the 5 of Spades'''
    spade4(turtle)
    turtle.goto(-25,-12.5)
    draw_spade(turtle)
    draw_5(turtle)

def diamond_5(turtle):
    '''Draws the 5 of Diamonds'''
    diamond4(turtle)
    turtle.goto(-22.5,-12.5)
    draw_diamond(turtle)
    draw_5(turtle)

def club_5(turtle):
    '''Draws the 5 of Clubs'''
    club4(turtle)
    turtle.goto(-5,-13.75)
    draw_club(turtle)
    draw_5(turtle)

def heart_5(turtle):
    '''Draws the 5 of Hearts <3'''
    heart4(turtle)
    turtle.goto(-7.5,-10)
    draw_heart(turtle)
    draw_5(turtle)

def spade6(turtle): # Used to reduce length
    '''Draws 6 spades'''
    card_outline(turtle)
    turtle.goto(-80,100)
    draw_spade(turtle)
    turtle.goto(-80, -125)
    draw_spade(turtle)
    turtle.goto(25,100)
    draw_spade(turtle)
    turtle.goto(25,-125)
    draw_spade(turtle)
    turtle.goto(25,-10)
    draw_spade(turtle)
    turtle.goto(-80,-10)
    draw_spade(turtle)

def spade_6(turtle):
    '''Draws the 6 of Spades'''
    spade6(turtle)
    draw_6(turtle)

def diamond6(turtle): # Used to reduce length
    '''Draws 6 diamonds'''
    card_outline(turtle)
    turtle.goto(-75,100)
    draw_diamond(turtle)
    turtle.goto(-75,-12.5)
    draw_diamond(turtle)
    turtle.goto(-75,-125)
    draw_diamond(turtle)
    turtle.goto(30,100)
    draw_diamond(turtle)
    turtle.goto(30,-12.5)
    draw_diamond(turtle)
    turtle.goto(30,-125)
    draw_diamond(turtle)

def diamond_6(turtle):
    '''Draws the 6 of Diamonds'''
    diamond6(turtle)
    draw_6(turtle)

def club6(turtle): # Used to reduce length
    '''Draws 6 clubs'''
    card_outline(turtle)
    turtle.goto(-55, 90)
    draw_club(turtle)
    turtle.goto(-55, -117.5)
    draw_club(turtle)
    turtle.goto(-55,-13.75)
    draw_club(turtle)
    turtle.goto(45, 90)
    draw_club(turtle)
    turtle.goto(45,-13.75)
    draw_club(turtle)
    turtle.goto(45, -117.5)
    draw_club(turtle)

def club_6(turtle):
    '''Draws the 6 of Clubs'''
    club6(turtle)
    draw_6(turtle)

def heart6(turtle): # Used to reduce length
    '''Draws 6 hearts'''
    card_outline(turtle)
    turtle.goto(-57.5,100)
    draw_heart(turtle)
    turtle.goto(-57.5,-12.5)
    draw_heart(turtle)
    turtle.goto(-57.5,-125)
    draw_heart(turtle)
    turtle.goto(40,100)
    draw_heart(turtle)
    turtle.goto(40,-12.5)
    draw_heart(turtle)
    turtle.goto(40,-125)
    draw_heart(turtle)

def heart_6(turtle):
    '''Draws the 6 of Hearts <3'''
    heart6(turtle)
    draw_6(turtle)

def spade_7(turtle):
    '''Draws the 7 of Spades'''
    spade6(turtle)
    turtle.goto(-27.5,-10)
    draw_spade(turtle)
    draw_7(turtle)

def diamond_7(turtle):
    '''Draws the 7 of Diamonds'''
    diamond6(turtle)
    turtle.goto(-22.5, -12.5)
    draw_diamond(turtle)
    draw_7(turtle)

def club_7(turtle):
    '''Draws the 7 of Clubs'''
    club6(turtle)
    turtle.goto(-5,-13.75)
    draw_club(turtle)
    draw_7(turtle)

def heart_7(turtle):
    '''Draws the 7 of Hearts <3'''
    heart6(turtle)
    turtle.goto(-8.25, -12.5)
    draw_heart(turtle)
    draw_7(turtle)

def spade8(turtle): # Used to reduce length
    '''Draws 8 spades'''
    card_outline(turtle)
    turtle.goto(-80, 95)
    draw_spade(turtle)
    turtle.goto(-80, 20)
    draw_spade(turtle)
    turtle.goto(-45, -55)
    turtle.seth(180)
    draw_spade(turtle)
    turtle.goto(-45, -130)
    turtle.seth(180)
    draw_spade(turtle)
    turtle.goto(25, 95)
    draw_spade(turtle)
    turtle.goto(25, 20)
    draw_spade(turtle)
    turtle.goto(60, -55)
    turtle.seth(180)
    draw_spade(turtle)
    turtle.goto(60, -130)
    turtle.seth(180)
    draw_spade(turtle)

def spade_8(turtle):
    '''Draws the 8 of Spades'''
    spade8(turtle)
    draw_8(turtle)

def diamond8(turtle): # Used to reduce length
    '''Draws 8 diamonds'''
    card_outline(turtle)
    turtle.goto(-75,95)
    draw_diamond(turtle)
    turtle.goto(-75,20)
    draw_diamond(turtle)
    turtle.goto(-75,-55)
    draw_diamond(turtle)
    turtle.goto(-75,-130)
    draw_diamond(turtle)
    turtle.goto(30,95)
    draw_diamond(turtle)
    turtle.goto(30,20)
    draw_diamond(turtle)
    turtle.goto(30,-55)
    draw_diamond(turtle)
    turtle.goto(30,-130)
    draw_diamond(turtle)

def diamond_8(turtle):
    '''Draws the 8 of Diamonds'''
    diamond8(turtle)
    draw_8(turtle)

def club8(turtle): # Used to reduce length
    '''Draws 8 clubs'''
    card_outline(turtle)
    turtle.goto(-55,95)
    draw_club(turtle)
    turtle.goto(-55, 20)
    draw_club(turtle)
    turtle.goto(-65,-55)
    turtle.seth(180)
    draw_club(turtle)
    turtle.goto(-65,-130)
    turtle.seth(180)
    draw_club(turtle)
    turtle.goto(45,95)
    draw_club(turtle)
    turtle.goto(45,20)
    draw_club(turtle)
    turtle.goto(35,-55)
    turtle.seth(180)
    draw_club(turtle)
    turtle.goto(35,-130)
    turtle.seth(180)
    draw_club(turtle)

def club_8(turtle):
    '''Draws the 8 of Clubs'''
    club8(turtle)
    draw_8(turtle)

def heart8(turtle): # Used to reduce length
    '''Draws 8 hearts '''
    card_outline(turtle)
    turtle.goto(-57.5,95)
    draw_heart(turtle)
    turtle.goto(-57.5,20)
    draw_heart(turtle)
    turtle.goto(-60,-55)
    turtle.seth(180)
    draw_heart(turtle)
    turtle.goto(-60,-130)
    turtle.seth(180)
    draw_heart(turtle)
    turtle.goto(40,95)
    draw_heart(turtle)
    turtle.goto(40,20)
    draw_heart(turtle)
    turtle.goto(37.5,-55)
    turtle.seth(180)
    draw_heart(turtle)
    turtle.goto(37.5,-130)
    turtle.seth(180)
    draw_heart(turtle)

def heart_8(turtle):
    '''Draws the 8 of Hearts <3'''
    heart8(turtle)
    draw_8(turtle)

def spade_9(turtle):
    '''Draws the 9 of Spades'''
    spade8(turtle)
    turtle.goto(-27.5,0)
    draw_spade(turtle)
    draw_9(turtle)

def diamond_9(turtle):
    '''Draws the 9 of Diamonds'''
    diamond8(turtle)
    turtle.goto(-22.5,-12.5)
    draw_diamond(turtle)
    draw_9(turtle)

def club_9(turtle):
    '''Draws the 9 of Clubs'''
    club8(turtle)
    turtle.goto(-5,-20)
    draw_club(turtle)
    draw_9(turtle)

def heart_9(turtle):
    '''Draws the 9 of Hearts <3'''
    heart8(turtle)
    turtle.goto(-7.5,-10)
    draw_heart(turtle)
    draw_9(turtle)

def spade_10(turtle):
    '''Draws the 10 of Spades'''
    spade8(turtle)
    turtle.goto(-27.5,50)
    draw_spade(turtle)
    turtle.goto(7.5,-85)
    turtle.seth(180)
    draw_spade(turtle)
    draw_10(turtle)

def diamond_10(turtle):
    '''Draws the 10 of diamonds'''
    diamond8(turtle)
    turtle.goto(-22.5,50)
    draw_diamond(turtle)
    turtle.goto(-22.5,-85)
    draw_diamond(turtle)
    draw_10(turtle)

def club_10(turtle):
    '''Draws the 10 of Clubs'''
    club8(turtle)
    turtle.goto(-5,50)
    draw_club(turtle)
    turtle.goto(-15,-85)
    turtle.seth(180)
    draw_club(turtle)
    draw_10(turtle)

def heart_10(turtle):
    '''Draws the 10 of Hearts <3'''
    heart8(turtle)
    turtle.goto(-7.5,57.5)
    draw_heart(turtle)
    turtle.goto(-7.5,-77.5)
    draw_heart(turtle)
    draw_10(turtle)

def spade_j(turtle):
    '''Draws the Jack of Spades'''
    Slippy.pu()
    Slippy.goto(-10,-10)
    Slippy.shape(jack)
    card_outline(turtle)
    turtle.goto(-100,-150)
    draw_spade(turtle)
    turtle.goto(80,135)
    turtle.seth(180)
    draw_spade(turtle)
    draw_j(turtle)

def diamond_j(turtle):
    '''Draws the Jack of Diamonds'''
    Slippy.pu()
    Slippy.goto(-10,-10)
    Slippy.shape(jack)
    card_outline(turtle)
    turtle.goto(-100,-155)
    draw_diamond(turtle)
    turtle.goto(80,135)
    turtle.seth(180)
    draw_diamond(turtle)
    draw_j(turtle)

def club_j(turtle):
    '''Draws the Jack of Clubs'''
    Slippy.pu()
    Slippy.goto(-10,-10)
    Slippy.shape(jack)
    card_outline(turtle)
    turtle.goto(-90,-155)
    draw_club(turtle)
    turtle.goto(70,135)
    turtle.seth(180)
    draw_club(turtle)
    draw_j(turtle)

def heart_j(turtle):
    '''Draws the Jack of Hearts'''
    Slippy.pu()
    Slippy.goto(-10, -10)
    Slippy.shape(jack)
    card_outline(turtle)
    turtle.goto(-90, -155)
    draw_heart(turtle)
    turtle.goto(70, 135)
    turtle.seth(180)
    draw_heart(turtle)
    draw_j(turtle)

def spade_q(turtle):
    '''Draws the Queen of Spades'''
    Slippy.pu()
    Slippy.goto(-10,-10)
    Slippy.shape(queen)
    card_outline(turtle)
    turtle.goto(-100,-150)
    draw_spade(turtle)
    turtle.goto(80,135)
    turtle.seth(180)
    draw_spade(turtle)
    draw_q(turtle)

def diamond_q(turtle):
    '''Draws the Queen of Diamonds'''
    Slippy.pu()
    Slippy.goto(-10,-10)
    Slippy.shape(queen)
    card_outline(turtle)
    turtle.goto(-100,-155)
    draw_diamond(turtle)
    turtle.goto(80,135)
    turtle.seth(180)
    draw_diamond(turtle)
    draw_q(turtle)

def club_q(turtle):
    '''Draws the Queen of Clubs'''
    Slippy.pu()
    Slippy.goto(-10,-10)
    Slippy.shape(queen)
    card_outline(turtle)
    turtle.goto(-90,-155)
    draw_club(turtle)
    turtle.goto(70,135)
    turtle.seth(180)
    draw_club(turtle)
    draw_q(turtle)

def heart_q(turtle):
    '''Draws the Queen of Hearts <3'''
    Slippy.pu()
    Slippy.goto(-10, -10)
    Slippy.shape(queen)
    card_outline(turtle)
    turtle.goto(-90, -155)
    draw_heart(turtle)
    turtle.goto(70, 135)
    turtle.seth(180)
    draw_heart(turtle)
    draw_q(turtle)

def spade_k(turtle):
    '''Draws the King of Spades'''
    Slippy.pu()
    Slippy.goto(-10,-10)
    Slippy.shape(king)
    card_outline(turtle)
    turtle.goto(-100,-150)
    draw_spade(turtle)
    turtle.goto(80,135)
    turtle.seth(180)
    draw_spade(turtle)
    draw_k(turtle)

def diamond_k(turtle):
    '''Draws the King of Spades'''
    Slippy.pu()
    Slippy.goto(-10,-10)
    Slippy.shape(king)
    card_outline(turtle)
    turtle.goto(-100,-155)
    draw_diamond(turtle)
    turtle.goto(80,135)
    turtle.seth(180)
    draw_diamond(turtle)
    draw_k(turtle)

def club_k(turtle):
    '''Draws the King of Clubs'''
    Slippy.pu()
    Slippy.goto(-10,-10)
    Slippy.shape(king)
    card_outline(turtle)
    turtle.goto(-90,-155)
    draw_club(turtle)
    turtle.goto(70,135)
    turtle.seth(180)
    draw_club(turtle)
    draw_k(turtle)

def heart_k(turtle):
    '''Draws the King of Hearts <3'''
    Slippy.pu()
    Slippy.goto(-10, -10)
    Slippy.shape(king)
    card_outline(turtle)
    turtle.goto(-90, -155)
    draw_heart(turtle)
    turtle.goto(70, 135)
    turtle.seth(180)
    draw_heart(turtle)
    draw_k(turtle)

def draw(card, turtle):
    '''Draws the appropriate card using the turtle'''
    if card.suit == "Spade":
        if card.number == "A": # If Spade and A
            ace_spade(turtle)
        elif card.number == "2": # If Spade and 2
            spade_2(turtle)
        elif card.number == "3": # If Spade and 3
            spade_3(turtle)
        elif card.number == "4": # If Spade and 4
            spade_4(turtle)
        elif card.number == "5": # If Spade and 5
            spade_5(turtle)
        elif card.number == "6": # If Spade and 6
            spade_6(turtle)
        elif card.number == "7": # If Spade and 7
            spade_7(turtle)
        elif card.number == "8": # If Spade and 8
            spade_8(turtle)
        elif card.number == "9": # If Spade and 9
            spade_9(turtle)
        elif card.number == "10": # If Spade and 10
            spade_10(turtle)
        elif card.number == "J": # If Spade and Jack
            spade_j(turtle)
        elif card.number == "Q": # If Spade and Queen
            spade_q(turtle)
        elif card.number == "K": # If Spade and King
            spade_k(turtle)
        else: # If Spade but not number
            input("How")
    elif card.suit == "Diamond":
        if card.number == "A": # If Diamond and A
            ace_diamond(turtle)
        elif card.number == "2": # If Diamond and 2
            diamond_2(turtle)
        elif card.number == "3": # If Diamond and 3
            diamond_3(turtle)
        elif card.number == "4": # If Diamond and 4
            diamond_4(turtle)
        elif card.number == "5": # If Diamond and 5
            diamond_5(turtle)
        elif card.number == "6": # If Diamond and 6
            diamond_6(turtle)
        elif card.number == "7": # If Diamond and 7
            diamond_7(turtle)
        elif card.number == "8": # If Diamond and 8
            diamond_8(turtle)
        elif card.number == "9": # If Diamond and 9
            diamond_9(turtle)
        elif card.number == "10": # If Diamond and 10
            diamond_10(turtle)
        elif card.number == "J": # If Diamond and Jack
            diamond_j(turtle)
        elif card.number == "Q": # If Diamond and Queen
            diamond_q(turtle)
        elif card.number == "K": # If Diamond and King
            diamond_k(turtle)
        else: # If Diamond but not number
            input("How")
    elif card.suit == "Club":
        if card.number == "A": # If Club and A
            ace_club(turtle)
        elif card.number == "2": # If Club and 2
            club_2(turtle)
        elif card.number == "3": # If Club and 3
            club_3(turtle)
        elif card.number == "4": # If Club and 4
            club_4(turtle)
        elif card.number == "5": # If Club and 5
            club_5(turtle)
        elif card.number == "6": # If Club and 6
            club_6(turtle)
        elif card.number == "7": # If Club and 7
            club_7(turtle)
        elif card.number == "8": # If Club and 8
            club_8(turtle)
        elif card.number == "9": # If Club and 9
            club_9(turtle)
        elif card.number == "10": # If Club and 10
            club_10(turtle)
        elif card.number == "J": # If Club and Jack
            club_j(turtle)
        elif card.number == "Q": # If Club and Queen
            club_q(turtle)
        elif card.number == "K": # If Club and King
            club_k(turtle)
        else: # If Club but not number
            input("How")
    else: # If card.suit == "Heart"
        if card.number == "A": # If Heart and A
            ace_heart(turtle)
        elif card.number == "2": # If Heart and 2
            heart_2(turtle)
        elif card.number == "3": # If Heart and 3
            heart_3(turtle)
        elif card.number == "4": # If Heart and 4
            heart_4(turtle)
        elif card.number == "5": # If Heart and 5
            heart_5(turtle)
        elif card.number == "6": # If Heart and 6
            heart_6(turtle)
        elif card.number == "7": # If Heart and 7
            heart_7(turtle)
        elif card.number == "8": # If Heart and 8
            heart_8(turtle)
        elif card.number == "9": # If Heart and 9
            heart_9(turtle)
        elif card.number == "10": # If Heart and 10
            heart_10(turtle)
        elif card.number == "J": # If Heart and Jack
            heart_j(turtle)
        elif card.number == "Q": # If Heart and Queen
            heart_q(turtle)
        elif card.number == "K": # If Heart and King
            heart_k(turtle)
        else: # If Heart but not number
            input("How")

# When run
name = input("Hello, please name your turtle") # Asks user for turtle name
while name.capitalize() == "Kyle":
    name = input("Hello, Kyle. I asked for a turtle name, not a monkey name. Please rename this turtle.") # Kyle is best monkey, but sadly not turtle
while name.capitalize() == "Test": # For testing porpoises
    answer = input("This is for testing, if you'd like to proceed with testing type 'Yes', otherwise you will be prompted to change your name")
    if answer.capitalize() != "Yes":
        name = input("Name your turtle (NOT 'Test' :)")
    else: # Proceeds to debug mode
        name = turtle.Turtle()
        Slippy = turtle.Turtle()
        screen = turtle.Screen()
        jack = "jacks.gif"
        queen = "queens.gif"
        king = "kings.gif"
        screen.register_shape(jack)
        screen.register_shape(queen)
        screen.register_shape(king)
        while answer.capitalize() == "Yes":
            inp = input("You can now test any function (Press enter to proceed, input anything to end testing)")
            if inp != "":
                input("Press enter to close this window")
                exit()
            else:
                s = input("Enter a number from 1-4 (Spade, Diamond, Club, Heart <3)")
                try:
                    int(s)
                    n = input("Enter a number from 1-13")
                    try:
                        int(n)
                        suits = ["Spade", "Diamond", "Club", "Heart"]
                        numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10","J","Q","K"]
                        s = suits[int(s)-1]
                        n = numbers[int(n)-1]
                        card = Card(s,n)
                        name.speed(0)
                        draw(card,name)
                        name.pu()
                        name.seth(0)
                        name.goto(0,0)
                        input("Press enter to clear and proceed with testing")
                        name.clear()
                        name.color("black")
                    except ValueError:
                        input("Test Failed (Press enter to continue)")
                except ValueError:
                    input("Test Failed (Press enter to continue)")
suit = input("What suit would you like to draw using " + name.capitalize() +  " ? (Type 'Random' for a random suit)") # Asks user for suit
if suit.capitalize() != "Spade" and suit.capitalize() != "Diamond" and suit.capitalize() != "Club" and suit.capitalize() != "Heart" and suit.capitalize() != "Random": # Checks if valid suit
    input(suit.capitalize() + " is not a valid suit :(, I will now draw a snek (Press enter to proceed)") # If invalid
    name = turtle.Turtle()
    screen = turtle.Screen()
    image = "snek.gif"
    screen.register_shape(image)
    name.shape(image)
    input("Press enter to close this window")
    exit()
if suit.capitalize() == "Random":
    suit = random.randrange(1,4)
    suits = ["Spade", "Diamond", "Club", "Heart"]
    suit = suits[suit] # Selects one of the four suits using the randomly generated value or inputted value
number = input("What number would you like to draw? (1-13 or Random)" ) # Asks user for number
if number.capitalize() != "Random": # Checks if random
    try:
        int(number) # Tries to concatenate to string and proceeds if it succeeds
        if int(number) > 13 or int(number)<1: # If number outside of range
            input(number + " is not a valid number :(, I will now draw a snek (Press enter to proceed)")
            name = turtle.Turtle()
            screen = turtle.Screen()
            image = "snek.gif"
            screen.register_shape(image)
            name.shape(image)
            input("Press enter to close this window")
            exit()
    except ValueError: # If variable number cannot be concatenated into type int
        input(number + " is not a valid number :(, I will now draw a snek (Press enter to proceed)")
        name = turtle.Turtle()
        screen = turtle.Screen()
        image = "snek.gif"
        screen.register_shape(image)
        name.shape(image)
        input("Press enter to close this window")
        exit()
else:
    number = random.randrange(1,13)
numbers = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
number = numbers[int(number)-1] # Selects a number using the randomly generated value or inputted value
card = Card(suit.capitalize(), number) # Creates card using suit and number; Suit is capitalized to reduce number of if statements I'd need
input(name + " will now draw the " + str(card) + " (Press enter to continue)") # Tells user their card in a neat way :)
name = turtle.Turtle() # Creates a turtle with the name user input
if number != "J" and number != "Q" and number != "K":
    pass
else: # If face card loads all 3 faces
    screen = turtle.Screen()
    jack = "jacks.gif"
    queen = "queens.gif"
    king = "kings.gif"
    screen.register_shape(jack)
    screen.register_shape(queen)
    screen.register_shape(king)
    Slippy = turtle.Turtle()
name.ht()  # Hides turtle so user can see card properly
draw(card,name) # Calls the draw function using the card and turtle objects
input("Thank you for participating. You can press enter to close this window")
exit()
# End
