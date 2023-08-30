import os

print ("Initializing geospaces folder: " + os.getcwd())
if (os.path.exists("geospaces/services.py")):
    from . import services
else:
    print("Services file does not exist")
    
