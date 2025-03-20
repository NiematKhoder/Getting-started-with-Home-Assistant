# Smart Trash Can Application
This repository provides a basic project to **get started with Home Assistant using MQTT** 🚀. The project is inspired by inspired by this Linux-based [guide](https://gbouloukakis.com/courses/csc4255-w25/labs/mqtt/). 
I'm doing this project to share my practical journey, applying it on a Windows system with Python scripts.
Throughout the process, I encountered some errors and solved them, which are documented in the Error Log section below. 

## Overview
The goal 🎯 of this tutorial is to create a Smart Trash Can 🗑️ Application. In this project, multiple virtual sensors are simulated using Python scripts that generate random data.
The generated data is published via MQTT and visualized in a Home Assistant instance. This project serves as a hands-on introduction to integrating Home Assistant with MQTT 
for smart home applications.

---

## What You'll Learn

- 🏠 **Setting up Home Assistant and MQTT.**
- 🐍 **Creating virtual sensors using Python.**
- 📡 **Publishing sensor data via MQTT.**
- 📊 **Visualizing sensor data in Home Assistant.**
- 🔧 **Troubleshooting common issues encountered during integration.**

Below is an updated "Prerequisites" section that includes Docker Compose, along with a brief note on its importance for the project:

---

## Prerequisites

- **Python 3 🐍**

  Ensure you have Python 3 installed. If not, download it from the [official Python website](https://www.python.org/downloads/).  
  **To verify your installation:**  
  Open the command prompt (CMD) and run:
  ```bash
  python --version
  ```

- **Paho-MQTT Library 📡**  

  This project uses the `paho-mqtt` library for MQTT communication.  
  **To install it:**  
  Open CMD and execute:
  ```bash
  pip install paho-mqtt
  ```

- **Docker 🐳**  

  To run Home Assistant on Windows, Docker is required.  
  **Download Docker:**  
  Get Docker for Windows from the [Docker website](https://www.docker.com/products/docker-desktop/).  
  **To verify Docker installation:**  
  Open CMD and run:
  ```bash
  docker --version
  ```

- **Docker Compose 📦**  

  Docker Compose is essential for orchestrating multiple containers, making it easier to manage and run Home Assistant alongside other services.  
  **To install Docker Compose:**  
  Follow the instructions on the [Docker Compose installation page](https://docs.docker.com/compose/install/).  
  **To verify Docker Compose installation:**  
  Open CMD and run:
  ```bash
  docker-compose --version
  ```

---

## Introduction to Home Assistant

Home Assistant is an **open-source home automation platform** designed to centralize control of your smart home devices while keeping your data secure. 
It acts as a hub for integrating various sensors, devices, and services, providing a unified and customizable dashboard to manage your home environment.More information can be found at 
[Home Assistant](https://www.home-assistant.io/)

### Key Features and Importance

- **Unified Control 🏠:**  
  Manage a wide range of devices—from lights and thermostats to cameras and sensors—all from one interface.

- **Local Control & Privacy 🔒:**  
  Unlike many cloud-based solutions, Home Assistant runs on your own hardware. This ensures that your personal data stays within your home network, reducing reliance on external servers and enhancing privacy.

- **Customizability & Flexibility ⚙️:**  
  Home Assistant is highly customizable with numerous integrations and automation options. Its open-source nature encourages community contributions and continuous improvement.

- **Cost-Effective & Open Source 💰:**  
  Being free to use, Home Assistant is accessible to hobbyists and professionals alike, making it a powerful tool for anyone looking to build a smart home without hefty subscription fees.

### Home Assistant vs. Google Assistant

While both Home Assistant and Google Assistant are popular in the smart home ecosystem, they serve different purposes:

- **Home Assistant:**  
  - **Role:** Acts as a central hub for home automation, enabling you to control and automate various smart devices.
  - **Operation:** Runs locally on your hardware, ensuring privacy and fast response times.
  - **Customization:** Highly configurable, allowing you to create custom automations and dashboards.
  - **Data Privacy:** Keeps your data on your local network, reducing exposure to third-party services.

- **Google Assistant:**  
  - **Role:** A voice-activated digital assistant designed to answer questions, control smart devices, and perform tasks using natural language.
  - **Operation:** Relies on cloud-based processing, which may involve sending data to external servers.
  - **Integration:** Works well with a broad range of devices and services primarily via voice commands.
  - **User Experience:** Focused on voice interactions and providing quick answers or executing commands on connected devices.

Understanding these differences is crucial for those new to home automation. Home Assistant is ideal for users who want a robust, customizable, and privacy-focused solution, whereas Google Assistant is best suited for those who prefer voice-activated commands and a more guided experience.

---

Below is a sample section for your README that explains how to install and run Home Assistant as a Docker container, along with a detailed explanation of the steps and important notes:

---

## Install and Run Home Assistant as a Docker Container

Before you begin, **ensure that the Docker Engine is running on your Windows OS**.

### Steps to Follow

1. **Start with the Tutorial:**  
   Follow the tutorial available at [Home Assistant Docker Tutorial](https://gbouloukakis.com/courses/csc4255-w25/labs/homeassistant/) starting from **Step 4**.

2. **Run Home Assistant:**  
   In **Step 5**, instead of navigating to `http://<your-raspberrypi-ip>:8123` in your browser, use `http://localhost:8123` to access Home Assistant.

### Quick Explanation

- **Test Sensor Configuration:**  
  You will first configure a test sensor to verify that Home Assistant can visualize data using a custom dashboard.

- **Creating a Dashboard:**  
  After configuring the sensor, you'll create your own dashboard. Home Assistant offers two ways to create views:  
  - **Drag and Drop:** For a quick and easy layout configuration.
  - **Code (YAML):** For advanced customization.  
    In your dashboard configuration, you'll add a view as code that includes various **cards**.  
    For example, you can add:
  ```yaml
  cards:
    - type: gauge
    - type: entities
  ```
  These cards are elements in Home Assistant that allow you to customize your view extensively, and there are many more types available.

- **Important Note on Sensor Naming:**  
  When adding your test sensor to the **view** , you reference it as `sensor.smart_trash_can`.
  ```yaml
  cards:
      # A gauge card to visually show the fill percentage
      - type: gauge
        entity: sensor.smart_trash_can
  ...

   - type: entities
        title: Smart Trash Can Details - type: entities
        title: Smart Trash Can Details
  ```

  However, even though your sensor template is defined with a `name` field like this:
  ```yaml
  template:
    - sensor:
        - name: "Smart Trash Can"
      ...
  ```
> [!NOTE]
  > **Home Assistant uses the `name` field to create a unique identifier for the sensor by converting all letters to lowercase and removing spaces.**
  > **This means that even if you assign to the sensor a unique ID, Home Assistant will still reference the sensor in the view using the name-based identifier (e.g., `sensor.smart_trash_can`).**
  > **This is important to keep in mind when configuring your dashboard views.**

---




