from flask import Flask

# экземпляр Flask-приложения
app = Flask(__name__)


@app.route("/")
def create_app():
    return "hello"
