import mysql.connector
import paho.mqtt.client as mqttClient
from threading import Thread
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import mysql.connector
import datetime
import calendar
import time


class Mqtt:
    def __init__(self):
        self.json_data = {}
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            db="demo")
        mqttclient = mqttClient.Client("52244535477668454")
        mqttclient.on_connect = self.on_connect
        mqttclient.on_message = self.on_message
        #print(mqttclient.on_message)
        mqttclient.username_pw_set(username="",password="")
        mqttstatus = mqttclient.connect("broker.emqx.io", 1883,60)
        mqttclient.subscribe("airquality",2)
        mqttclient.loop_forever()


    def upload(self,msg):
        mqtt_msg = str(msg.payload).replace("b'", "").replace("'", "").replace("  ", "").replace("\\n", "").replace("\n", '')
        print(msg.payload)
        mqtt_msg = str(mqtt_msg).replace("\\","")
        mqtt_msg = str(mqtt_msg).replace('}"','}')
        mqtt_msg = str(mqtt_msg).replace('"{','{')
        mqtt_msg = str(mqtt_msg).replace('{','')
        mqtt_msg = str(mqtt_msg).replace('}','')
        mqtt_msg = str(mqtt_msg).replace('"','')
        mqtt_msg = mqtt_msg.split(",")
        #print("====",mqtt_msg)
        #print("=----",mqtt_msg[2]) 
        # {
         #   'temperature': temperature,
          #  'humidity': humidity,
           # 'pollution_level': 0.123,  # Replace with your pollution sensor data
            #'particulate_matter': 2.5,  # Replace with your PM sensor data
       # }

       
        temp = mqtt_msg[1].split(":")[1]
        print("rv:"+temp+"end")
        #ya = mqtt_msg[4].split(":")[1]
        #ba = mqtt_msg[5].split(":")[1]
        #rv = mqtt_msg[1].split(":")[1]
        #print("rv:"+rv+"end")
        humidity = mqtt_msg[2].split(":")[1]
        print("yv:"+humidity+"end")
        pollution = mqtt_msg[3].split(":")[1]
        print("bv:"+pollution+"end")
        particulatematter = mqtt_msg[4].split(":")[1]
        print("ri:"+particulatematter+"end")
        
       
       
    def on_connect(self,mqttclient, userdata, flags,rc):
        if rc == 0:
            print("connected!")
        else:
            print("Connection failed")


    def on_message(self, mqttclient, userdata, msg):
        Thread(target=self.upload, args=(msg,)).start()
       # print("enter")


if __name__ == '__main__':
    Mqtt()
