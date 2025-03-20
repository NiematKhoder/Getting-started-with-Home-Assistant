import time
import random
import paho.mqtt.client as mqtt

# MQTT Broker Configuration
broker_address = "localhost"  # or your broker's IP address
broker_port = 1883
username = "mqttuser"
password = "123456"

# MQTT Topics
fill_percentage_topic = "smart_trash_can/fill_percentage"
motion_topic = "smart_trash_can/motion"
location_topic = "smart_trash_can/location"
id_topic = "smart_trash_can/id"
trash_count_topic = "smart_trash_can/trash_count"

# Create MQTT client
client = mqtt.Client("smart_trash_can_client")
client.username_pw_set(username, password)
client.connect(broker_address, broker_port)

# Publish 20 messages at 2-second intervals
for i in range(20):
    # Generate random values
    fill_percentage = random.randint(0, 100)
    motion_status = random.choice(["detected", "no_motion"])
    location_value = random.choice([
        "Building A, Room 101",
        "Building B, Room 202",
        "Building C, Room 303"
    ])
    trash_can_id = random.choice(["TC-001", "TC-002", "TC-003"])
    count = random.randint(0, 10)

    # Publish each value to its respective topic
    client.publish(fill_percentage_topic, fill_percentage)
    client.publish(motion_topic, motion_status)
    client.publish(location_topic, location_value)
    client.publish(id_topic, trash_can_id)
    client.publish(trash_count_topic, count)

    print(f"Iteration {i+1}:")
    print(f"  Fill Percentage: {fill_percentage}")
    print(f"  Motion Status: {motion_status}")
    print(f"  Location: {location_value}")
    print(f"  Trash Can ID: {trash_can_id}")
    print(f"  Trash Count: {count}\n")

    # Wait 2 seconds before the next iteration
    time.sleep(2)

# Disconnect after publishing all messages
client.disconnect()
