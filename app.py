import sqlite3
from flask import Flask
from flask import redirect, flash, render_template, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import config
import db
import workouts
import users

app = Flask(__name__)
app.secret_key = config.secret_key


@app.route("/")
def index():
    all_workouts = workouts.get_workouts()
    return render_template("index.html", workouts=all_workouts)


@app.route("/find_workout")
def find_workout():
    query = request.args.get("query")

    if query:
        results = workouts.find_workout(query)
    else:
        query = ""
        results = []
    return render_template("find_workout.html", query=query, results=results)


@app.route("/workout/<int:workout_id>")
def workout(workout_id):
    workout = workouts.get_workout(workout_id)
    return render_template("show_workout.html", workout=workout)


@app.route("/new_workout")
def new_workout():
    return render_template("new_workout.html")


@app.route("/create_workout", methods=["POST"])
def create_workout():
    title = request.form["title"]
    muscle_groups = request.form["muscle_groups"]
    goals = request.form["goals"]
    description = request.form["description"]
    user_id = session["user_id"]

    workouts.add_workout(title, muscle_groups, goals, description, user_id)

    return redirect("/")


@app.route("/edit_workout/<int:workout_id>")
def edit_workout(workout_id):
    workout = workouts.get_workout(workout_id)
    return render_template("edit_workout.html", workout=workout)


@app.route("/update_workout", methods=["POST"])
def update_workout():
    workout_id = request.form["workout_id"]
    title = request.form["title"]
    muscle_groups = request.form["muscle_groups"]
    goals = request.form["goals"]
    description = request.form["description"]

    workouts.update_workout(workout_id, title, muscle_groups, goals, description)

    return redirect("/workout/" + str(workout_id))


@app.route("/remove_workout/<int:workout_id>", methods=["GET", "POST"])
def remove_workout(workout_id):
    if request.method == "GET":
        workout = workouts.get_workout(workout_id)
        return render_template("remove_workout.html", workout=workout)

    if request.method == "POST":
        if "remove" in request.form:
            workouts.remove_workout(workout_id)
            return redirect("/")
        else:
            return redirect("/workout/" + str(workout_id))


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        flash("ERROR: passwords not matching")
        return redirect("/register")

    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        flash("ERROR: Username already taken")
        return redirect("/register")

    return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username])[0]
        user_id = result["id"]
        password_hash = result["password_hash"]

        if check_password_hash(password_hash, password):
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "ERROR: wrong username or password"


@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["username"]
        del session["user_id"]
    return redirect("/")
