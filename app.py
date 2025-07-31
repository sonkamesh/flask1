from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():  # put application's code here
    return render_template('índex.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/day1')
def day1():
    return render_template('day1.html')


if __name__ == '__main__':
    app.run()
