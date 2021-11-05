# monitoring-tsdb
Monitoring solution using Influxdb2

![contributors](https://img.shields.io/github/contributors/joshruggles/saas-system-design)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
[![pypi version](https://badge.fury.io/py/influxdb-client.svg)](https://badge.fury.io/py/influxdb-client.svg)
[![pypi version](https://badge.fury.io/py/psutil.svg)](https://badge.fury.io/py/psutil.svg)
![python version](https://img.shields.io/badge/python-3.7-blue?logo=python)

## Setup

1. Install docker-compose on host.
1. Clone this repo on host.
1. Change environment secrets.
1. Run the following command from the root of the repo:

```
docker-compose up -d
```

Login to influxdb via [http://localhost:8086/](http://localhost:8086/)

Login to grafana via [http://localhost:3000/](http://localhost:3000/)