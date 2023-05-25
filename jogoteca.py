from flask import Flask, render_template

class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

app = Flask(__name__)

@app.route('/')
def home():
    game1 = Game('Tetris', 'Puzzle', 'Super Nintendo')
    game2 = Game('Super Mario', 'Action', 'Super Nintendo')
    game3 = Game('Mortal Kombat', 'Fight', 'PS2')
    list = [game1, game2, game3]

    # gamesList = ['Tetris','Skyrim','Minecraft','GTA V','The Witcher 3','Crash','God Of War','Valorant']
    return render_template('gameTable.html', title='Games', games=list)

@app.route('/new')
def new():
    return render_template('register.html', title='New Game')

app.run()