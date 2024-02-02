from tts import *

def bingo():

    from random import randint
    from time import sleep
    n = randint(1, 100)
    list=[]
    while len(list)<=100:
        while n in list:
            n=randint(1,100)
        list.append(n)
        print(n)
        say(n)
        say(n)
        say(n)