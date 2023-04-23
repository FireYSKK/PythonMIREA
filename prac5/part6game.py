from typing import NamedTuple


class State(NamedTuple):
    room: str
    toggle1: int = 0
    toggle2: int = 0


# Функция перехода из комнаты в комнату
def go(room):
    def func(state):
        new_state = list(state)
        new_state[0] = room
        return State(*new_state)

    return func


# Функция действия в комнате
def toggle(ind):
    def func(state):
        new_state = list(state)
        new_state[ind] = (state[ind] + 1) % 2

        for effect in toggles[ind]:
            if effect[1] in game[effect[0]]:
                del game[effect[0]][effect[1]]
            else:
                game[effect[0]][effect[1]] = effect[2]

        return State(*new_state)

    return func


# Структура игры. Комнаты и допустимые в них действия
game = {
    'room0': dict(
        left=go('room1'),
        up=go('room2'),
        right=go('room3')
    ),
    'room1': dict(
        up=go('room2'),
        right=go('room0')
    ),
    'room2': dict(
    ),
    'room3': dict(
        up=go('room4'),
        right=go('room5')
    ),
    'room4': dict(
        down=go('room3'),
        right=go('room5')
    ),
    'room5': dict(
        up=go('room4'),
        left=go('room3')
    )
}

# Функции рычагов. Добавляются к структуре игры при активации
toggles = {
    1: [['room3', 'left', go('room0')]],
    2: [['room3', 'left', go('room0')],
        ['room5', 'right', go('room2')],
        ['room5', 'down', go('room1')],
        ['room4', 'up', go('room2')],
        ['room4', 'left', go('room0')]]
}

# Стартовое состояние
START_STATE = State(room='room0')
GOAL = 'room2'


def is_goal_state(state):
    """
    Проверить, является ли состояние целевым.
    """
    return state[0] == GOAL


def get_current_room(state):
    """
    Выдать комнату, в которой находится игрок.
    """
    return state[0]
