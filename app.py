from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():  # put application's code here
    return render_template('índex.html')


if __name__ == '__main__':
    app.run()
