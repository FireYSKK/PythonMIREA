# Функция перехода из комнаты в комнату
def go(room, req):
    def func(state):
        new_state = state.copy()
        active_player = players[state['player']]
        if req in active_player['inventory']:
            new_state[active_player + '_room'] = room
        return new_state

    return func


def pick():
    def func(state, key):
        if key not in players[state['player']]['inventory']:
            players[state['player']]['inventory'].append(key)

    return func


def drop():
    def func(state, key):
        if key in players[state['player']]['inventory']:
            players[state['player']]['inventory'].remove(key)

    return func


# Структура игры. Комнаты и допустимые в них действия
game = {
    'east room': dict(
        up=go('blue room', 'blue_key'),
        left=go('west room', 'green_key')
    ),
    'west room': dict(
        up=go('red room', 'red_key'),
        right=go('east room', 'green_key')
    ),
    'red_room': dict(
        down=go('west room', 'red_key')
    ),
    'room3': dict(
        down=go('east room', 'blue_key')
    )
}

players = {
    'alice': dict(
        inventory=[],
        pick=pick(),
        drop=drop()
    ),
    'bob': dict(
        inventory=[],
        pick=pick(),
        drop=drop()
    )
}

# Стартовое состояние
START_STATE = dict(
    player='alice',
    alice_room='west room',
    bob_room='east room',
    red_key='east room',
    blue_key='west room',
    green_key='east room'
)
GOAL = 'room2'


def is_goal_state(state):
    """
    Проверить, является ли состояние целевым.
    """
    return state['alice_room'] == 'red room' and state['bob_room'] == 'blue room'
