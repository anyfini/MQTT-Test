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
    print("message received", m_decode)
    #print("message received", msg.payload)             # falls nur so werden noch um die Nachricht Klammern gesetzt ect.

broker = "127.0.0.2"
#broker = "test.mosquitto.org"      # Online Broker
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
time.sleep(4)
client.loop_stop()
client.disconnect()
