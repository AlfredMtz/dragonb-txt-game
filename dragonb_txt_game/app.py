from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
import planisphere

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

# YOU SHOULD CHANGE THIS IF YOU PUT ON THE INTERNET
app.secret_key = 'AOZr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run()