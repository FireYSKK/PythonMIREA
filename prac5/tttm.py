from typing import NamedTuple


class State(NamedTuple):
    player: str
    alice: str
    bob: str
    red_key: str
    blue_key: str
    green_key: str


# Функция перехода из комнаты в комнату.
# Возвращает лист НОВЫХ состояний, т.е. отбрасывает варианты,
# ведущие в текущее состояние (переходы, не имея нужного ключа)
def go(room, req):
    def func(state):
        # Персонаж не уйдет из своей комнаты
        if state[0] == 'alice' and state[1] == 'red room':
            return []
        if state[0] == 'bob' and state[1] == 'blue room':
            return []

        states = []
        new_state = list(state)
        player_ind = ['alice', 'bob'].index(state[0]) + 1
        req_ind = ['red_key', 'blue_key', 'green_key'].index(req) + 3
        if new_state[player_ind] == new_state[req_ind]:
            new_state[player_ind] = room
            new_state[req_ind] = room
            states.append(State(*new_state))
            for i in range(1, 3):
                if new_state[((req_ind + i) % 3) + 3] == state[player_ind]:
                    new_state[((req_ind + i) % 3) + 3] = room
                    states.append(State(*new_state))

        return states

    return func


def switch_player():
    def func(state):
        new_state = list(state)
        players = ['alice', 'bob']
        ind = (players.index(state[0]) + 1) % 2
        new_state[0] = players[ind]
        return [State(*new_state)]

    return func


# Структура игры. Комнаты и допустимые в них действия
game = {
    'east room': dict(
        up=go('blue room', 'blue_key'),
        left=go('west room', 'green_key'),
        switch=switch_player()
    ),
    'west room': dict(
        up=go('red room', 'red_key'),
        right=go('east room', 'green_key'),
        switch=switch_player()
    ),
    'red room': dict(
        down=go('west room', 'red_key'),
        switch=switch_player()
    ),
    'blue room': dict(
        down=go('east room', 'blue_key'),
        switch=switch_player()
    )
}

# Стартовое состояние
START_STATE = State(
    player='alice',
    alice='west room',
    bob='east room',
    red_key='east room',
    blue_key='west room',
    green_key='east room'
)


def is_goal_state(state):
    """
    Проверить, является ли состояние целевым.
    """
    return state.alice == 'red room' and state.bob == 'blue room'
