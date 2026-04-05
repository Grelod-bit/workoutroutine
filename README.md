# Workout Routine

* Users can create an account and log in to the application.

* Users can add workout routines. Additionally, users can edit and delete the routines they have created.
  
* Users can view all workout routines added to the application, including their own and those added by other users.

* Users can search for workout routines, muscle groups, goals, or equipment using keywords. This search applies to both the user’s own routines and those created by others.
  
* The application includes user profile pages that display statistics for each user and a list of the workout routines they have added.

* Users can assign one or more classifications (tags) to a routine. The available categories (e.g., muscle group, goal, equipment) are stored in the database.
  
* The application allows users to rate workout routines, leave comments, and view the date the comment was posted.

## Installing the application

> [!NOTE]
> This application is stable on Python **3.13+**.

> [!IMPORTANT]
> Ensure you have [Python](https://www.python.org/downloads/) and [SQLite](https://sqlite.org/download.html) installed on your computer before proceeding!

> [!TIP]
> **For Linux users:** You typically need to install the `venv` module separately. Run:
> ```bash
> sudo apt install python3-venv
> ```

### Clone this repository on your local machine
```bash
git clone git@github.com:Grelod-bit/workoutroutine.git
```
### Setup the Virtual Environment

**1. Create the Venv:**
```bash
python3 -m venv venv
```

**2. Initiate Venv:**

**Linux/MacOS:**
```bash
source venv/bin/activate
```
**Windows PowerShell:**
```bash
.\venv\Scripts\Activate.ps1
```
> [!NOTE]
> If you get a script execution error, try running **PowerShell** as an administrator and use the following command:

```bash
Set-ExecutionPolicy RemoteSigned
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
