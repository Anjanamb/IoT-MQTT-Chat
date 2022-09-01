import time
import paho.mqtt.client as mqtt

broker = 'broker.hivemq.com'
port = 1883
username = 'app_client'
password = 'app@1234'

client_id = "client_id"
topic = "/system"

def on_connect (client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

    client.subscribe(topic, qos = 0)

#callback for  messages coming from server
def on_message (client, userdata, msg):
    print("topic: {} conetent {}" .format(msg.topic, str(msg.payload)))

def on_publish (client, userdata, mid):
    print("msg published. mid: {}" .format(mid))

client = mqtt.Client(client_id=client_id, 
                     clean_session=True, 
                     userdata=None, 
                     protocol=mqtt.MQTTv311, 
                     transport="tcp")

client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.username_pw_set(username=username, password=password)
client.connect(broker, port=1883, keepalive=60)

client.loop_start()

while True:

    payload_msg = "Test message"
    client.publish(topic,
                    payload = payload_msg,
                    qos = 0,
                    retain = False)
    
    time.sleep(5)

client.loop_stop()