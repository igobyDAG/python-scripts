from enum import Enum


class Animal(Enum):
    dog = 1
    cat = 2
    bird = 3


print('all enum values are: ')
for animal in Animal:
    print(animal)

# d = {}
# d[Animal.dog] = 'bark'
# d[Animal.bird] = 'chirp'
# d[Animal.cat] = 'nya'
# print(d)
#
# if d == {Animal.dog: 'bark', Animal.cat: 'nya', Animal.bird: 'chirp'}:
#     print('Enum is hashed')
# else:
#     print('aint hashed')
#
# print('the enum value associatied with 2 is:')
# print(Animal(2))
#
# # Assinging Enum member
# mem = Animal.dog
# print('mem values associated with Dog:')
# print(mem.value, mem.name)
