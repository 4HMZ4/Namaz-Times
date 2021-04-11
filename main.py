import json
import requests
from datetime import date

today = date.today()
month = today.strftime("%m")
year = today.strftime("%Y")

with open("config.json") as f:
    config = json.load(f)

method = config["method"]

lat = config["latitude"]
lon = config["longitude"]

tunImsak = config["tunImsak"]
tunFajar = config["tunFajar"]
tunSunrise = config["tunSunrise"]
tunDhuhr = config["tunDhuhr"]
tunAsr = config["tunAsr"]
tunMaghrib = config["tunMaghrib"]
tunSunset = config["tunSunset"]
tunIsha = config["tunIsha"]
tunMidnight = config["tunMidnight"]

apiurl = f"http://api.aladhan.com/v1/calendar?latitude={lat}&longitude={lon}&method={method}&month={month}&year={year}&tune={tunImsak},{tunFajar},{tunSunrise},{tunDhuhr},{tunAsr},{tunMaghrib},{tunSunset},{tunIsha},{tunMidnight}"

request = requests.get(apiurl)
reqData=(request.json())

data = open("data.json", "w")
data.write(json.dumps(reqData, indent=4))
data.close

