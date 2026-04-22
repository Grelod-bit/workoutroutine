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
    result = db.query(sql, [workout_id])
    return result[0] if result else None


def update_workout(workout_id, title, muscle_groups, goals, description):
    sql = """UPDATE workouts SET
    title=?,
    muscle_groups =?,
    goals=?,
    description=?
    WHERE id = ?"""
    db.execute(sql, [title, muscle_groups, goals, description, workout_id])


def remove_workout(workout_id):
    sql = "DELETE FROM workouts WHERE id = ?"
    db.execute(sql, [workout_id])


def find_workout(query):
    sql = """SELECT id, title
    FROM workouts
    WHERE title LIKE ? OR muscle_groups LIKE ? OR goals LIKE ?
    ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like, like])
