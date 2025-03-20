import os
import subprocess

# Get the current working directory
current_dir = os.getcwd()

# Build the volume mapping with proper Windows path formatting.
# Using forward slashes is often accepted by Docker on Windows.
volume_mapping = f"{current_dir}/mosquitto/config/passwords.txt:/mosquitto/config/passwords.txt"

# Construct the Docker command as a list
docker_command = [
    "docker", "run", "--rm", "-it",
    "-v", volume_mapping,
    "eclipse-mosquitto",
    "mosquitto_passwd", "-c", "/mosquitto/config/passwords.txt", "mqttuser"
]

# Execute the command
subprocess.run(docker_command)
