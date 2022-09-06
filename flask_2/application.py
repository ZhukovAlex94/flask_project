from flask import Flask
import sqlite3

app = Flask(__name__)


def get_connection():
    conn = sqlite3.connect('example.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/best_selling/<int:track_count>')
def best_selling(track_count):
    conn = get_connection()
    tracks = conn.execute('SELECT invoice_items.TrackId, tracks.Name, SUM(invoice_items.UnitPrice *'
                          ' invoice_items.Quantity) FROM invoice_items INNER JOIN tracks ON invoice_items.TrackId ='
                          ' tracks.TrackId GROUP BY invoice_items.TrackId'
                          ' ORDER BY SUM(invoice_items.UnitPrice * invoice_items.Quantity) DESC LIMIT ?',
                          [track_count]).fetchall()
    conn.close()

    return [{"track_id": track_id, 'track_name': track_name, 'sells': sells} for track_id, track_name, sells in tracks]


app.run(debug=True, port=5050)
