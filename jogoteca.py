from flask import Flask, render_template, request, redirect, session, flash

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
app.secret_key = 'criptografia'

# ------------------------------------------------- Pages ----------------------------------------------------------------
@app.route('/')
def index():
    # gamesList = [,'Skyrim','Minecraft','GTA V','The Witcher 3','Crash','God Of War','Valorant']
    return render_template('gameTable.html', title='Games', games=list)

@app.route('/new')
def new():
    return render_template('register.html', title='Register A New Game')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

# ------------------------------------------------- Methods ----------------------------------------------------------------
@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    category = request.form['category']
    plataform = request.form['plataform']
    game = Game(name, category, plataform)
    list.append(game)
    return redirect('/')

@app.route('/auth', methods=['POST'])
def auth():
    user = request.form['user']
    password = request.form['password']
    if user == 'admin' and password == 'admin':
        session['logged_user'] = request.form['user']
        flash(session['logged_user'] + ' Logged successfully!')
        return redirect('/')
    else:
        flash('Invalid user or password! Try again!')
        return redirect('/login')
    
@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('No user logged!')
    return redirect('/')

app.run(debug=True)