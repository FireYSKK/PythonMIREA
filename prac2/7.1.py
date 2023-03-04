import re


class Room:
    def __init__(self, name, *description):
        self.name = name
        self.description = description
        self.connections = None

    def set_description(self, description):
        self.description = description

    def add_connection(self, connection):
        if not self.connections:
            self.connections = list()
        self.connections.append(connection)

    def __str__(self):
        print(self.name, self.description, self.connections)
        return ""


HEADING = '##\s\[(.*)]\s*\(#(\d+)\)'
CHOICE = '\*\s+(.*)\s+\[\.\.\.]\(#(\d+)\)'
rooms = dict()

with open('game.md', 'r', encoding='utf-8') as world:
    for line in world:
        if line == "":
            continue

        match = re.match(HEADING, line)
        if match:
            current_room = match.group(2)
            rooms[current_room] = Room(match.group(1))
            continue

        match = re.match(CHOICE, line)
        if match:
            rooms[current_room].add_connection(match.group(1, 2))
            continue

        rooms[current_room].set_description(line.strip())

for room in rooms:
    print(room, rooms[room])