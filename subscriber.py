import paho.mqtt.client as mqtt

# Configuration parameters
broker_address = "localhost"  # or your broker's IP address
port = 1883
username = "mqttuser"
password = "123456"
topic = "smart_trash_can/trash_count"

# Callback function when a message is received
def on_message(client, userdata, message):
    print("Message received:", message.payload.decode("utf-8"))

# Create an MQTT client instance
client = mqtt.Client("python_sub")
client.username_pw_set(username, password)

# Set the on_message callback
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, port, keepalive=60)

# Subscribe to the topic
client.subscribe(topic)
print(f"Subscribed to topic: '{topic}'")

# Loop forever, waiting for incoming messages
client.loop_forever()
