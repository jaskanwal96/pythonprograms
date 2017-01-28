import turtle
def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")
    ##draw_square()
    ##draw_circle()
    ##draw_triangle()
    draw_thatshape()
    window.exitonclick()

def draw_thatshape():
    bunny = turtle.Turtle()
    bunny.shape("triangle")
    bunny.color("white")
    bunny.speed(20)
    distance = 10
    for j in range(1,200):
        bunny.circle(distance)
        bunny.right(10)
        distance = distance + 1;
    bunny.forward(70)

    
def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)
    for j in range(1,90):
        for i in range(0,4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)
def draw_circle(): 
    sunny = turtle.Turtle()
    sunny.shape("arrow")
    sunny.color("blue")
    sunny.circle(100)
    
def draw_triangle():
    bunny = turtle.Turtle()
    bunny.shape("triangle")
    bunny.color("white")
    for i in range(0,2):
        bunny.forward(100)
        bunny.right(60)
    bunny.right(90)
    bunny.forward(180)

draw_shape()   
