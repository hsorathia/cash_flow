from flask import Flask, render_template
from login import loginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-key'

@app.route("/")

def hello():
    form = loginForm()
    return render_template('index.html', form = form)


app.run()