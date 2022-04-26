# class Employee:
#     num_of_emps = 0
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
#
#         Employee.num_of_emps += 1
#
#     def fullname(self):
#         return f'{self.first} {self.last}'
#
#     def apply_raise(self):
#         self.pay *= self.raise_amt
#
#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amt = amount
#
#     @classmethod
#     def an_amployee(cls):
#         print('an_employee ' + str(cls.num_of_emps))
#
#     @staticmethod
#     def a_static_employee():
#         print('static employee ' + str(Employee.raise_amt))
#
#
# Employee.an_amployee()
# Employee.a_static_employee()

import staticmethod
staticmethod.Music.play()
staticmethod.Music.next_track()

stop_music = staticmethod.Music()
stop_music.stop()
