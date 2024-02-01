import paho.mqtt.client as mqtt
from utils import get_or_default_str, get_or_default_int, get_or_default_bool, print_connection_parameters, print_connection_successful

host = get_or_default_str("Host", "localhost")
port = get_or_default_int("Port", 1883)
client_id = get_or_default_str("Client ID", "client.id")
topic = get_or_default_str("Topic", "example")
qos = get_or_default_int("QoS", 0)
retain = get_or_default_bool("Retain", False)

def on_connect(client, userdata, flags, rc):
    print_connection_successful(host, port, rc)

print_connection_parameters(host, port, client_id)
client = mqtt.Client(client_id)
client.on_connect = on_connect
client.connect(host, port)
client.loop_start()

while client.is_connected:
    data = input("Enter data to send: ")
    client.publish(topic, data, qos, retain)
