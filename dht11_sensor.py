#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import dht11
import requests
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
instance = dht11.DHT11(pin = 17)
result = instance.read()

# send data in json format to server
url = "http://192.168.1.122:2000/sensor"
headers = {'Content-type': 'application/json'}

if __name__ == "__main__":
	while True:
		if result.is_valid():
			print("Temperature: %d C" % result.temperature)
			print("Humidity: %d %%" % result.humidity)
			datas = {
				"name":'DHT11',
				"temperature":result.temperature,
				"humidity":result.humidity, 
				"status":1
				}
			rsp = requests.post(url, json=datas, headers=headers)
		else:
			print("Error: %d" % result.error_code)
			datas = {
				"name": 'DHT11',
				"temperature":result.temperature,
				"humidity":result.humidity, 
				"status":0
				}
			rsp = requests.post(url, json=datas, headers=headers)
		time.sleep(1)

# DHT11 사용법
# https://stackoverflow.com/questions/28913592/python-gpio-code-for-dht-11-temperature-sensor-fails-in-pi-2
# http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
# https://github.com/momenso/node-dht-sensor
# DHT11 library
# https://github.com/szazo/DHT11_Python/blob/master/dht11.py
# json 통신
# https://stackoverflow.com/questions/9733638/post-json-using-python-requests
