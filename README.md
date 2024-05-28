# sqlalchemy-challenge
Module 10 - SQL Alchemy


## Precipitation Analysis
### 1. Reflect Tables into SQL Alchemy ORM
- I used the imports and dependencies included in the starter file, but I did add the inspect import on my own.
- I created an engine that connnected to the provided hawaii.sqlite file, and used automap_base() to declare a base and `Base.prepare(autoload_with=engine)`  to reflect the database schema and generate the classes within it automatically.
- To get the classes, I utilized two methods:
  - `Base.classes.keys()` which displayed each table in the database ('measurement' and 'station')
  - `inspector = inspect(engine)` followed by `inspector.get_table_names()` that verified the tables.
- Then I saved the references to each table as measurement and station.
- Next I created the session that links Python to the database with:
  - `session = Session(engine)`
  - `measurement_data = session.query(measurement).all()`
  - `station_data = session.query(station).all()`
- My final preparation before exploratory analysis was to get a sample of the measurement data as a list of tuples, to ensure that I would be able to get the information needed for my queries, see figure 1.

   ![alt text]()

  Fig 1: sample data.

### 2. Exploratory Precipitation Analysis
* To find the most recent date in the dataset, I utililzed the `.order_by()` function with `.desc()` and `.first()`. The result was '2017-08-23'.
* To find the last 12 months of precipitation data, I used the `filter()` function on the measurement table to fetch all dates after 2016-08-23. Following this I defined a 'sel' variable that contained [measurement.date, measurement.prcp], and used that variable in the query that filtered for data on and after 2016-08-23, grouped it by date, and ordered it by date. Once this query ran, I saved the results in a dictionary named 'prcp_data' and turned it into a Pandas Dataframe, named 'prcp_df'. This dataframe was then sorted by date and saved as prcp_df_sorted.
* The next step was to plot the precipitation and dates after 2016-08-23, but I had trouble getting the plot to display properly, even with help from Xpert Learning Assistant, see figure 2.

  ![alt text]()

  Fig 2: failed precipitation plot.

* Finally, I used `.describe()` to generate the summary statistics for the precipitation data, see figure 3.

  ![alt text]()

  Fig 3: precipitation summary statistics

------------------------------------------------------
## Station Analysis (16 points)
* To find the total number of stations, I simply used the `.count()` function and found there are 9 stations.
* To find the most active stations, I designed a query that went through 'measurement.station' and used:
  * `func.count()` to count the number of rows per unique station,
  * `.group_by()` to group by unique station,
  * `.order_by().desc()` to list the most active station first,
  * `.all()` to list each one
* Following that query, I implemented a for loop to go through each station and its row count, and displaey the results, see figure 4.

  ![alt text]()

  Fig 4: most active stations.

* The next query was designed to find the minimun, maximum, and average temperature at the most active station, 'USC00519281'. I made a variable to house the min, max, and avg query functions, then fed it into a query that computed those statistics and filtered the results by station 'USC00519281'. The resulting values were (54.0, 85.0, 71.66378066378067) as (min, max, avg), respectively.
* The last step before creating a histogram was to find the temperature observation data for station 'USC00519281' from the last 12 months. I was able to accomplish this by using a simple query that filtered the measurement table by the station ID and the date range (>= 2016-08-23). I then saved this data into a dataframe called 'temp_data_df'.
* Lastly I created a histogram of the temperature data, with the temperature frequency on the y-axis and the temperature on the x-axis, see figure 5.

  ![alt text]()

  Fig 5: temperature histogram for previous 12 months, station USC00519281

## API SQLite Connection & Landing Page (10 points)

* Correctly generate the engine to the correct sqlite file (2 points)

* Use automap_base() and reflect the database schema (2 points)

* Correctly save references to the tables in the sqlite file (measurement and station) (2 points)

* Correctly create and binds the session between the python app and database (2 points)

* Display the available routes on the landing page (2 points)

## API Static Routes (15 points)

A precipitation route that:

* Returns json with the date as the key and the value as the precipitation (3 points)

* Only returns the jsonified precipitation data for the last year in the database (3 points)

A stations route that:

* Returns jsonified data of all of the stations in the database (3 points)

A tobs route that:

* Returns jsonified data for the most active station (USC00519281) (3 points)

* Only returns the jsonified data for the last year of data (3 points)

## API Dynamic Route (15 points)

A start route that:

* Accepts the start date as a parameter from the URL (2 points)

* Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset (4 points)

A start/end route that:

* Accepts the start and end dates as parameters from the URL (3 points)

* Returns the min, max, and average temperatures calculated from the given start date to the given end date (6 points)

## Resources
* Xpert Learning Assistant
* Module 10 Activities
