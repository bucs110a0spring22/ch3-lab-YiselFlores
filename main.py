import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
michelangelo.forward(random.randrange(1,101))
leonardo.forward(random.randrange(1,101))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for x in range(20):
 michelangelo.forward(random.randrange(1,11))
 leonardo.forward(random.randrange(1,11))
# Part B - complete part B here
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
michelangelo.hideturtle()
leonardo.down()
shapelist = [3,4,6,9,12]
for x in range(len(shapelist)):
  leonardo.clear()
  for y in range(shapelist[x]):
   leonardo.forward(20)
   deg = 360/shapelist[x]
   leonardo.right(deg)
 
window.exitonclick()
