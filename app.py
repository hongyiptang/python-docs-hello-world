from flask import Flask, render_template

# Referenciing this file
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('testing1.html')


if __name__ == "__main__":
    app.run(debug=True)
