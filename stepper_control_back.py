from multiprocessing import shaerd_memory
from stepper import Stepper
import time
from urllib.request import urlopen
from urllib.parse import urlencode

shm = shared_memory.SharedMemory(name='stepper', create=True, size=11) # one byte for zeroing, ten for angle data
buffer = shm.buf

stp = Stepper()

api = 'ONPVLC2A2X1X14GG'

try:
    timer = time.time()
    while 1:
        if buffer[0]:
            stp.zero()
            buffer[0] = 0

        if time.time() - timer > 15.1:
            params = {1:stp.curr_angle, 'api_key':api}
            params = urlencode(params)
            url = 'https://api.thingspeak.com/update?' + params
            urlopen(url)
            timer = time.time()

        stp.goAngle(float(buffer[1:]))
        print(f'Zeroing: {buffer[0]}, Angle Set: {float(buffer[1:])}')
        time.sleep(0.1)

except KeyboardInterrupt:
    print('\nExiting')

except Exception as e:
    print(f'\nExiting because of {e}')

finally:
    gpio.cleanup()
    shm.close()
    shm.unlink()
