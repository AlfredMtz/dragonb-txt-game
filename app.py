from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
import planisphere
import os

from flask import Flask
app = Flask(__name__)


# routes browser url link extension "/" to the below function
@app.route("/")
def index():
    # this is use to "setup" the session with starting values
    session['room_name'] = planisphere.START
    # generates url for game() function and redirects users to the game page
    return redirect(url_for("game"))


@app.route("/game", methods=['GET', 'POST'])
def game():
    # Saves value from given key in diccionary{"key": 'value'}
    room_name = session.get('room_name')
    # IF METHOD = "GET", RUN THIS BLOCK(Standard starting method
    # is 'GET')
    if request.method == "GET":
        # room_name = 'intro'
        # if statements seems unnecessary.
        if room_name:
            # saves Room() object ---> Intro
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            # why is there here? do I need it?
            return render_template("you_died.html")

    # eLSE IF METHOD = "POST", THEN RUN THIS BLOCK
    else: 
        action = request.form.get('action')

        if room_name == 'intro':
            room = planisphere.load_room(room_name)
            next_room = room.go(action)
            #pdb.set_trace() 
            if not next_room:
                # save session 'room_name' key  value to current 'room' variable
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)


    return redirect(url_for("game"))

# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = os.environ.get('MY_DBTXT_GAME_KEY')

if __name__ == "__main__":
    app.run() 