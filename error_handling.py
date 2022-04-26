name = 'Daniel'
print(f"{name} is asking:"
      f"What do you want for dinner?")
fruits = ['apple', 'pear', 'orange', 'pineapple', 'Watermelon']

for i in range(6):
    try:
        print(fruits[i])
    except IndexError:
        print('Range too big')

try:
    print(non_declared_variable)
except:
    print('The variable was not declared ya dingus')

x = -1
if x < 0:
    raise Exception('No numbers below zero')

name = 'Daniel'
if not isinstance(name, float):
    raise TypeError(f'{name} was not a float data type.')


class Thing:

    def __init__(self):
        pass

    def does(self):
        errors = []
        self._add_error(errors)
        print(errors)

    @staticmethod
    def _add_error(errors):
        errors.append('something')
        return errors
