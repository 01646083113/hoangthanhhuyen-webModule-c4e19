from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return ("Sử dụng render_template ")

@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight, height):
    bmi = weight/((height*height)*(10**(-4)))
    return render_template('index.html', bmi=bmi)


if __name__ == '__main__':
    app.run(debug = True)