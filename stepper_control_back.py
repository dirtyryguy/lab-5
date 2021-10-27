import json
from stepper import Stepper
import time
from urllib.request import urlopen
from urllib.parse import urlencode

stp = Stepper()

api = 'ONPVLC2A2X1X14GG'
path = 'stepper_control.txt'

try:
    timer = time.time()
    while 1:
        with open(path, 'r') as f:
            data = json.load(f)

        if int(data['zero'])
            stp.zero()

        if time.time() - timer > 15.1:
            params = {1:stp.curr_angle, 'api_key':api}
            params = urlencode(params)
            url = 'https://api.thingspeak.com/update?' + params
            urlopen(url)
            timer = time.time()

        stp.goAngle(float(data['angle']))
        print(f'Zeroing: {int(data['zero'])}, Angle Set: {float(data['angle'])}')
        time.sleep(0.1)

except KeyboardInterrupt:
    print('\nExiting')

except Exception as e:
    print(f'\nExiting because of {e}')

finally:
    gpio.cleanup()
