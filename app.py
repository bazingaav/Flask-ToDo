from flask import Flask

#Convention
app = Flask(__name__)

#Define index page
@app.route('/')
def index():
    return "Hello Earthlings!"

#About page
@app.route('/about')
def about():
    return "This is about page"


if __name__ == "__main__":
    app.run(debug=True)
