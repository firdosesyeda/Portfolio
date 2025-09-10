# Portfolio
# Portfolio Website (Flask + SQLite)

This is a personal portfolio website built with **Flask** and **SQLite**.  
It includes pages for education, skills, projects, experience, certifications, and a contact form that stores messages in a database.

---

## 🚀 Features
- Home page with portfolio introduction
- Pages for:
  - Education
  - Skills
  - Projects
  - Experience
  - Certifications
- Contact form (saves messages into SQLite database)
- Admin page to view submitted messages
- Database auto-initialization from `schema.sql`

---

## 🛠️ Tech Stack
- [Flask](https://flask.palletsprojects.com/) (Python web framework)
- [SQLite](https://www.sqlite.org/index.html) (lightweight database)
- HTML templates with Jinja2
- Static files (CSS, JS, Images)

---

## 📂 Project Structure
Portfolio/
│── flask/
│ ├── app.py # Flask app
│ ├── portfolio.db # SQLite database (auto-created)
│ ├── schema.sql # Database schema
│ ├── static/ # CSS, JS, images
│ └── templates/ # HTML templates
│── venv/ # Python virtual environment

**Create & activate virtual environment**
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate

**Install dependencies**
pip install flask
(If you add more libraries later, update requirements.txt using
pip freeze > requirements.txt)

**Run the app**
python app.py

**Open in browser**
http://127.0.0.1:5000/
