import requests
import time

temperature = 15
humidity = 60

# send data in json format to server
url = "http://localhost:2000/sensor"
headers = {'Content-type': 'application/json'}

if __name__ == "__main__":
	while True:
		if 1 == 1:
			print("Temperature: %d C" % temperature)
			print("Humidity: %d %%" % humidity)
			datas = {
				"temperature":temperature,
				"humidity":humidity, 
				"status":1
				}
			rsp = requests.post(url, json=datas, headers=headers)
		else:
			print("Error")
			datas = {
				"temperature":temperature,
				"humidity":humidity, 
				"status":0
				}
			rsp = requests.post(url, json=datas, headers=headers)
		time.sleep(5)
