# HafezShabrang

import paho.mqtt.client as mqtt
import time
import threading


class Clients:

    def __init__(self, mqttBroker, port, qos, user, passwd):
        self.mqttBroker = mqttBroker
        self.port = port
        self.qos = qos
        self.user = user
        self.passwd = passwd
        self.client = mqtt.Client()
        self.client.username_pw_set(username = self.user, password = self.passwd)
        self.client.connect(self.mqttBroker, self.port, self.qos)
        print("client created! and connected!")



    def publisher(self,topic):
        client = self.client
        while True:
            # msg = input("Enter Message : ")
            msg = input()
            if msg == "stop":
                break
            client.publish(topic, msg)


    

    def subscriber(self, topic):
        client = self.client
        def on_message(client,userdata,msg):
            # print(f'recived message: {msg.payload.decode("utf-8")}')
            print(msg.payload.decode("utf-8"))
            print()
        
        while True:
            client.loop_start()
            client.subscribe(topic)
            client.on_message = on_message
            client.loop_stop()



mqttBroker = "localhost"
port = 1883
qos = 2
user = "hafez"
passwd = "hafez123"
topic1 = "topic1"
topic2 = "topic2"

client1 = Clients(mqttBroker, port, qos, user, passwd)

pub = threading.Thread(target=client1.publisher, args=(topic1,))
sub = threading.Thread(target=client1.subscriber, args=(topic2,))

pub.start()
time.sleep(1)
sub.start()

pub.join()
sub.join()







