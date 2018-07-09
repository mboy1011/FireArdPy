# import pyrebase
from pyfirmata import Arduino, util
from time import sleep

# # Credentials for Firebase Account
# config = {
# 	"apiKey": "AIzaSyA5qDzIcT3nsfha6yE4lH_7rbf3JjoQkHM",
# 	"authDomain": "colors-45ade.firebaseapp.com",
# 	"databaseURL": "https://colors-45ade.firebaseio.com",
# 	"storageBucket": "colors-45ade.appspot.com"
# }

# firebase = pyrebase.initialize_app(config)

# #Authentication
# email = "elliot@fsociety.com"
# password = "root@fsoc.py~#"

# # Get a reference to the auth service
# auth = firebase.auth()

# # Log the user in
# user = auth.sign_in_with_email_and_password(email, password)

# # Get a reference to the database service
# db = firebase.database()

# c = db.child("colors").get()

# print(c.val())



# Port for Arduino
board = Arduino('/dev/ttyACM0')

# Pin 13 On
board.digital[13].write(1)

sleep(1)

# Pin 13 Off
board.digital[13].write(0)
