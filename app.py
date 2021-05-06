from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def testing2():
    return render_template("testing2.html")

if __name__ == '__main__':
    app.run(debug=True)
