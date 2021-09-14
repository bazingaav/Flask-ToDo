from flask import Flask

#Convention
app = Flask(__name__)

#Define index page
@app.route('/')
def index():
    return "Hello Earthlings!"


if __name__ == "__main__":
    app.run(debug=True)
