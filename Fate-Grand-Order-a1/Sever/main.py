import threading
import time
from random import randint

import socketio
import eventlet.wsgi
from flask import Flask, render_template

sio = socketio.Server()
app = Flask(__name__)

player_list = []
enemy_list = []


def roomloop():
    starttime = time.time() * 1000
    fighttime = starttime + 100
    while True:
        print starttime, fighttime, time.time() * 1000


t = threading.Thread(target=roomloop)
t.start()


@app.route('/')
def index():
    return render_template('index.html')


@sio.on('connect')
def connect(sid, environ):
    print sid + " connected"


@sio.on("user login")
def login(sid, data):
    pos = randint(0, 100), randint(100, 300)
    _data = {"pos": pos, "sid": sid}
    player_list.append(_data)
    data = {"list": player_list, "index": player_list.index(_data)}
    sio.emit("player list", data)
    if not enemy_list:
        pos = randint(0, 100), randint(100, 300)
        _data = {"pos": pos}
        enemy_list.append(_data)
    sio.emit("create enemy", enemy_list)


@sio.on("player move")
def player_pos(sid, data):
    for x in player_list:
        if x['sid'] == sid:
            x['pos'] = data['pos']
    sio.emit("player pos", data)


@sio.on("player fire")
def player_fire(sid, data):
    sio.emit("bullet", data)


@sio.on("enemy bullet")
def create_bullet(sid, data):
    sio.emit("create enemy bullet", data)


@sio.on('disconnect')
def disconnect(sid):
    for member in player_list:
        if member['sid'] == sid:
            player_list.remove(member)


if __name__ == '__main__':
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app)
