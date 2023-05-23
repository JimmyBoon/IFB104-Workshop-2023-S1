from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def root():
    return '<h1>Hello, World!</h1>'

@app.route('/page')
def page():

    return render_template("index.html", content="nothing")

@app.route('/json')
def my_json():
    return json.dumps({"message":"This is the message"})

@app.route('/hello/<name>')
def hello(name):
    if name == "on":
        print("Swith on the light")
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(app.run(host= '0.0.0.0', port=8000, debug=False))