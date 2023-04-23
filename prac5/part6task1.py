import part6game as source
from graphviz import Digraph


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
    dot = Digraph("Possible states")
    graph_keys = list(states.keys())
    for state in states:
        n = graph_keys.index(state)
        if state == start_state:
            dot.node(f'n{n}', style="filled", fillcolor="dodgerblue", shape="circle")
        elif source.is_goal_state(state):
            dot.node(f'n{n}', style="filled", fillcolor="green", shape="circle")
        else:
            dot.node(f'n{n}', shape="circle")
    for state1 in states:
        n1 = graph_keys.index(state1)
        for state2 in states[state1]:
            n2 = graph_keys.index(state2)
            dot.edge(f'n{n1}', f'n{n2}')
    print(dot.source)


make_model(source.game, source.START_STATE)
