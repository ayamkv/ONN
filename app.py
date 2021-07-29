
import requests, json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

ip = ''
data = requests.get(f"https://api.mcsrvstat.us/2/{ip}").json()

dataOnline = data["online"]
isFalse = bool(dataOnline == 'false') 
motd = data["motd"]["clean"]
version = data["version"]
hostname = data["hostname"]
playerOn = data["players"]["online"]
playerMax = data["players"]["max"]

