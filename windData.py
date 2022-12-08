import pandas as pd
from influxdb import InfluxDBClient # install via "pip install influxdb"
import datetime


class WindDataCollector:
    def __init__(self):
        self.client = InfluxDBClient(host='influxus.itu.dk', port=8086, username='lsda', password='icanonlyread')
        self.client.switch_database('orkney')

    def getDf(self, results):
        values = results.raw["series"][0]["values"]
        columns = results.raw["series"][0]["columns"]
        df = pd.DataFrame(values, columns=columns).set_index("time")
        df.index = pd.to_datetime(df.index) # Convert to datetime-index
        return df

    def getGenerationData(self, now, delta):
        generation = self.client.query(
            "SELECT * FROM Generation where time > {}-{}d".format(now,delta)
        ) # Query written in InfluxQL
        
        return self.getDf(generation)
    
    def getWindData(self, now, delta):
        wind  = self.client.query(
            "SELECT * FROM MetForecasts where time > {}-{}d and time <= {} and Lead_hours = '1'".format(now,delta,now)
        ) # Query written in InfluxQL
        
        return self.getDf(wind)
    