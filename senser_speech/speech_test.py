#!/usr/bin/python
import time
import requests

# send data in json format to server
headers = {'Content-type': 'application/json'}
status = 0
url = "http://localhost:2000/device/"

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
                line = line.strip() # 양쪽 공백 제거
                # PC, air conditioner, light, TV, refrigerator
                if line == 'PC off':
                    url = url + "PC/status"
                    status = 0
                elif line == 'PC on':
                    url = url + "PC/status"
                    status = 1
                elif line == 'AC off' or line == 'air conditioner off':
                    url = url + "AirConditioner/status"
                    status = 0
                elif line == 'AC on' or line == 'air conditioner on':
                    url = url + "AirConditioner/status"
                    status = 1
                elif line == 'light off':
                    url = url + "Light/status"
                    status = 0
                elif line == 'light on':
                    url = url + "Light/status"
                    status = 1
                elif line == 'TV off' or line == 'television off':
                    url = url + "Television/status"
                    status = 0
                elif line == 'TV on'or line == 'television on':
                    url = url + "Television/status"
                    status = 1
                elif line == 'refrigerator off':
                    url = "http://192.168.1.144:2000/device/Refrigerator/status"
                    status = 0
                elif line == 'refrigerator on':
                    url = "http://192.168.1.144:2000/device/Refrigerator/status"
                    status = 1
                else:
                    status = 'NA'
                if status != 'NA' :
                    try:
                        data = {"status": status}
                        rsp = requests.post(url, json=data, headers=headers)
                        print(url+" => post success")
                        url = "http://localhost:2000/device/"
                    except Exception as e:
                        failed_key = e.args[0]
                        print("extract_key: {}".format(failed_key))
                        url = "http://localhost:2000/device/"
                else:
                    print("no matching")
                    url = "http://localhost:2000/device/"
