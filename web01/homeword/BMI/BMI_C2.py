from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return ('em lại chào a Quý :v nếu web không chạy thì a vào atom bỏ cmt nhá :)))')

@app.route('/bmi/<int:weight>/<int:height>')
def calc(weight, height):
    BMI = weight/((height*height)*(10**(-4)))
    return render_template('index.html', BMI=BMI)


if __name__ == '__main__':
    app.run(debug = True)