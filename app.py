from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my Flask app!"

@app.route("/about")
def about():
    return "This is a simple Flask application with two routes. toutes"

if __name__ == "__main__":
    app.run(debug=True)
