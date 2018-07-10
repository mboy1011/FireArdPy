import pyrebase
from pyfirmata import Arduino, util
from time import sleep
import getpass

## Credentials for Firebase Account
config = {
	"apiKey": "AIzaSyA5qDzIcT3nsfha6yE4lH_7rbf3JjoQkHM",
	"authDomain": "colors-45ade.firebaseapp.com",
	"databaseURL": "https://colors-45ade.firebaseio.com",
	"storageBucket": "colors-45ade.appspot.com"
}

firebase = pyrebase.initialize_app(config)

# Authentication
# email = "user@firebase.com"
# password = "user1234"

# Get a reference to the auth service
auth = firebase.auth()

# Input Firebase Credentials
print("\033[0;33;48mFire\033[0;34;48mArd\033[0;37;48mPy")
email = input("\033[0;37;48mEmail: ")
password = getpass.getpass(prompt='Password:')

# Log the user in
user = auth.sign_in_with_email_and_password(email, password)

# Get a reference to the database service
db = firebase.database()

gr = db.child("colors").child("green").get(user['idToken'])
bl = db.child("colors").child("blue").get(user['idToken'])
re = db.child("colors").child("red").get(user['idToken'])

# Ports for Arduino
## Windows ##
# board = Arduino('COM5')
## Linux ##
board = Arduino('/dev/ttyACM0')

# Pin Code
r = 13
g = 12
b = 8



if gr.val() == 1:
	board.digital[g].write(1)
	print("Green is On")
else:
	board.digital[g].write(0)
	print("Green is Off")
if bl.val() == 1:
	board.digital[b].write(1)
	print("Blue is On")
else:
	board.digital[b].write(0)
	print("Blue is Off")
if re.val() == 1:
	board.digital[r].write(1)
	print("Red is On")
else:
	board.digital[r].write(0)
	print("Red is Off")