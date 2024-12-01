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
states_guessed = []
written_state = turtle.Turtle()
written_state.penup()
written_state.hideturtle()
written_state.color('black')

while game_is_on:

    answer_state = screen.textinput(title=f'{score}/50  Guess the state', prompt="What's state's name?")
    answer_state = answer_state.title()
    print(answer_state)
    data = pandas.read_csv('50_states.csv')
    # print(data['state'])
    states_data = data.get('state').to_numpy()
    # print(f'Получаем список штатов через .get(): {states_data}')
    # print(f'Тип данных, которые получили через .get(): {type(states_data)}')
    # print(f'{states_data[0]}')
    # Первый вариант if clause. Не совсем подходит, так как data.values возвращает
    # не только штаты, но и координаты. Могут быть ошибки, если пользователь
    # случайно введет число вместо слова
    # if answer_state in data.values and answer_state not in states_guessed:
    if len(states_guessed) == 50:
        game_is_on = False

    if answer_state == 'Exit':
        break



    if answer_state in states_data and answer_state not in states_guessed:
        # print('Found!')
        # print(type(data.values))
        # print(data.values)
        # print(data.values[0])
        score += 1
        # print(score)
        states_guessed.append(answer_state)
        state_row = data[data.state == answer_state]
        X_STATE = state_row["x"].to_list()[0]
        print(X_STATE)
        Y_STATE = state_row["y"].to_list()[0]
        print(Y_STATE)
        written_state.goto(X_STATE, Y_STATE)
        written_state.write(f'{answer_state}', align='center', font=('Courier', 11, 'bold'))
states_data = states_data.tolist()
print(type(states_data))
states_to_learn = list(set(states_data) - set(states_guessed))
states_to_learn_dic = {'states': states_to_learn}
df = pandas.DataFrame(states_to_learn_dic)
df.to_csv('states_to_learn.csv')


# turtle.mainloop()

# screen.exitonclick()
