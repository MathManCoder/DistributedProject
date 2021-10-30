# HafezShabrang

import os
import paho.mqtt.client as mqtt
import time
import threading


class Clients:

    def __init__(self, mqttBroker, port, qos, username, passwd):
        self.mqttBroker = mqttBroker
        self.port = port
        self.qos = qos
        self.username = username
        self.passwd = passwd
        self.client = mqtt.Client()
        self.client.username_pw_set(username = self.username, password = self.passwd)
        self.client.connect(self.mqttBroker, self.port, self.qos)
        print("client created! and connected!")



    def publisher(self,topic):
        client = self.client
        while True:
            msg = input()
            if msg == "stop":
                break
            client.publish(topic, msg)


    

    def subscriber(self, topic):
        client = self.client
        def on_message(client,userdata,msg):
            print(msg.payload.decode("utf-8"))
        
        while True:
            client.loop_start()
            client.subscribe(topic)
            client.on_message = on_message
            client.loop_stop()



mqttBroker = "195.248.240.240"
port = 1883
qos = 2
username = "hafez"
passwd = "hafez123"
topic1 = "topic1"
topic2 = "topic2"

client1 = Clients(mqttBroker, port, qos, username, passwd)


#############   Threading    ##############
pub = threading.Thread(target=client1.publisher, args=(topic1,))
sub = threading.Thread(target=client1.subscriber, args=(topic2,))

pub.start()
time.sleep(1)
sub.start()

pub.join()
sub.join()
#############   End Threading    ##############





