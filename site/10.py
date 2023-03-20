class MealyError(Exception):
    pass


class MealyMachine:
    states = {'A': {'crush': 'B', 'run': 'H'},
              'B': {'print': 'C'},
              'C': {'print': 'D', 'crush': 'C'},
              'D': {'run': 'E'},
              'E': {'run': 'C', 'print': 'F', 'crush': 'G'},
              'F': {'crush': 'G', 'print': 'H'},
              'G': {'run': 'H'}}

    outputs = {'A': {'crush': 0, 'run': 1},
               'B': {'print': 2},
               'C': {'print': 3, 'crush': 4},
               'D': {'run': 5},
               'E': {'run': 7, 'print': 6, 'crush': 8},
               'F': {'crush': 9, 'print': 10},
               'G': {'run': 11}}

    def __init__(self):
        self.state = 'A'

    def crush(self):
        if 'crush' not in self.states[self.state]:
            raise MealyError('crush')

        out = self.outputs[self.state]['crush']
        self.state = self.states[self.state]['crush']
        return out

    def print(self):
        if 'print' not in self.states[self.state]:
            raise MealyError('print')

        out = self.outputs[self.state]['print']
        self.state = self.states[self.state]['print']
        return out

    def run(self):
        if 'run' not in self.states[self.state]:
            raise MealyError('run')

        out = self.outputs[self.state]['run']
        self.state = self.states[self.state]['run']
        return out


def main():
    return MealyMachine()


def test():
    pass

o = main()
print(o.crush(),  # 0
      o.print(),  # 2
      o.print(),  # 3
      o.run(),  # 5
      o.run(),  # 7
      o.crush(),  # 4
      o.crush(),  # 4
      o.print(),  # 3
      o.run(),  # 5
      o.print(),  # 6
      o.crush(),  # 9
      o.run())  # 11

o = main()
print(o.crush(),  # 0
      o.print(),  # 2
      o.print(),  # 3
      o.run(),  # 5
      o.run(),  # 7
      o.crush(),  # 4
      o.print(),  # 3
      o.crush(),  # MealyError
      o.run(),  # 5
      o.print(),  # 6
      o.crush(),  # 9
      o.run())  # 11
