import db


def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes


def add_workout(title, description, user_id, classes):

    sql = """INSERT INTO workouts (title, description, user_id)
    VALUES (?, ?, ?)"""
    db.execute(sql, [title, description, user_id])

    sql = "INSERT INTO workout_classes (workout_id, title, value) VALUES (?,?,?)"

    workout_id = db.last_insert_id()

    for title, value in classes:
        db.execute(sql, [workout_id, title, value])


def get_workouts():
    sql = "SELECT id, title FROM workouts ORDER BY id DESC"
    return db.query(sql)


def get_classes(workout_id):
    sql = "SELECT title, value FROM workout_classes WHERE workout_id = ?"
    return db.query(sql, [workout_id])


def get_workout(workout_id):
    sql = """SELECT
    w.id,
    w.title,
    w.description,
    u.username,
    u.id AS user_id
    FROM workouts AS w
    LEFT JOIN users AS u ON w.user_id  = u.id
    WHERE w.id = ?"""
    result = db.query(sql, [workout_id])
    return result[0] if result else None


def update_workout(workout_id, title, description):
    sql = """UPDATE workouts SET
    title=?,
    description=?
    WHERE id = ?"""
    db.execute(sql, [title, description, workout_id])


def remove_workout(workout_id):
    sql = "DELETE FROM workouts WHERE id = ?"
    db.execute(sql, [workout_id])


def find_workout(query):
    sql = """SELECT id, title
    FROM workouts
    WHERE title LIKE ? OR description LIKE ?
    ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])
