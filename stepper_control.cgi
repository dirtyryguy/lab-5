#!/usr/bin/python37all
import cgi
import cgitb
import json
cgitb.enable()

path = '/home/pi/Documents/ENME441/labs/stepper_control.txt'

data = cgi.FieldStorage()
data = {'zero':'zero' in data, 'angle':data.getvalue('angle')}

with open(path, 'w') as f:
    json.dump(data, f)

print('Content-type:text/html\n\n')
print(
'''
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
	  height: 375px;
      margin: 0 auto;
      border: 5px outset black;
      background-color: white;
      text-align: center;
    }
	.aframe
    {
      display: block;
	  width: 100%;
	}
  </style>
</head>

<body>
  <br>
  <div class="aDiv">
    <h2>Stepper Controller</h2>
    <iframe width="450"
		    height="260"
		    style="border: 2px solid red; margin-left: 30;"
		    align="left"
		    src="https://thingspeak.com/channels/1549475/charts/1?bgcolor=%23ffffff
                 &color=%23d62020&dynamic=true&results=60&type=line&update=15">
    </iframe>
    <iframe width="449"
		    height="259"
		    style="border: 1px solid red; margin-right: 30;"
		    align="right"
		    src="https://thingspeak.com/channels/1549475/widgets/372562">
    </iframe>
  </div>
  <div style="text-align: center">
    <form action="/cgi-bin/stepper_control.cgi" method="POST">
      <br>
	  Angle Control:
      <input type="text" name="angle">
      <input type="submit" value="Submit">
      <input type="submit" name="zero" value = "Zero">
    </form>
  </div>
</body>
</html>
'''
)
