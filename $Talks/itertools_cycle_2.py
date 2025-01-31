import time
from itertools import cycle

lights = [
    ('Green', 2),
    ('Yellow', 0.5),
    ('Red', 2)
]

colors = cycle(lights)
while True:
    c, s = next(colors)
    print(c)
    time.sleep(s)

'''changed from a "c" style loop to a pythonic style iterator'''