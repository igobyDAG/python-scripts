#base class
class State:
    def __init__(self):
        print('In the state class')
        self.state1 = 'Main state'

#base class 2
class Event:
    def __init__(self):
        print('In the event class')
        self.event = 'Main Event'


class HappyState(State, Event):
    def __init__(self):
        print('In the happy state class')
        self.state2 = 'Happy State'
        super().__init__()
        super(State, self).__init__()


a = HappyState()
# print(a.state1)
# print(a.state2)