# serial_to_websocket.py

# Required Libraries:
# Install them using:
# pip install -r requirements.txt

import asyncio
import serial
import websockets

# Configure the serial port
serial_port = serial.Serial(
    port="/dev/ttyUSB0",      # Adjust if needed
    baudrate=230400,
    bytesize=8,
    timeout=2,
    stopbits=serial.STOPBITS_ONE
)

# WebSocket handler to stream serial data
async def websocket_handler(websocket, path):
    print("Client connected")
    try:
        # Send 'd' to start serial data transmission
        serial_port.write(b"d")

        while True:
            serial_line = serial_port.readline()
            try:
                decoded_line = serial_line.decode("ascii").strip()
                if decoded_line:
                    await websocket.send(decoded_line)
            except UnicodeDecodeError:
                continue
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

# Start WebSocket server
async def main():
    print("Starting WebSocket server on ws://0.0.0.0:8765")
    async with websockets.serve(websocket_handler, "0.0.0.0", 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
