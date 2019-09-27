import os
import secrets
from PIL import Image
from flask import render_template, session, redirect, url_for, escape, request, flash
from dragonb_game import app, db, bcrypt
from dragonb_game.forms import RegistrationForm, LoginForm, UpdateAccountForm
from dragonb_game.models import User
from dragonb_game import planisphere, lexicon, parser
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def index():
    # this is used to "setup" the session with starting values
    session['room_name'] = planisphere.START
    session['player_health'] = planisphere.Player().health
    session['enemy_name'] = ""
    session['enemy_health'] = 100
    session['boxmap_counts'] = 0
    session['dragon_balls'] = 0

    # if logged user
    if current_user.is_authenticated:
        session['score'] = current_user.score
    # if playing as a guess
    else:
        session['score'] = 0

    return redirect(url_for("home"))

# HOME PAGE
@app.route("/home")
def home():
    return render_template("home.html")


# GAME
@app.route("/game", methods=['GET', 'POST'])
def game():
    # Sessions' key values
    room_name = session.get('room_name')
    p_name = planisphere.Player().name
    p_health = session.get('player_health')
    e_health = session.get('enemy_health')
    e_name = session.get('enemy_name')
    boxmap_counts = session.get('boxmap_counts')
    dragon_balls = session.get('dragon_balls')

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room, p_name=p_name, p_health=p_health,
                                   e_name=e_name, e_health=e_health, boxmap_counts=boxmap_counts,
                                   dragon_balls=dragon_balls)
        else:
            pass

    else:
        # request inputed data in client's side web page.
        word_list = lexicon.scan(request.form.get('action'))
        action = parser.parse_sentence(word_list).__str__()

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

            while room_name == "map_world" and action != "123":
                if boxmap_counts < 3:
                    session['boxmap_counts'] += 1
                    break
                else:
                    break

            if not next_room:
                if room_name == "map_world" and boxmap_counts == 2:
                    next_room = room.go("*")
                    session['room_name'] = planisphere.name_room(next_room)

                elif room_name in ["freezas_grounds", "cell_world", "majinbu_grounds", "synshenron"]:
                    p_health, e_health = planisphere.combat(p_health, e_health)
                    session['player_health'] = p_health
                    session['enemy_health'] = e_health
                    session['room_name'] = planisphere.name_room(room)

                    if e_health < 10 and room_name == "synshenron":
                        session['dragon_balls'] += 1
                        next_room = room.go('player next play')
                        session['room_name'] = planisphere.name_room(next_room)

                    elif p_health < 10:
                        next_room = room.go('*')
                        session['room_name'] = planisphere.name_room(next_room)
                        # Reseting health values for next fight
                        session['player_health'] = 100
                        session['enemy_health'] = 100

                    elif e_health < 10:
                        session['dragon_balls'] += 2
                        next_room = room.go('player next play')
                        session['room_name'] = planisphere.name_room(next_room)
                        # Reseting health values for next fight
                        session['player_health'] = 100
                        session['enemy_health'] = 100
                else:
                    # Go back to the same room
                    session['room_name'] = planisphere.name_room(room)

            else:
                # Go to next room
                session['room_name'] = planisphere.name_room(next_room)
                # And set enemy's name
                e_name = planisphere.load_room(session['room_name'])
                session['enemy_name'] = e_name.character

        # Back to /game url function
        return redirect(url_for("game"))




# REGISTER/CREATE ACCOUNT
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)

# LOGIN METHOD
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template("login.html", title='Login', form=form)

# LOGOUT METHOD
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


# ACCOUNT 
@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
            current_user.username = form.username.data
            current_user.email = form.email.data
            db.session.commit()
            flash('Your account has been updated!', 'success')
            return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template("account.html", title='Account', 
                            image_file=image_file, form=form)

# ABOUT
@app.route("/about")
def about():
    return render_template("about.html", title='About')

# GAME HELP
@app.route("/help")
def help():
    room_name = session.get('room_name')
    room = planisphere.load_room(room_name)
    return render_template("help.html", room=room)



