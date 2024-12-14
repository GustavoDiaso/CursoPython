"""
count é um objeto iterável que não possui fim

"""

import itertools

for i in itertools.count():
    print(i)
    if i == 10:
        break
