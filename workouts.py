import db


def add_workout(title, muscle_groups, goals, description, user_id):

    sql = """INSERT INTO workouts (title, muscle_groups, goals, description, user_id)
    VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [title, muscle_groups, goals, description, user_id])


def get_workouts():
    sql = "SELECT id, title FROM workouts ORDER BY id DESC"
    return db.query(sql)


def get_workout(workout_id):
    sql = """SELECT
    w.id,
    w.title,
    w.muscle_groups,
    w.goals,
    w.description,
    u.username,
    u.id AS user_id
    FROM workouts AS w
    LEFT JOIN users AS u ON w.user_id  = u.id
    WHERE w.id = ?"""
    return db.query(sql, [workout_id])[0]


def update_workout(workout_id, title, muscle_groups, goals, description):
    sql = """UPDATE workouts SET
    title=?,
    muscle_groups =?,
    goals=?,
    description=?
    WHERE id = ?"""
    db.execute(sql, [title, muscle_groups, goals, description, workout_id])
