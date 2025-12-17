
# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret")  # needed for flash messages

db = SQLAlchemy(app)

# --- Model ---
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.Text, nullable=False, default='Pending')  # 'Pending' or 'Completed'
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# --- Home: list tasks ---
@app.route('/')
def home():
    status_filter = request.args.get('status', 'all')
    query = Task.query.order_by(Task.created_at.desc())
    if status_filter in ('Pending', 'Completed'):
        query = query.filter_by(status=status_filter)
    tasks = query.all()
    counts = {
        'all': Task.query.count(),
        'pending': Task.query.filter_by(status='Pending').count(),
        'completed': Task.query.filter_by(status='Completed').count(),
    }
    return render_template('index.html', tasks=tasks, counts=counts, status_filter=status_filter)

# --- Create ---
@app.route('/tasks', methods=['POST'])
def create_task():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    if not title:
        flash("Title is required.", "error")
        return redirect(url_for('home'))
    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()
    flash("Task added.", "success")
    return redirect(url_for('home'))

# --- Complete ---
@app.route('/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.status = 'Completed'
    db.session.commit()
    flash("Task marked as completed.", "success")
    return redirect(url_for('home'))

# --- Reopen ---
@app.route('/tasks/<int:task_id>/reopen', methods=['POST'])
def reopen_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.status = 'Pending'
    db.session.commit()
    flash("Task reopened.", "info")
    return redirect(url_for('home'))

# --- Delete ---
@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted.", "warning")
    return redirect(url_for('home'))

# --- Edit (GET: show form, POST: save changes) ---
@app.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        if not title:
            flash("Title is required.", "error")
            return redirect(url_for('edit_task', task_id=task.id))
        task.title = title
        task.description = description
        db.session.commit()
        flash("Task updated.", "success")
        return redirect(url_for('home'))
    # GET: render a simple edit page (or you can build a modal later)
    return render_template('edit.html', task=task)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
