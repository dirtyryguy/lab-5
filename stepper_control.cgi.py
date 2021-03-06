#!/usr/bin/python37all
import cgi
import json

path = '/home/pi/Documents/ENME441/labs/stepper_control.txt'

data = cgi.FieldStorage()
data = {'zero':'zero' in data, 'angle':data.getvalue('angle')}

with open(path, 'w') as f:
    json.dump(data, f)

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
