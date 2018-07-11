# ![FireArdPy](https://github.com/mboy1011/FireArdPy/blob/master/FireArdPy.png)
<p><b>FireArdPy</b> is an Arduino Based Project to connect from Firebase using Python3.</p>

## Prerequisite:
> * Basic knowledge to Programming (Python).
> * Basic knowledge of NoSQL databases since Firebase is a NoSQL.
> * Basic knowledge of Electronics.


## Requirements:
[![Python3](https://www.python.org/static/img/python-logo.png)](https://www.python.org/downloads/)
[![Arduino Uno R3 Kit](https://www.arduino.cc/favicon.ico)](https://store.arduino.cc/usa/arduino-starter-kit)
[![Firebase Account](https://www.gstatic.com/mobilesdk/160503_mobilesdk/logo/2x/firebase_28dp.png)](https://console.firebase.google.com/)

## Installation:
1. Connect your Arduino Uno R3 to your computer.
2. Upload a Standard Firmata on your Arduino using Arduino IDE.
3. Install requirements for Python3:
	<br><code>pip install -r requirements.txt</code>
	<br><code>pip3 install -r requirements.txt</code>
4. Go to console.firebase.google.com and fill out the configuration needed by the Pyrebase.
5. Copy this rule to your Firebase Database Rules and Publish:
	<code>
	```json
	{
		"rules": {
			".read": "auth != null",
			".write": "auth != null"
		}
	}
	```
	</code>
6. Follow the Circuit Diagram:
![Diagram](https://github.com/mboy1011/FireArdPy/blob/master/Circuit%20Diagram.png)
7. Run command:
	<br><b>Windows</b></br>
	<code>python fireArd.py</code>
	<br><b>Linux</b></br>
	<code>python3 fireArd.py</code>
8. Enter this Sample Account:
	<br><b>Email:</b> <i>user@firebase.com</i>
	<br><b>Password:</b> <i>user1234</i>
##
[![Compatibility](https://img.shields.io/badge/python-3-brightgreen.svg)](https://github.com/mboy1011/FireArdPy.git)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/mboy1011/FireArdPy.git)


