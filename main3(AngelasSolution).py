import turtle
import pandas
from jinja2.utils import missing

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50  Guess the state',
                                    prompt="What's state's name?").title()

    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')


        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state, align='center', font=('Arial', 8, 'normal'))
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

#
# game_is_on = True
# # data = pandas.read_csv('50_states.csv')
# # print(data['state'])
# score = 0
# all_states = []
# written_state = turtle.Turtle()
# written_state.penup()
# written_state.hideturtle()
# written_state.color('black')
#
# while game_is_on:
#
#     answer_state = screen.textinput(title=f'{score}/50  Guess the state', prompt="What's state's name?")
#     answer_state = answer_state.title()
#     print(answer_state)
#     data = pandas.read_csv('50_states.csv')
#     # print(data['state'])
#
#     if answer_state in data.values and answer_state not in all_states:
#         print('Found!')
#         score += 1
#         print(score)
#         all_states.append(answer_state)
#         state_row = data[data.state == answer_state]
#         X_STATE = state_row["x"].to_list()[0]
#         print(X_STATE)
#         Y_STATE = state_row["y"].to_list()[0]
#         print(Y_STATE)
#         written_state.goto(X_STATE, Y_STATE)
#         written_state.write(f'{answer_state}', align='center', font=('Courier', 11, 'bold'))
#



turtle.mainloop()

# screen.exitonclick()
