from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)

def clear_screen():
    tim.reset()







#tell screen to start listening:
screen.listen()
#bind keystroke to event (use event listener onkey(), need to create function to pass to this):
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = counter_clockwise)
screen.onkey(key = "d", fun = clockwise)
screen.onkey(key = "c", fun = clear_screen)


screen.exitonclick()