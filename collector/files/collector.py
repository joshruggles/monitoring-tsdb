import os
import time
import psutil
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# set timer
starttime = time.time()

def collector():
  # set measurement name
  measurement_name = "system"

  # collect node load
  load = psutil.getloadavg()

  # set data for influxdb2
  data = [
    {
        "measurement": measurement_name,
        "fields": {
            "load_1": load[0],
            "load_5": load[1],
            "load_15": load[2],
        }
      }
    ]

  # https://docs.influxdata.com/influxdb/cloud/api-guide/client-libraries/python/

  # define influxdb2 variables
  bucket = os.environ.get('BUCKET')
  org = os.environ.get('ORG')
  token = os.environ.get('TOKEN')
  url= os.environ.get('URL')

  # instantiate the client
  client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
  )

  # instantiate the write client
  write_api = client.write_api(write_options=SYNCHRONOUS)
  write_api.write(bucket=bucket, org=org, record=data)

  # print out loads
  print(data[0]['fields'])

while True:
    collector()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))