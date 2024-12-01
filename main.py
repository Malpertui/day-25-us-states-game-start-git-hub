import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

game_is_on = True
score = 0
states_guessed = []
written_state = turtle.Turtle()
written_state.penup()
written_state.hideturtle()
written_state.color('black')

while game_is_on:

    answer_state = screen.textinput(title=f'{score}/50  Guess the state', prompt="What's state's name?")
    answer_state = answer_state.title()
    data = pandas.read_csv('50_states.csv')
    states_data = data.get('state').to_numpy()

    if len(states_guessed) == 50:
        game_is_on = False

    if answer_state == 'Exit':
        break

    if answer_state in states_data and answer_state not in states_guessed:
        score += 1
        states_guessed.append(answer_state)
        state_row = data[data.state == answer_state]
        written_state.write(f'{answer_state}', align='center', font=('Courier', 11, 'bold'))

states_data = states_data.tolist()
states_to_learn = list(set(states_data) - set(states_guessed))
states_to_learn_dic = {'states': states_to_learn}
df = pandas.DataFrame(states_to_learn_dic)
df.to_csv('states_to_learn.csv')


