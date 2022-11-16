import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Name Guess Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_data = data.to_dict()
# print(states['state'])

name = turtle.Turtle()
name.hideturtle()
name.penup()

states = states_data['state']
total_states = len(states)
guessed_states = []
while guessed_states != 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{total_states} States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    for id in states:
        if answer_state == states[id]:
            name.goto(states_data['x'][id], states_data['y'][id])
            name.write(answer_state)
            guessed_states.append(answer_state)

missed_states = [states[s] for s in states if states[s] not in guessed_states]
# for s in states['state']:
#     if states['state'][s] not in guessed_states:
#         missed_states.append(states['state'][s])

data_series = pandas.Series(missed_states)
data_series.to_csv("learn.csv")

screen.exitonclick()
