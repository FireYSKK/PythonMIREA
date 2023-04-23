import part6game as source
import queue
from graphviz import Digraph


def find_dead_ends(states):
    reverse_states = dict.fromkeys(states)
    dead_ends = []

    for node in states:
        for connected_node in states[node]:
            if reverse_states[connected_node] is not None:
                reverse_states[connected_node].append(node)
            else:
                reverse_states[connected_node] = [node]

    winnable = set()
    nodes_to_check = queue.Queue()
    for state in states:
        if state[0] == source.GOAL:
            nodes_to_check.put(state)
            winnable.add(state)

    while not nodes_to_check.empty():
        step = nodes_to_check.get()
        for connected_room in reverse_states[step]:
            if connected_room in winnable:
                continue
            winnable.add(connected_room)
            nodes_to_check.put(connected_room)

    for state in states:
        if state not in winnable:
            dead_ends.append(state)

    return dead_ends


def make_model(game, start_state):
    states = dict()

    def iterate(current_state):
        nonlocal states
        if current_state in states:
            return

        states[current_state] = list()
        options = game[source.get_current_room(current_state)]
        for option in options:
            next_state = options[option](current_state)
            states[current_state].append(next_state)
            iterate(next_state)

    iterate(start_state)
    dead_ends = find_dead_ends(states)

    dot = Digraph("Possible states")
    graph_keys = list(states.keys())
    for state in states:
        n = graph_keys.index(state)
        if state == start_state:
            dot.node(f'n{n}', style="filled", fillcolor="dodgerblue", shape="circle")
        elif source.is_goal_state(state):
            dot.node(f'n{n}', style="filled", fillcolor="green", shape="circle")
        elif state in dead_ends:
            dot.node(f'n{n}', style="filled", fillcolor="red", shape="circle")
        else:
            dot.node(f'n{n}', shape="circle")
    for state1 in states:
        n1 = graph_keys.index(state1)
        for state2 in states[state1]:
            n2 = graph_keys.index(state2)
            dot.edge(f'n{n1}', f'n{n2}')
    print(dot.source)


make_model(source.game, source.START_STATE)
