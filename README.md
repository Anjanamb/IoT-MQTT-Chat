# IoT-MQTT-ChatApp

A lightweight IoT-based **chat application** implemented in Python using **MQTT (paho-mqtt)** and **Tkinter**.  
This project demonstrates real-time publish/subscribe messaging with a GUI chat client as well as simple CLI publisher/subscriber examples.  

Originally developed as a Semester 6B IoT lab project.

---

## Features

- **Graphical Chat Client (Tkinter)**  
  - Connect with a custom **name** and **topic**  
  - Real-time chat via MQTT broker  
  - Scrollable chat history  
  - Enter `exit` to close session gracefully  

- **MQTT Publisher**  
  - Publishes a test message every 5 seconds  
  - Useful for testing broker connectivity  

- **MQTT Subscriber**  
  - Listens on a topic and prints incoming messages  

---

## Project Structure
```
IoT-MQTT-ChatApp/
├── Chat_App_Lab.py # GUI chat client using Tkinter + MQTT
├── publisher.py # Simple MQTT publisher
├── subscriber.py # Simple MQTT subscriber
└── README.md # Project documentation
```

---

## Requirements

- Python **3.7+**
- Dependencies:
  ```bash
  pip install paho-mqtt

---

## Usage

### 1. Run the GUI Chat Client
```bash
python Chat_App_Lab.py
```
- Enter your Name and a Topic to join.
- Press Connect.
- Type your messages and hit Enter to send.
- All users connected to the same topic will see the messages.

### 2. Run the CLI Publisher
```bash
python publisher.py
```
Publishes `"Test message"` every 5 seconds to `/system` topic.

### Run the CLI Subscriber
```bash
python subscriber.py
```
Subscribes to `/system` topic and prints incoming messages.

---

## How It Works
- Broker: Uses HiveMQ’s public broker (`broker.hivemq.com:1883`) by default.
- Publisher: Sends messages to an MQTT topic.
- Subscriber: Receives messages from the topic.
- GUI Client: Combines publisher and subscriber with a Tkinter chat window.

Messages are exchanged in JSON format:

```json
{
  "Name": "Alice",
  "msg": "Hello world!"
}
```

---

## Future Enhancements

- Add private messaging and multi-topic chatrooms
- Include timestamps in messages
- Enable TLS/SSL encryption for secure communication
- Package as a desktop executable (PyInstaller)
- Extend to a web-based MQTT chat

---

## Acknowledgments

This project was created as part of the Semester 6B IoT Lab. It serves as a foundational example of MQTT messaging in Python.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---


