import mysql.connector
import paho.mqtt.client as mqttClient
from threading import Thread
import json
import calendar
import datetime
from dateutil import parser
import datetime
from decimal import Decimal
import time
import random
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
        mqttclient.username_pw_set(username="",password="")
        mqttstatus = mqttclient.connect("demo.isenzr.com", 8883,60)
        mqttclient.subscribe("number",2)
        mqttclient.loop_forever()
    def upload(self,msg):
        mqtt_msg = str(msg.payload).replace("b'", "").replace("'", "").replace("  ", "").replace("\\n", "").replace("\n", '')
        mqtt_json = json.loads(mqtt_msg)
        print(mqtt_json)

    def on_connect(self,mqttclient, userdata, flags,rc):
       
        if rc == 0:
            print("connected!")
        else:
             random_value = random.randint(0, 100)
             print("Generated random value: " + str(random_value))

    def on_message(self, mqttclient, userdata, msg):
        Thread(target=self.upload, args=(msg,)).start()

    

if __name__ == '__main__':
    Mqtt()
