import os

print ("Initializing example_app folder: " + os.getcwd())
if (os.path.exists("stocks/services.py")):
    from . import services
else:
    print("Services file does not exist")
    