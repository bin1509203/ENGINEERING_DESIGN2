#!/usr/bin/python
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import requests
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
humidity,temperature = dht.read_retry(dht.DHT22, 17)
temperature = round(temperature, 2)
humidity = round(humidity, 2)

# send data in json format to server
url = "http://192.168.1.74:2000/sensor"
headers = {'Content-type': 'application/json'}

if __name__ == "__main__":
	while True:
		# if result.is_valid():
		print("Temperature: %d C" % temperature)
		print("Humidity: %d %%" % humidity)
		datas = {
			"temperature":temperature,
			"humidity":humidity, 
			"status":1
			}
		rsp = requests.post(url, json=datas, headers=headers)
		time.sleep(5)
		# else:
		# 	print("Error: %d" % result.error_code)
		# 	datas = {
		# 		"temperature":result.temperature,
		# 		"humidity":result.humidity, 
		# 		"status":0
		# 		}
		# 	rsp = requests.post(url, json=datas, headers=headers)
		

# DHT11 사용법
# https://stackoverflow.com/questions/28913592/python-gpio-code-for-dht-11-temperature-sensor-fails-in-pi-2
# http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
# https://github.com/momenso/node-dht-sensor
# DHT11 library
# https://github.com/szazo/DHT11_Python/blob/master/dht11.py
# json 통신
# https://stackoverflow.com/questions/9733638/post-json-using-python-requests
