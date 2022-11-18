# pritice: https://pythongeeks.org/namedtuple-in-python/

import collections

Student = collections.namedtuple('Student', ['name', 'age', 'DBO'])

S = Student('Nandini', '32', '43904890')

print('The Student age using index is: ', end="")
print(S[1])

print('The Student name using keyname is :', end="")
print(S.name)

print('The Student DBO using getattr() is : ', end="")
print(getattr(S, 'DBO'))

print(getattr(S, 'name'))

print(S._fields)
print(S._replace(name='Manjeet'))

