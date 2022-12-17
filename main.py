from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)






#tell screen to start listening:
screen.listen()
#bind keystroke to event (use event listener onkey(), need to create function to pass to this):
screen.onkey(key = "space", fun = move_forward)
screen.exitonclick()