import os
import secrets
from PIL import Image
from flask import render_template, session, redirect, url_for, escape, request, flash
from dragonb_game import app, db, bcrypt, mail
from dragonb_game.forms import (RegistrationForm, LoginForm, UpdateAccountForm, 
                                RequestResetForm, ResetPasswordForm)
from dragonb_game.models import User
from dragonb_game import planisphere, lexicon, parser
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


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
        if room_name == "game_finished":
            room = planisphere.load_room(room_name)
            current_user.score = current_user.score + 1
            db.session.commit()
            return render_template("show_room.html", room=room, p_name=p_name, p_health=p_health,
                                   e_name=e_name, e_health=e_health, boxmap_counts=boxmap_counts,
                                   dragon_balls=dragon_balls)
        elif room_name :
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
    # If user has successfully been logged in, redirect them to homepage
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    # Run the code if all of the information in the form gets validated in accordance with
    # all conditons
    if form.validate_on_submit():
        # Emcrypts user's password
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        # Persists user's new account data into our database
        db.session.add(user)
        db.session.commit()

        # Confirmation message about account creating and directs user to our login page
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    # Reroutes user back to current page is some of the inputted data did not get validated.
    return render_template("register.html", title='Register', form=form)


# LOGIN METHOD
@app.route("/login", methods=['GET', 'POST'])
def login():
    # If user has successfully been logged in, redirect them to homepage
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # If user exists and password matches within the database
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # if remember checkbox marked in the login page "remember" value will be True.
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            # if user logged in go to requested route, else go to home page
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

    # Resizing Image: Saving space on file system and speeding up website.
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


# ACCOUNT 
@app.route("/account", methods=['GET', 'POST'])
# login_required -- makes it requirement to be logged in before an user has access
# to this route content.
@login_required
def account():
    form = UpdateAccountForm()
    # If data update are valid, update the data as followed
    if form.validate_on_submit():
        # Saving/Persisting updated picture 
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        # Then update/persist username, email and picture to database
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))

    # Populating our form with the current user's data if user's new data does not
    # get validated/ is not allowed.
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

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', 
                sender='noreply@demo.com', 
                recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)



# Where users will request to reset their password
@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    # If user is logged in, take them back to their home page, otherwise
    # skip the lines of code and go to the reset request validation form.
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    #
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

# Actual place where users will reset their password
# When user goes to this url, the function will try to validate the "token" created
# under the reset_request() function above, and present under the reset_password url
@app.route("/reset_password<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    # If valid, it will return the user_id
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # Emcrypts user's password
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        # Persists user's new updated password into our database
        user.password = hashed_password
        db.session.commit()

        # Confirmation message about account creating and directs user to our login page
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
