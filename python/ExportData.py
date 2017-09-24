
from bs4 import BeautifulSoup
import psycopg2

# Link to HTML doc
htmlDoc = r'/Users/samuelgrosenick/Documents/Projects/AncWeatherMap/index.html'

# Open the HTML doc with BeautifulSoup
with open(htmlDoc) as fp:
    soup = BeautifulSoup(fp, 'lxml')

# Extract the AWS table
aws = soup.find("table", {"id": "AWS"})
rows = aws.find('tbody').find_all('tr')

# Iterate past the frist two rows, ignoring title and hearder rows
iterrows = iter(rows)
next(iterrows)
next(iterrows)

# Connect to heroku database
conn = psycopg2.connect(host="ec2-50-17-217-166.compute-1.amazonaws.com", database="da6gb10sr74e3i",\
 user="avihgcjvhypvgq", password="bb4fd2d54c1b90e40f423aa5bc45667edcb0f0d6a41aeb98b0470f1fd9b2ebe1")

# Create cursor
cur = conn.cursor()

# Create AWS weater station table
cur.execute('CREATE TABLE AWS_WeatherStations (StationID varchar PRIMARY KEY, StationName varchar, \
 Temp varchar, DewPt varchar, RelHumidity varchar, WindDir varchar, WindSpeed varchar, WindGust varchar, SeaLevelPress varchar)')

#Extract weather station data for each station and insert into database
for row in iterrows:
    if len(row) > 1:
        cell = [i.text for i in row.find_all('td')]
        sql = "INSERT INTO AWS_WeatherStations (StationID, StationName, Temp, \
         DewPt, RelHumidity, WindDir, WindSpeed, WindGust, SeaLevelPress) VALUES (%s,\
          %s, %s, %s, %s, %s, %s, %s, %s);"
        data = (cell[0], cell[1], cell[2], cell[3], cell[4], cell[5], cell[6], cell[7], cell[8],)
        cur.execute(sql, data)

### Query the database and obtain data as Python objects
##cur.execute("SELECT * FROM AWS_WeatherStations;")
##cur.fetchone()

# Make changest to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
