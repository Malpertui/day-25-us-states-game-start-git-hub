import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)


game_is_on = True
# data = pandas.read_csv('50_states.csv')
# print(data['state'])
score = 0
all_states = []
written_state = turtle.Turtle()
written_state.penup()
written_state.hideturtle()
written_state.color('black')

while game_is_on:

    answer_state = screen.textinput(title=f'{score}/50  Guess the state', prompt="What's state's name?")
    answer_state = answer_state.title()
    print(answer_state)
    data = pandas.read_csv('50_states.csv')
    state_row = data[data.state == answer_state]
    print(state_row)
    # temp_list = state_row["x"].to_list()
    # X_STATE = state_row["x"]._get_value(0)
    X_STATE = state_row["x"].to_list()[0]

    # temp_list = data['temp'].to_list()
    print('+++++++++')
    print(X_STATE)
    print(type(X_STATE))
    # print(X_STATE)


    # X_STATE = data[data.state == data[answer_state]]
    # print(X_STATE)
    # Y_STATE = data[data.y == data[answer_state]]
    # print(Y_STATE)

    # print(data['state'])

    # if answer_state in data.values and answer_state not in all_states:
    #     print('Found!')
    #     score += 1
    #     print(score)
    #     all_states.append(answer_state)
    #     X_STATE = data[data.x == data[answer_state]]
    #     print(X_STATE)
    #     Y_STATE = data[data.y == data[answer_state]]
    #     print(Y_STATE)
    #     written_state.goto(X_STATE, Y_STATE)
    #     written_state.write(f'{answer_state}', align='center', font=('Courier', 24, 'normal'))
    #



turtle.mainloop()

# screen.exitonclick()
