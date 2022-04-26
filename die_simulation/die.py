from random import randint
from matplotlib.pyplot import bar, show


class Die:
    '''Pass input value for number of sides of die.'''
    def __init__(self,sides) -> None:
        self.sides = [str(i) for i in range(sides+1)]

    def simulate(self,throws):
            return [self._throw_die() for i in range(throws)]
    
    def _throw_die(self):
        return self.sides[randint(1,len(self.sides)-1)]

    def graph_display(self, simulation):
        bar(self.count_ocurrences(simulation).keys(), self.count_ocurrences(simulation).values())
        show()

    def count_ocurrences(self, simulation):
        side_count = {}
        for side in self.sides:
            if side not in side_count:
                side_count.setdefault(side,simulation.count(side))
        side_count.pop('0')
        return side_count
 