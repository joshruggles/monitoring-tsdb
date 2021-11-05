import time
import psutil
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# set timer
starttime = time.time()

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
bucket = "devops"
org = "devops-monitoring"
token = "worst-token-ever"
url="http://influxdb2:8086"

# instantiate the client
client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)

# instantiate the write client
write_api = client.write_api(write_options=SYNCHRONOUS)

def collector():
    write_api.write(bucket=bucket, org=org, record=data)

while True:
    collector()
    print(data[0]['fields'])
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))