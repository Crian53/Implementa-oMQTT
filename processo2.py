import paho.mqtt.client as mqtt
from struct import pack
from random import randint
from time import sleep
 
AREA_ID = 10
SENSOR_ID = 5000

tt = "area/%d/sensor/%s/umidade" % (AREA_ID,SENSOR_ID)
ut = "area/%d/sensor/%s/temperatura" % (AREA_ID,SENSOR_ID)

client = mqtt.Client(client_id = 'NODE:%d-%d' % (AREA_ID,SENSOR_ID),
                     protocol = mqtt.MQTTv31)

client.connect("127.0.0.1", 1883)
 
while True:
    t = randint(0,50)
    payload = pack(">H",t)
    client.publish(tt,payload,qos=0)
    print(tt + "/" + str(t))
    u = randint(0,100)
    payload = pack(">H",u)
    client.publish(ut,payload,qos=0)
    print(ut + "/" + str(u))
    
    sleep(5)
