from flask import Flask, render_template, request, redirect, url_for 
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
    #Show all todos
    todo_list = Todo.query.all()
    print(todo_list)
    #using jinja template engine
    return render_template('index.html', todo_list=todo_list)

#About page
@app.route('/about')
def about():
    return "This is about page"


#this route won't ever be used- as the job of this function is to add new values to the db
#Byt the route needs to be defined
@app.route('/add', methods=["POST"])
def add():
    #Add new item
    title = request.form.get("title")
    new_todo = Todo(title= title, isComplete=False)
    db.session.add(new_todo)
    db.session.commit()
    #Refresh the page - redirect
    return redirect(url_for("index"))

#update record: complete <-> not-complete
@app.route('/update/<int:todo_id>')
def update(todo_id):
    #Update existing item
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.isComplete = not todo.isComplete
    db.session.commit()
    return redirect(url_for("index"))

#delete record
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    #Update existing item
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
