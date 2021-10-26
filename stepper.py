import RPi.GPIO as gpio
import time

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


    # def zero(self):
    #     pass









"""
pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4
for pin in pins:
    GPIO.setup(pin, GPIO.OUT, initial=0)

# Define the pin sequence for counter-clockwise motion, noting that
# two adjacent phases must be actuated together before stepping to
# a new phase so that the rotor is pulled in the right direction:
ccw = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
        [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
# Make a copy of the ccw sequence. This is needed since simply
# saying cw = ccw would point both variables to the same list object:
cw = ccw[:]  # use slicing to copy list (could also use ccw.copy() in Python 3)
cw.reverse() # reverse the new cw sequence

def delay_us(tus): # use microseconds to improve time resolution
    endTime = time.time() + float(tus)/ float(1E6)
    while time.time() < endTime:
        pass

# Make a full rotation of the output shaft:
def loop(dir): # dir = rotation direction (cw or ccw)
    for i in range(512): # full revolution (8 cycles/rotation * 64 gear ratio)
        for halfstep in range(8): # 8 half-steps per cycle
            for pin in range(4):    # 4 pins that need to be energized
                GPIO.output(pins[pin], dir[halfstep][pin])
            delay_us(1000)
try:
    loop(cw)
    loop(ccw)
except:
    pass
GPIO.cleanup()
"""
