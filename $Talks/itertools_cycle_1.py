'''
from
https://youtube.com/shorts/Ht_LdGroNZE?si=KYYVhjR_e5R-n8-p
'''
import time

lights = [
    ('Green', 2),
    ('Yellow', 0.5),
    ('Red', 2)
]

i = 0

while True:
    c, s = lights[i]
    print(c)
    time.sleep(s)

    if i == len(lights) - 1:
        i = 0
    else:
        i += 1
'''
tuple reversal from jeremy        
x,y=y,x
'''