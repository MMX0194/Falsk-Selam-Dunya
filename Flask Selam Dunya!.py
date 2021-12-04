from flask import Flask

app = Flask(__name__)


@app.route('/')
def SelamDunya():
    return '<h1>Selam Dunya!</h1>'