from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def testing1():
    return render_template('testing1.html')
