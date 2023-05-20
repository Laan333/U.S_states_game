from turtle import Screen, Pen
import pandas

answer_true = 0
img = "blank_states_img.gif"

data = pandas.read_csv("50_states.csv")
all_states = data["state"]
new_data = all_states.to_list()

screen = Screen()
screen.title("U.S. States Game")
guessed_states = []
screen.addshape(img)  # Create IMG with shape settings
pen = Pen(shape=img)
while answer_true < len(all_states):
    answer_state = screen.textinput(title=f"Guess the state {answer_true}/{len(all_states)}",
                                    prompt="What`s another state? ").title()
    if answer_state == "Exit":
        df = pandas.DataFrame(new_data)
        df.to_csv("state_needs_to_learn.csv")
        break

    if answer_state in new_data:
        guessed_states.append(answer_state)
        new_data.remove(answer_state)

        answer_true += 1
        row_data = data[all_states == answer_state]
        coords_x = row_data["x"].iloc[0]
        coords_y = row_data["y"].iloc[0]

        pen_states = Pen()
        pen_states.hideturtle()
        pen_states.up()
        pen_states.goto(coords_x, coords_y)
        pen_states.write(answer_state)




