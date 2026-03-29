CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);


CREATE TABLE workouts (
    id INTEGER PRIMARY KEY,
    title TEXT,
    muscle_groups TEXT,
    goals TEXT,
    description TEXT,
    user_id INTEGER REFERENCES users
);


