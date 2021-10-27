#!/usr/bin/python37all
import cgi
from multiprocessing import shared_memory

shm = shared_memory.SharedMemory(name='stepper', create=False)
buffer = shm.buf

data = cgi.FieldStorage()
try:
    buffer[0] = 1 if 'zero' in data else 0
    buffer[1:] = f'{float(data.getvalue('angle')):010.6f}'.encode('utf-8')

except:
    pass

finally:
    shm.close()

print(
'''
Content-type:text/html\n\n
<html>
<head>
  <title>Stepper Control</title>
  <style>
    body
    {
      background-color: powderblue;
    }
    .aDiv
    {
      width: 1000px;
      margin: 0 auto;
      border: 5px outset black;
      background-color: white;
      text-align: center;
    }
  </style>
</head>

<body>
  <br>
  <div class="aDiv">
    <h2>Stepper Controller</h2>

    <iframe width="450" height="260" style="border: 1px solid #cccccc;
                                            float: center"
            aligh="left"
      src="https://thingspeak.com/channels/1549475/charts/1?bgcolor=%23ffffff
           &color=%23d62020&dynamic=true&results=60&type=line&update=15">
    </iframe>

    <iframe width="450" height="260" style="border: 1px solid #cccccc;"
            alight="right"
      src="https://thingspeak.com/channels/1549475/widgets/372562">
    </iframe><br>

    <form action="/cgi-bin/stepper_control.cgi" method="POST">
      Change Angle:<br><br>
      <input type="text" name="angle">
      <input type="submit" value="Submit">
      <input type="submit" name="zero" value = "Zero">
    </form>

  </div>
</body>
</html>
'''
)
