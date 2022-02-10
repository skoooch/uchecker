"""
Routes and views for the flask application.
"""
import flask
from datetime import datetime
from flask import render_template, request
from ucheck import app
print(flask.__version__)

@app.route('/')
@app.route('/data/') 
def data():
    return render_template('about.html')

@app.route('/home', methods = ['POST', 'GET'])
def home():
    """Renders the home page."""
    from datetime import date, datetime
    day = date.today().strftime("%B %d, %Y")
    time = datetime.now().strftime("%I:%M %p")
    form_data = request.form.values()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        date=day,
        time=time,
        name = list(form_data)[0]
    )


