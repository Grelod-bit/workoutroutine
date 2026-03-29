import db


def add_workout(title, muscle_groups, goals, description, user_id):

    sql = """INSERT INTO workouts (title, muscle_groups, goals, description, user_id)
    VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, muscle_groups, goals, description, user_id])
