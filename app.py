import sqlite3
from flask import Flask
from flask import abort, redirect, flash, render_template, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import config
import db
import workouts
import users
import re

app = Flask(__name__)
app.secret_key = config.secret_key


def require_login():
    if "user_id" not in session:
        abort(403)


@app.route("/")
def index():
    all_workouts = workouts.get_workouts()
    return render_template("index.html", workouts=all_workouts)


@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        return abort(404)
    workouts = users.get_workouts(user_id)
    return render_template("show_user.html", user=user, workouts=workouts)


@app.route("/find_workout")
def find_workout():
    query = request.args.get("query")
    if query:
        if re.fullmatch(r"[^\w\s]", query):
            abort(403)
        results = workouts.find_workout(query)
    else:
        query = ""
        results = []
    return render_template("find_workout.html", query=query, results=results)


@app.route("/workout/<int:workout_id>")
def show_workout(workout_id):
    workout = workouts.get_workout(workout_id)
    if not workout:
        return abort(404)
    return render_template("show_workout.html", workout=workout)


@app.route("/new_workout")
def new_workout():
    return render_template("new_workout.html")


@app.route("/create_workout", methods=["POST"])
def create_workout():
    require_login()

    title = request.form["title"]
    if not title or len(title) > 50:
        abort(403)
    muscle_groups = request.form["muscle_groups"]
    if not muscle_groups or len(muscle_groups) > 500:
        abort(403)
    goals = request.form["goals"]
    if not goals or len(goals) > 500:
        abort(403)
    description = request.form["description"]
    if not description or len(description) > 1000:
        abort(403)
    user_id = session["user_id"]

    workouts.add_workout(title, muscle_groups, goals, description, user_id)

    return redirect("/")


@app.route("/edit_workout/<int:workout_id>")
def edit_workout(workout_id):
    require_login()
    workout = workouts.get_workout(workout_id)
    if not workout:
        return abort(404)
    if workout["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_workout.html", workout=workout)


@app.route("/update_workout", methods=["POST"])
def update_workout():
    require_login()
    workout_id = request.form["workout_id"]
    workout = workouts.get_workout(workout_id)

    if not workout:
        return abort(404)

    if workout["user_id"] != session["user_id"]:
        abort(403)

    title = request.form["title"]
    if not title or len(title) > 50:
        abort(403)
    muscle_groups = request.form["muscle_groups"]
    if not muscle_groups or len(muscle_groups) > 500:
        abort(403)
    goals = request.form["goals"]
    if not goals or len(goals) > 500:
        abort(403)
    description = request.form["description"]
    if not description or len(description) > 1000:
        abort(403)

    workouts.update_workout(workout_id, title, muscle_groups, goals, description)

    return redirect("/workout/" + str(workout_id))


@app.route("/remove_workout/<int:workout_id>", methods=["GET", "POST"])
def remove_workout(workout_id):
    require_login()
    workout = workouts.get_workout(workout_id)
    if not workout:
        return abort(404)
    if workout["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
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

        user_id = users.check_login(username, password)

        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            flash("ERROR: wrong username or password")
            return redirect("/login")


@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["username"]
        del session["user_id"]
    return redirect("/")
