import part6game as source
import itertools
import graphviz

def make_model(game, start_state):
    locations = game.keys()
    events = [1, 2]
    for room in game:
        if 'toggle' in game[room]:
            events.append(room + "toggle")
    for i in itertools.product(locations, events):
        print(i)


make_model(source.game, source.START_STATE)
