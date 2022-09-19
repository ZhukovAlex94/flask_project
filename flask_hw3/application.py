from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs
from utils import get_rate

app = Flask(__name__)


@app.route('/rates')
@use_kwargs(
    {
        'currency': fields.Str(required=True)
    },
    location='query'
)
def search_currency(currency):
    return {'rate': get_rate(currency)}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
