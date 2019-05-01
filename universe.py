from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def space():
    return render_template('space.html')


if __name__ == '__main__':
    app.run(debug=True)
