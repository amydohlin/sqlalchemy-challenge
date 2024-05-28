# Import the dependencies.
from flask import Flask




#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


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

# @app.route("/api/v1.0/precipitation")
# # def precip():

# @app.route("/api/v1.0/stations")
# # def stations():

# @app.route("/api/v1.0/tobs")

# def temp():
# from 10-3 activity 04, define main behavior
# if __name__ == "__main__":
#     app.run(debug=True)