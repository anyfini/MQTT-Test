import time

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Sub connected")

def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print("message received :", m_decode)

###Broker###
#broker = "localhost"
broker = "192.168.0.16"

subclient = mqtt.Client()

subclient.on_connect = on_connect
subclient.on_message = on_message

print("Connecting to broker", broker)
subclient.connect(broker)
subclient.loop_start()
subclient.subscribe("MQTT/Test1")
time.sleep(10)
subclient.loop_stop()
subclient.disconnect()

# todo finish this shiat


