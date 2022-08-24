import os
import subprocess
import uuid
import json
import time 
import random
import datetime 
import sys 
import socket

args = sys.argv
topic = args[1]
bootstrap_servers = args[2]

assert topic is not None
assert bootstrap_servers is not None


# install confluent-kafka
# probably better ways to handle this dependency but this will work 
def install(name):
    subprocess.call(['pip3', 'install', name])

install('confluent-kafka')


from confluent_kafka import Producer


# set up a producer client 
conf = {'bootstrap.servers': bootstrap_servers,
        'client.id': socket.gethostname()}
producer = Producer(conf)


while True: 
    print("====> Sending Message")
    # format a random message 
    action = "Open" if random.random() < 0.5 else "Close"
    current_time = int(datetime.datetime.utcnow().timestamp())*1000
    
    data = {"eventId": str(uuid.uuid1()), "action": action, "time": current_time}
    print("==> {}".format(data))
    # send the data to the topic 
    producer.produce(topic, key="event_message", value=json.dumps(data).encode('utf-8'))
    producer.flush()
    time.sleep(5) # wait for 5 seconds 
    



