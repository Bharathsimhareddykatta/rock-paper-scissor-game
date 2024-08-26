from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_choice = request.form['choice']
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            result = "You win!"
        else:
            result = "You lose!"

        return render_template('index.html', user_choice=user_choice, computer_choice=computer_choice, result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
