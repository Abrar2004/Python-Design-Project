
import turtle
bob= turtle.Turtle()
bob.speed(0)

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    
def illusion():
    bob.width(5)
    bob.color('black')
    bob.begin_fill()
    bob.circle(3)
    for times in range(4):
        bob.forward(50)
        bob.left(90)
    for times in range(4):
        bob.right(90)
        bob.forward(50)
        
    bob.penup()
    bob.goto(100,-100)
    bob.pendown()
    for times in range(4):
        bob.left(90)
        bob.forward(50)
    bob.penup()
    bob.goto(-100, 100)
    bob.pendown()
    for times in range(4):
        bob.forward(50)
        bob.right(90)
    bob.end_fill()
    
    bob.penup()
    bob.goto(-100,-100)
    bob.pendown()
    for times in range(4):
        bob.forward(200)
        bob.left(90)
def rhombus():
    bob.width(3)
    bob.fillcolor("red")
    bob.begin_fill()
    bob.left(45)
    bob.forward(70)
    bob.right(45)
    bob.forward(50)
    bob.right(135)
    bob.forward(70)
    bob.right(45)
    bob.forward(50)
    bob.end_fill()
    bob.fillcolor('yellow')
    bob.begin_fill()
    bob.right(90)
    bob.forward(50)
    bob.right(45)
    bob.forward(70)
    bob.right(135)
    bob.forward(50)
    bob.right(45)
    bob.forward(70)
    bob.left(45)
    bob.end_fill()
    bob.left(90)
    bob.forward(150)
    bob.fillcolor('yellow')
    bob.begin_fill()
    bob.left(135)
    bob.forward(70)
    bob.right(45)
    bob.forward(50)
    bob.right(135)
    bob.forward(70)
    bob.right(45)
    bob.end_fill()
    bob.fillcolor('red')
    bob.begin_fill()
    bob.left(90)
    bob.forward(50)
    bob.left(135)
    bob.forward(70)
    bob.left(45)
    bob.forward(50)
    bob.left(135)
    bob.forward(70)
    bob.left(45)
    bob.forward(50)
    bob.left(90)
    bob.end_fill()
    bob.fillcolor('red')
    bob.begin_fill()
    bob.forward(150)
    bob.left(135)
    bob.forward(70)
    bob.right(45)
    bob.forward(50)
    bob.right(135)
    bob.forward(70)
    bob.right(45)
    bob.forward(50)
    bob.end_fill()
    bob.fillcolor('yellow')
    bob.begin_fill()
    bob.right(135)
    bob.forward(70)
    bob.left(45)
    bob.forward(50)
    bob.left(135)
    bob.forward(70)
    bob.left(45)
    bob.forward(50)
    bob.end_fill()
    bob.left(90)
    bob.forward(150)
    bob.left(135)    
    bob.fillcolor('yellow')
    bob.begin_fill()
    bob.forward(70)
    bob.right(45)
    bob.forward(50)
    bob.right(135)
    bob.forward(70)
    bob.right(45)
    bob.forward(50)
    bob.end_fill()
    bob.fillcolor('red')
    bob.begin_fill()
    bob.left(180)
    bob.forward(50)
    bob.left(45)
    bob.forward(70)
    bob.right(135)
    bob.forward(50)
    bob.right(45)
    bob.forward(70)
    bob.right(135)
    bob.forward(50)
    bob.end_fill()
#first

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
def illusion2():
    bob.width(5)
    bob.color('black')
    bob.begin_fill()
    bob.circle(3)
    for times in range(4):
        bob.forward(50)
        bob.left(90)
    for times in range(4):
        bob.right(90)
        bob.forward(50)
        
    bob.penup()
    bob.goto(300,-100)
    bob.pendown()
    for times in range(4):
        bob.left(90)
        bob.forward(50)
    bob.penup()
    bob.goto(100, 100)
    bob.pendown()
    for times in range(4):
        bob.forward(50)
        bob.right(90)
    bob.end_fill()
    
    bob.penup()
    bob.goto(100,-100)
    bob.pendown()
    for times in range(4):
        bob.forward(200)
        bob.left(90)

    
