from flask import Flask, render_template, request, redirect

class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

game1 = Game('Tetris', 'Puzzle', 'Super Nintendo')
game2 = Game('Super Mario', 'Action', 'Super Nintendo')
game3 = Game('Mortal Kombat', 'Fight', 'PS2')
game4 = Game('Skyrim', 'RPG', 'PC')
list = [game1, game2, game3,game4]

app = Flask(__name__)

# ------------------------------------------------- Pages ----------------------------------------------------------------
@app.route('/')
def index():
    # gamesList = [,'Skyrim','Minecraft','GTA V','The Witcher 3','Crash','God Of War','Valorant']
    return render_template('gameTable.html', title='Games', games=list)

@app.route('/new')
def new():
    return render_template('register.html', title='Register A New Game')

# ------------------------------------------------- Methods ----------------------------------------------------------------
@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    category = request.form['category']
    plataform = request.form['plataform']
    game = Game(name, category, plataform)
    list.append(game)
    return redirect('/')

app.run(debug=True)