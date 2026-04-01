# Workout Routine

* Users can create an account and log in to the application.

* Users can add workout routines. Additionally, users can edit and delete the routines they have created.
  
* Users can view all workout routines added to the application, including their own and those added by other users.

* Users can search for workout routines, muscle groups, goals, or equipment using keywords. This search applies to both the user’s own routines and those created by others.
  
* The application includes user profile pages that display statistics for each user and a list of the workout routines they have added.

* Users can assign one or more classifications (tags) to a routine. The available categories (e.g., muscle group, goal, equipment) are stored in the database.
  
* The application allows users to rate workout routines, leave comments, and view the date the comment was posted.

## Installing the application
This application is stable on Python version 3.13.7.
> [!IMPORTANT]
> Make sure you also have 'python3' and 'venv environment' installed on your computer before proceeding.

### Installing Python on Windows: ###
* https://www.python.org/downloads/
* Install Python 3.13
* check the box that says "Add Python to PATH"

### Installing Python on Linux: ###
Installing `Python3` and `Venv`
```bash
sudo apt update
```
```bash
sudo apt install python3
```
```bash
sudo apt install python3-venv
```
### Installing Python on MacOS: ###
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```bash
brew install python
```

---

### Venv environment: ###

**Create the Environment:**
```bash
python3 -m venv venv
```

**Initiate Venv:**

Linux/MacOS:
```bash
source venv/bin/activate
```

Windows CMD:
```bash
venv\Scripts\activate.bat
```
---

Install `flask`-library:
```bash
pip install flask
```

Initiate database tables:
```bash
sqlite3 database.db < schema.sql
```

Start the application:
```bash
flask run
```
