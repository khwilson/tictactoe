"""
The actual web application

@author Kevin Wilson - khwilson@gmail.com
"""
from flask import Flask, render_template, request

app = Flask(__name__)


def __check_winner(status, letter):
    """
    Given a dict a la _check_win, return letter if letter has a winning
    tic tac toe configuration. Else return None.

    :param dict[str, str] status: The status of the game
    :param str letter: Which letter to check if it has won
    :return: letter if letter has won, else None
    :rtype: str | None
    """
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
    """
    Check if either X or O has a winning configuration. ``status`` should be a
    dict wich keys of the form ``ij`` where ``i`` is the row number and ``j`` is
    the column number (starting from 0). The values should be either ``X``, ``O``,
    or simply the empty string.

    :param dict[str, str] status: The status of the game
    :return: The winner, or None if there is none yet
    :rtype: str | None
    """
    for letter in ('X', 'O'):
        stat = __check_winner(status, letter)
        if stat: return stat
    return None


@app.route("/")
def home():
    """
    Just a simple greeting page
    """
    return render_template("hello.html")


@app.route("/play.html", methods=["GET", "POST"])
def play():
    """
    Actually play a game. GET starts a game and POST plays it.
    """
    if request.method == 'GET':
        return render_template("play.html",
                               status={'%d%d' % (i, j): '' for i in xrange(3) for j in xrange(3)},
                               turn='X')
    else:
        status = {'%d%d' % (i, j): request.form['%d%d' % (i, j)] for i in xrange(3) for j in xrange(3)}
        turn = 'X' if request.form['turn'] == 'O' else 'O'
        win = _check_win(status)
        # Status can be: There's a winner, there's not a winner and there are free squares, or cat.
        if win:
            return render_template("win.html", status=status, winner=win)
        else:
            if all(status.itervalues()):
                return render_template("win.html", status=status, winner="No one")
            else:
                return render_template("play.html", status=status, turn=turn)
