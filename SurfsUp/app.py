# Import the dependencies.
from flask import Flask
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
# 10-3, activity 10
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)
measurement_data = session.query(measurement).all()
station_data = session.query(station).all()


#################################################
# Flask Setup
#################################################
# Create app
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Define what to do when a user hits the index route
@app.route("/")
def home():
    return (
        f"Welcome to the Hawaii weather app!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )

# -----------------------------------
# app route to precipitation data
@app.route("/api/v1.0/precipitation")
def precip():
    # create session link from Python to db
    session = Session(engine)

    # query for the last 12 months of data
    sel = [measurement.date, measurement.prcp]
    prcp_data = session.query(*sel).\
        filter(measurement.date >= '2016-08-23').\
        group_by(measurement.date).\
        order_by(measurement.date).all()
    
    # create a dictionary with the date as the key and the precipitation as they value
    precip_dict = {date: prcp for date, prcp in prcp_data}

    # close the session
    session.close()

    # return the JSON-ififed version of the dictionary
    return jsonify(precip_dict)

# -----------------------------------
@app.route("/api/v1.0/stations")
def stations():
    # create session link from Python to db
    session = Session(engine)

    # query for the list of stations
    # using query from climate_starter_ipynb for most active stations (includes all stations)
    stations = session.query(station.station).all()
    
    # create a list of the station IDs (help from Xpert Learning Assistant)
    station_list = [station[0] for station in stations]

    # close the session
    session.close()

    
    return jsonify(station_list)

# -----------------------------------
@app.route("/api/v1.0/tobs")
def temps():
    # create session link from Python to db
    session = Session(engine)

    # query dates and temp observations of most active station for the previous year of data
    # using query from climate_starter_ipynb for station, date, and temp data
    temp_obs = [measurement.tobs, measurement.date]

    # query for the temperature data for every day after 2016-08-23
    temp_data = session.query(*temp_obs).\
        filter(measurement.station == "USC00519281").\
        filter(measurement.date >= '2016-08-23').all()
    
    # close the session
    session.close()

    # return the JSON-ififed version of the list
    return jsonify(temp_data)
    
# -----------------------------------
# Dynamic Route (help from Xpert Learning Assistant)
# first, define a function that will query the db and compute the temperature statistics
def temp_calc(start_date, end_date=None):
    # create session link from Python to db
    session = Session(engine)

    # query to use temp and date data
    temp_obs = [measurement.tobs, measurement.date]

    # define tmin, tmax, tavg
    tmin = func.min(measurement.tobs).all()
    tmax = func.max(measurement.tobs).all()
    tavg = func.avg(measurement.tobs).all()

    # query to get the temp data and calculate it
    temps = session.query(*temp_obs).\
        tmin = func.min(measurement.tobs).all().\
        tmax = func.max(measurement.tobs).all().\
        tavg = func.avg(measurement.tobs).all()

    return {
        'TMIN': tmin,
        'TMAX': tmax,
        'TAVG': tavg
    }

# create route for temp calculations with a start date
@app.route("/api/v1.0/<start>")
def temp_by_start_date(start):
    temp_data = temp_calc(start)
    return jsonify(temp_data)

# create route for temp calculations within a date range
@app.route("/api/v1.0/<start>/<end>")
def temp_by_date_range(start,end):
    temp_data = temp_calc(start,end)
    return jsonify(temp_data)

# from 10-3 activity 04, define main behavior
# if __name__ == "__main__":
#     app.run(debug=True)