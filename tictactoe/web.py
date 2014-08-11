from flask import Flask, render_template, request

app = Flask(__name__)


def __check_winner(status, letter):
    for i in xrange(3):
        if all(status['%d%d' % (i, j)] == letter for j in xrange(3)):
            return letter
    for j in xrange(3):
        if all(status['%d%d' % (i, j)] == letter for i in xrange(3)):
            return letter
    if all(status['%d%d' % (i, i)] == letter for i in xrange(3)):
        return letter
    if all(status['%d%d' % (i, 2 - i)] == letter for i in xrange(3)):
        return letter
    return None


def _check_win(status):
    for letter in ('X', 'O'):
        stat = __check_winner(status, letter)
        if stat: return stat
    return None


@app.route("/")
def home():
    return render_template("hello.html")


@app.route("/play.html", methods=["GET", "POST"])
def play():
    if request.method == 'GET':
        return render_template("play.html",
                               status={'%d%d' % (i, j): '' for i in xrange(3) for j in xrange(3)},
                               turn='X')
    else:
        status = {'%d%d' % (i, j): request.form['%d%d' % (i, j)] for i in xrange(3) for j in xrange(3)}
        turn = 'X' if request.form['turn'] == 'O' else 'O'
        win = _check_win(status)
        if win:
            return render_template("win.html", status=status, winner=win)
        else:
            return render_template("play.html", status=status, turn=turn)
