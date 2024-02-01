import paho.mqtt.client as mqtt
from utils import get_or_default_str, get_or_default_int, print_connection_parameters, print_connection_successful, print_message

host = get_or_default_str("Host", "localhost")
port = get_or_default_int("Port", 1883)
client_id = get_or_default_str("Client ID", "client.id")
topic = get_or_default_str("Topic", "example")

def on_connect(client, userdata, flags, rc):
    print_connection_successful(host, port, rc)
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print_message(msg.topic, str(msg.payload))

print_connection_parameters(host, port, client_id)
client = mqtt.Client(client_id)
client.on_connect = on_connect
client.on_message = on_message

client.connect(host, port)
client.loop_forever()