from flask import Flask, render_template, jsonify
from flask_mongoengine import MongoEngine
import requests

db = MongoEngine()

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'Movies'
}
db.init_app(app)


@app.route('/')
def hello_world():
    return render_template("test.html")


@app.route('/new')
def new_function():
    res = requests.get("https://itunes.apple.com/search?term=michael+jackson")
    return jsonify(res.json())


if __name__ == '__main__':
    app.run()
