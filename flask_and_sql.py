from flask import Flask, request
import sqlite3
from db import get_db
from parse_query import parse_query

app = Flask(__name__)


def count_of_names() -> int:
    req = get_db("SELECT FirstName FROM Customers;")
    res = len(set(req))
    return res


def count_of_tracks() -> int:
    req = get_db("SELECT TrackId FROM tracks;")
    res = len(req)
    return res


def track_long() -> str:
    req = get_db("SELECT Name, Milliseconds FROM tracks;")
    res = ""
    for track in req:
        res += f'{track[0]} - {str(track[1] / 1000)}; '
    return res


def filter_db():
    if 'filter' in request.args:
        filter = request.args.get('filter')
        return str(get_db(parse_query(filter)))
    else:
        return str(get_db("SELECT * FROM Customers"))

@app.route('/names/')
def names():
    return str(count_of_names())


@app.route('/tracks/')
def tracks():
    return str(count_of_tracks())


@app.route('/tracks_seconds/')
def tracks_seconds():
    return track_long()


@app.route('/customers/')
def customers():
    return filter_db()



if __name__ == '__main__':
    app.run()
