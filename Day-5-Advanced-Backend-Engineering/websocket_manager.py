
from fastapi import WebSocket
from collections import defaultdict


class ConnectionManager:

    def __init__(self):
        # Store WebSocket connections room-wise
        self.rooms = defaultdict(set)

    async def connect(self, websocket: WebSocket, room: str):
        # Accept the WebSocket connection
        await websocket.accept()

        # Add connection to the requested room
        self.rooms[room].add(websocket)

    def disconnect(self, websocket: WebSocket, room: str):
        # Remove connection from the room
        if room in self.rooms:
            self.rooms[room].discard(websocket)

            # Remove empty rooms
            if not self.rooms[room]:
                del self.rooms[room]

    async def broadcast(self, message: str, room: str):
        # Send message to every connection in the room
        connections = list(self.rooms.get(room, set()))

        for connection in connections:
            try:
                await connection.send_text(message)
            except Exception:
                self.disconnect(connection, room)


# Create one shared manager
manager = ConnectionManager()
