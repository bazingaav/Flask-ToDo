from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy

#Convention
app = Flask(__name__)
#Path for DB -/// -> relative path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)

#DB structure
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    isComplete = db.Column(db.Boolean)

#Define index page
@app.route('/')
def index():
    return render_template('index.html')

#About page
@app.route('/about')
def about():
    return "This is about page"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
