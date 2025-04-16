# Serial to WebSocket Bridge

This project reads data from a serial device connected to a Raspberry Pi and broadcasts it over a WebSocket server.

## Features
- Reads from serial port `/dev/ttyUSB0` in Linux  
- Reads from serial port `COM7` in Windows  
- Sends command `d` to the device to start data transmission (you can change this command based on your serial device's protocol)  
- Streams serial data to any WebSocket client  
- Simple and lightweight Python script

## Requirements
Install required libraries with:
```bash
pip install -r requirements.txt
```

## requirements.txt
```
pyserial
websockets
```

## Usage
Run the script using:
```
python3 serial_to_websocket.py
```

## WebSocket Server
The server runs at:
```
ws://<your-pi-ip>:8765
```
Replace <your-pi-ip> with the actual IP address of your Raspberry Pi.

You can connect using a WebSocket client (e.g., Postman, browser, or Python) to receive real-time data.

## Example Client in Python
```
import websocket

ws = websocket.WebSocket()
ws.connect("ws://<your-pi-ip>:8765")

while True:
    print(ws.recv())
```

## Connecting Using Postman
1. Open Postman.
2. Click on New > WebSocket Request.

3. Enter the WebSocket URL:
```
ws://<your-pi-ip>:8765
```
4. Click Connect.
5. You should start receiving real-time data if the serial device is sending it.

## Debugging Tips
To verify if the WebSocket server is listening, run:
```
netstat -tuln | grep 8765
```
You should see a line showing 0.0.0.0:8765 or :::8765 if the server is running properly.

