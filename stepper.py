# Add to PYTHONPATH
import RPi.GPIO as gpio
import time
from multiprocessing import shaerd_memory

gpio.setmode(gpio.BCM)

# seq = (1, 3, 2, 6, 4, 12, 8, 9) # tuple 'cause no change. Is this worth the speed?? No...
seq = ((0,0,0,1),
       (0,0,1,1),
       (0,0,1,0),
       (0,1,1,0),
       (0,1,0,0),
       (1,1,0,0),
       (1,0,0,0),
       (1,0,0,1)) # WHAAAAA
CONST_ANGLE_STEP = 360/512

class Stepper:
    """

    """

    def __init__(
                 self,
                 pins=(18, 21, 22, 23), # tuples > lists
                 led_pin=24
                 ):
        """

        """

        self.pins = pins
        for pin in self.pins:
            gpio.setup(pin, gpio.out, initial=0)

        self.curr_angle = 0.0
        self.curr_step = 0
        self.__update()

    def __update(self):
        """

        """

        temp = seq[self.curr_step]
        for n, pin in enumerate(self.pins):
            gpio.output(pin, temp[n])


    def __halfstep(self, rot_dir): # 0 for cw, 1 for ccw
        """

        """

        s = self.curr_step
        if rot_dir:
            self.curr_step = s - 1 if s > 0 else 7 # why
            self.curr_angle += CONST_ANGLE_STEP
        else:
            self.curr_step = s + 1 if s < 7 else 0 # idk
            self.curr_angle -= CONST_ANGLE_STEP
        self.__update()


    def __turnsteps(self, steps, rot_dir):
        """

        """

        for _ in range(steps):
            self.__halfstep(rot_dir)
            time.sleep(0.001)


    def goAngle(self, ang): # Degrees even though I dislike them
        """

        """

        diff = ang - self.curr_angle
        self.__turnsteps(int(diff/CONST_ANGLE_STEP), diff>0) # proud of this


    def zero(self):
        pass
