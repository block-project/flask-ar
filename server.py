from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/keyboard")
def keyboard():
    return render_template('keyboard.html')

app.run(host='0.0.0.0')

