import re
import queue
import graphviz


class Room:
    def __init__(self, name, *description):
        self.name = name
        self.description = None
        self.connections = None

    def set_description(self, description):
        if not self.description:
            self.description = description
            return
        self.description += '\n' + description

    def add_connection(self, connection):
        if not self.connections:
            self.connections = list()
        self.connections.append(connection)

    def print_room(self):
        print(self.name, '\n')
        print(self.description, '\n')
        for i in range(len(self.connections)):
            print(str(i + 1) + '.', self.connections[i][0])

    def get_connected_room(self, connection_number):
        return self.connections[connection_number - 1][2]


HEADING = r'##\s\[(.*)]\s*\(#(.+)\)'
CHOICE = r'^\*\s+(.*)\[(.+)]\(#(.+)\)'
REPEAT_MSG = 'Некорректный ввод'
CONGRATULATIONS_MSG = 'Вы выбрались!'
rooms = dict()
world_map = graphviz.Digraph()


def load_world(source):
    with open(source, 'r', encoding='utf-8') as world:
        for line in world:
            if line == "\n":
                continue

            match = re.match(HEADING, line)
            if match:
                current_room = match.group(2)
                rooms[current_room] = Room(match.group(1))
                continue

            match = re.match(CHOICE, line)
            if match:
                rooms[current_room].add_connection(match.group(1, 2, 3))
                world_map.edge(current_room, match.group(3))
                continue

            rooms[current_room].set_description(line.strip())


def check_adjacency():
    reverse_connections = dict()
    for room in rooms:
        for connected_room in rooms[room].connections:
            if connected_room[2] in reverse_connections:
                reverse_connections[connected_room[2]].append(room)
            else:
                reverse_connections[connected_room[2]] = [room]

    escape = set()
    rooms_to_check = queue.Queue()
    rooms_to_check.put('end')
    while not rooms_to_check.empty():
        step = rooms_to_check.get()
        for connected_room in reverse_connections[step]:
            if connected_room in escape:
                continue
            escape.add(connected_room)
            rooms_to_check.put(connected_room)

    for room in rooms:
        if room not in escape:
            print(room, "is a dead end")
            print('--------------------')


load_world('game.md')
check_adjacency()
world_map.node('end', style='filled', fillcolor='green')
world_map.render(outfile='world_map.svg')

next_room = '1'
while next_room != 'end':
    rooms[next_room].print_room()
    path = input('\n>')
    while not (re.fullmatch(r'\d+', path) and int(path) in range(1, len(rooms[next_room].connections) + 1)):
        path = input(REPEAT_MSG + '\n>')
    next_room = rooms[next_room].get_connected_room(int(path))

print(CONGRATULATIONS_MSG)
