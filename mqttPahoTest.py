import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
    print("log: " + buf)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code =", rc)

def on_disconnect(client, userdata, flags, rc = 0):
    print("Disconnected result code " + str(rc))

def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print("message received :", m_decode)
    #print("message received", msg.payload)             # falls nur so werden noch um die Nachricht Klammern gesetzt ect.

###BROKER###
broker = "127.0.0.1"                   #Localhost
#broker = "test.mosquitto.org"          #Online Broker
#broker = "169.254.173.239"             #Raspi Broker LAN
#broker = "192.168.0.16"                 #Raspi via Wlan

client = mqtt.Client("python1")

client.on_connect = on_connect
#client.on_log = on_log                                 # eigentlich lässt man das immer weg
client.on_disconnect = on_disconnect
client.on_message = on_message

print("Connecting to broker", broker)
client.connect(broker)
client.loop_start()
client.subscribe("MQTT/Test1")
time.sleep(1)
client.publish("MQTT/Test1", "my first message")
time.sleep(10)
client.loop_stop()
client.disconnect()