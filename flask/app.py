from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'portfolio.db')
SCHEMA_PATH = os.path.join(BASE_DIR, 'schema.sql')

app = Flask(__name__)
app.config['DATABASE'] = DB_PATH
app.config['SECRET_KEY'] = 'replace-this-with-a-secure-key'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = sqlite3.Row
    return db

def init_db():
    if not os.path.exists(app.config['DATABASE']):
        with app.app_context():
            db = get_db()
            with open(SCHEMA_PATH, 'r', encoding='utf8') as f:
                db.executescript(f.read())
            db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# initialize DB on first run
init_db()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not message:
            return render_template('contact.html', error="Please fill all fields.", name=name, email=email, message=message)

        db = get_db()
        db.execute('INSERT INTO messages (name, email, message) VALUES (?, ?, ?)', (name, email, message))
        db.commit()
        return render_template('contact.html', success="Message sent! Thank you.", name='', email='', message='')

    return render_template('contact.html')

@app.route('/messages')
def messages():
    # This is a simple admin view (no auth). Add auth in future if needed.
    db = get_db()
    cur = db.execute('SELECT id, name, email, message, created_at FROM messages ORDER BY created_at DESC')
    msgs = cur.fetchall()
    return render_template('messages.html', messages=msgs)

if __name__ == '__main__':
    app.run(debug=True)
