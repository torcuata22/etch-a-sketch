from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400) #resize screen
#popup:
user_bet = screen.textinput(title = "Place your bets", prompt = "Which turtle will win the race? Choose a color: " )
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index]) #send turtle to the start of line (left edge), height changes
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose. The {winning_color} turtle is the winner")



        random_distance = random.randint(0,10)
        turtle.forward(random_distance)








#Etch-a-sketch:
#tim = Turtle()
# def move_forward():
#     tim.forward(10)

# def move_backwards():
#     tim.back(10)

# def counter_clockwise():
#     tim.left(10)

# def clockwise():
#     tim.right(10)

# def clear_screen():
#     tim.reset()
#     #OR:
#     #tim.clear()
#     #tim.penup()
#     #tim.home()







# #tell screen to start listening:
# screen.listen()
# #bind keystroke to event (use event listener onkey(), need to create function to pass to this):
# screen.onkey(key = "w", fun = move_forward)
# screen.onkey(key = "s", fun = move_backwards)
# screen.onkey(key = "a", fun = counter_clockwise)
# screen.onkey(key = "d", fun = clockwise)
# screen.onkey(key = "c", fun = clear_screen)


screen.exitonclick()