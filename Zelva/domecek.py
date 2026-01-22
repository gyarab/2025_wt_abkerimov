from turtle import *
from math import sqrt
from random import randint



def domecek():
    x = randint(50, 350)
    for _ in range(4):
        forward(x)
        left(90)

    left(45)
    
    forward(sqrt(2) * x)
    
    for _ in range(2):
        left(90)
        forward((sqrt(2) * x)/2)
    
    left(90)
    forward(sqrt(2) * x)
domecek()
