import paho.mqtt.client as mqttClient
import random

# MQTT broker details
broker_address = "iot-dev.innomaint.com"
broker_port = 1883
topic = "v1/devices/me/telemetry"

# Callback function for when a message is received
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
client=mqttClient.Client()
client.on_message=on_message
#Connect to MQTT broker
client.connect(broker_address, broker_port)

# Subscribe to the topic
client.subscribe(topic)

# Start the MQTT loop to process incoming messages
client.loop_start()

# Main loop to check for live data or generate random values
while True:
    # Check if any live data has been received
   
    
    # Generate random values as no live data exists
    random_value = random.randint(0, 100)
    print("Generated random value: " + str(random_value))
    
    # Publish the random value to the MQTT topic
    client.publish(topic, str(random_value))
