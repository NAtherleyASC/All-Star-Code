from Myro import *
init("sim")
def square(length):
    i=0
    while i<4:
        penDown()
        turnBy(90)
        forward(1.5, length)
        i=i+1
def add1(number):
    number=number+5
    return number

x=5
print(add1(x))
