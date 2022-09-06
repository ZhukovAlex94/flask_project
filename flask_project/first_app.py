from flask import Flask

from avr_data import get_avr_data as calc_avr_data
from requirements import requirements as requirement

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def hello():
    return '<h1>Hello World!</h1><br>'


@app.route('/get_avr_data')
def get_avr_data():
    avg_height, avg_weight = calc_avr_data()
    return f"Average height: {avg_height} cm <br> Average weight: {avg_weight} kg"


@app.route('/requirements')
def requirements():
    return requirement().replace('\n', '<br>')


if __name__ == "__main__":
    app.run(debug=True)
