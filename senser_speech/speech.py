#!/usr/bin/python
import time
import requests

# send data in json format to server
headers = {'Content-type': 'application/json'}
status = 0

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.read()
        if not line:
            time.sleep(0.05)
            continue
        yield line


if __name__ == "__main__":
    while True:
        # print("true")
        # totalAmount = "TV on"
        # with open("output.txt", "a") as text_file:
        #     text_file.write(totalAmount)

        with open ("output.txt","r") as logfile :
            loglines = follow(logfile)
            for line in loglines:
                print(line)
                url = "http://192.168.1.124:2000/device/"
                # PC, air conditioner, light, TV, refrigerator
                if line == 'PC off':
                    url = url + "PC/status"
                    status = 0
                if line == 'PC on':
                    url = url + "PC/status"
                    status = 1
                if line == 'air conditioner off':
                    url = url + "AirConditioner/status"
                    status = 0
                if line == 'air conditioner on':
                    url = url + "AirConditioner/status"
                    status = 1
                if line == 'light off':
                    url = url + "Light/status"
                    status = 0
                if line == 'light on':
                    url = url + "Light/status"
                    status = 1
                if line == 'TV off':
                    url = url + "Television/status"
                    status = 0
                if line == 'TV on':
                    url = url + "Television/status"
                    status = 1
                if line == 'refrigerator off':
                    url = url + "Refrigerator/status"
                    status = 0
                if line == 'refrigerator on':
                    url = url + "Refrigerator/status"
                    status = 1
                try:
                    data = {"status": status}
                    rsp = requests.post(url, json=data, headers=headers)
                    print("post success")
                except Exception as e:
                    failed_key = e.args[0]
                    print("extract_key: {}".format(failed_key))





