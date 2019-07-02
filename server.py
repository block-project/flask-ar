from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def get_index():
    return render_template('index.html')

@app.route("/flag")
def get_flag():
    return render_template('flag.html')

app.run(host='0.0.0.0')

