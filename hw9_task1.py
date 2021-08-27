import time
from itertools import cycle
from termcolor import colored

class TrafficLight:
    __color = 'red'

    def running(self):
        cyc = cycle(['red', 'yellow', 'green'])
        cyc_sec = cycle([7, 2, 3])
        i = 0
        while i < 20:
            self.__color = next(cyc)
            print(colored(self.__color, self.__color))
            time.sleep(next(cyc_sec))
            i += 1

a = TrafficLight()
a.running()
