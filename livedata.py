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
        mqttstatus = mqttclient.connect("iot-dev.innomaint.com", 1883,60)
        mqttclient.subscribe("v1/devices/me/telemetryz",2)
        mqttclient.loop_forever()


    def upload(self,msg):
        mqtt_msg = str(msg.payload).replace("b'", "").replace("'", "").replace("  ", "").replace("\\n", "").replace("\n", '')
        mqtt_json = json.loads(mqtt_msg)
        #{'temp': [{'ipid': '1', 'value': 31, 'error_code': 0}]

        #{'mac': '94e686434928',
        #'dt': '2023-07-12T06:29:13Z',
        #'Subtopic': 'DeviceCommand',
        #'temp': [{'ipid': '1', 'value': 31, 'error_code': 0}],
        #'pressure': [{'ipid': '2', 'value': 0}],
        #'flow': [{'ipid': '3', 'value': 0}]}
        print(mqtt_json)
       # mac=str(mqtt_json['mac'])
        dt=(mqtt_json['dt'])
        sub=str(mqtt_json['Subtopic'])
        temp=(mqtt_json['temp'][0]['value'])
        pre=(mqtt_json['pressure'][0]['value'])
        flow=(mqtt_json['flow'][0]['value'])
        #print(mac)
        #print(type(mac))
        print(type(dt))
        print(type(sub))
        print(type(temp))
        print(type(pre))
        print(type(flow))
        #print(mac)
        print(dt)
        print(sub)
        print(temp)
        print(pre)
        print(flow)
        maxi="94e686434928"
        nm=maxi
        print("Data Inserted!")
        dt_tmp = parser.parse(dt)
        #format = "%y-%m-%dT%h:%m:%i" 
        #dateTime = time.strftime(format, time.gmtime(dt))
        #print(DT)
        #print(type(DT))
        #mac = Decimal(mac)
        #print(mac)
        #print(type(mac))
        # Create datetime string
        #Date as a string
       
        predict_epoch = calendar.timegm(dt_tmp.timetuple())
        epoch_date_time = datetime.datetime.fromtimestamp(predict_epoch)
        print(predict_epoch)
        print(type(predict_epoch))
        maxi=94e686434928
        mydb = mysql.connector.connect(host="localhost",user="root",password="",database="demo")
       
        mycursor = mydb.cursor()
        sql = 'INSERT INTO `sensors`(dt,sub,temp,pre,flow,mac) VALUES (%s,%s,%s,%s,%s,%s)'
        mycursor.execute(sql,(epoch_date_time,sub,temp,pre,flow,nm))
        mydb.commit()

        mycursor.close()
        mydb.close()


        

    def on_connect(self,mqttclient, userdata, flags,rc):
        if rc == 0:
            print("connected!")
        else:
            print("Connection failed")
        mqttclient = mqtt_client.Client(client_id)
        mqttclient.on_connect = on_connect
        mqttclient.connect(broker, port)
        mqttclient.username_pw_set("U6rxd0cFJyrlN46iRarC")
        return mqttclient

    def on_message(self, mqttclient, userdata, msg):
        Thread(target=self.upload, args=(msg,)).start()


if __name__ == '__main__':
    Mqtt()
