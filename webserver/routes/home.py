from flask import Blueprint, render_template

app = Blueprint('home', __name__)

@app.route('/')
def home():
    return render_template('index.html')