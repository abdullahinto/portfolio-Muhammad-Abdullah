from flask import render_template, request, redirect, url_for, flash
from . import app, db
from .models import TextModel

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        new_text = TextModel(name=name, email=email, message=message)
        db.session.add(new_text)
        db.session.commit()
        flash('Feedback submitted to Muhammad Abdullah', 'success')
        return redirect(url_for('home'))
