from datetime import datetime, time
from api import createApp, getSocket
from flask import render_template
import googlemaps
import json

#from flask_sqlalchemy import SQLAlchemy


app = createApp()
socketIO = getSocket()
    # add database
#app.app_context().push()
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C:\\Developer\\Website\\moveables_app_backend_python2\\moveables_app_backend_python\\test.db'

#db = SQLAlchemy(app)
#class Users(db.Model):
#    key = db.Column(db.Integer, primary_key=True)
#    id = db.Column(db.String(80), unique=True, nullable=False)
#    password = db.Column(db.String(80), unique=True, nullable=False)
#    email = db.Column(db.String(120), unique=True, nullable=False)
#
#    def __repr__(self):
#        return f"User(id = {self.id}, password = {self.password}, email = {self.email}"

@app.route('/maps')
def index():
    return render_template('loc.html')

@socketIO.on('data')
def handle_data(data):
    pickup = data["pickup"]
    dropoff = data["dropoff"]
    dispatch = data["dispatch"]

    gmaps = googlemaps.Client(key="AIzaSyDON3DiK7aYG444F6W9OhNxC4Z6Uy5REXU")

    # get directions with google maps
    directions_pickup = gmaps.directions(dispatch, pickup)
    directions_dropoff = gmaps.directions(dispatch, dropoff)
    
    # save directions to files
    with open("pickup.json", 'w') as p:
        json.dump(directions_pickup, p)

    with open("dropoff.json", 'w') as d:
        json.dump(directions_dropoff, d)

    socketIO.emit("message", "generated directions file")

if __name__ == '__main__':
    socketIO.run(app, debug=True)
