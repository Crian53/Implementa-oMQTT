import paho.mqtt.client as mqtt
from struct import unpack
from time import sleep

TOPIC = "area/10/sensor/#"

def on_connect(client, data, rc):
    client.subscribe([(TOPIC,0)])

def on_message(client, userdata, msg):
    v = unpack(">H",msg.payload)[0]
    print(msg.topic + "/" + str(v))

client = mqtt.Client(client_id = 'SCADA',
                     protocol = mqtt.MQTTv31)

client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883)
