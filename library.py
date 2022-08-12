import time
import os
import random

def wait(dur):
    time.sleep(dur)


def clearConsole():
    os.system("clear")


def randInt(start, end):
    random.randint(start, end)


def loading(msg, time):
    for i in range(0, time):
        print(msg + ".")
        wait(0.2)
        clearConsole()
        print(msg + "..")
        wait(0.2)
        clearConsole()
        print(msg + "...")
        wait(0.2)
        clearConsole()
        print(msg + "....")
        wait(0.2)
        clearConsole()
        print(msg + ".....")
        wait(0.2)
        clearConsole()

