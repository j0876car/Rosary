from mysteries import Glorious_mystery
from mysteries import Luminmous_mystery
from rosary_begin import *
from conclusion import ending_prayers
import time
import os
import conclusion
_day=time.strftime('%A')
#The start of the Rosary
sign_of_the_cross()
Apostle_Creed()
os.system('cls')
Our_Father()
os.system('cls')
hail_mary_begin(4)
os.system('cls')
glory_be()
os.system('cls')
#
#
#
#
#start of mysteries
if _day in ['Monday','Saturday']:
    print(_day, 'is the Joyful mystery')
elif _day in ['Tuesday','Friday']:
    print(_day, 'is the sorrowful mystery')
elif _day in ['Wednesday','Sunday']:
    Glorious_mystery()

else:
    print(_day, 'is the Luminous mystery\n')
    Luminmous_mystery()
    ending_prayers()