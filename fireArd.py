import pyrebase
from pyfirmata import Arduino, util
from time import sleep

# # Credentials for Firebase Account
config = {
	"apiKey": "AIzaSyA5qDzIcT3nsfha6yE4lH_7rbf3JjoQkHM",
	"authDomain": "colors-45ade.firebaseapp.com",
	"databaseURL": "https://colors-45ade.firebaseio.com",
	"storageBucket": "colors-45ade.appspot.com"
}

firebase = pyrebase.initialize_app(config)

#Authentication
email = "elliot@fsociety.com"
password = "root@fsoc.py~#"

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(email, password)

# Get a reference to the database service
db = firebase.database()

gr = db.child("colors").child("green").get()
bl = db.child("colors").child("blue").get()
re = db.child("colors").child("red").get()

# print(gr.val())



# Port for Arduino
## Windows ##
board = Arduino('COM5')
## Linux ##
#board = Arduino('/dev/ttyACM0')

# Pin Code
r = 13
g = 12
b = 8


if gr.val() == 1:
	board.digital[g].write(1)
	print("Green is On")
elif bl.val() == 1:
	board.digital[b].write(1)
	print("Blue is On")
elif re.val() == 1:
	board.digital[r].write(1)
	print("Red is On")
else:
	board.digital[g].write(1)
	board.digital[r].write(1)
	board.digital[b].write(1)
	print("Off")