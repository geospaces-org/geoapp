import os

print ("Initializing example_app folder: " + os.getcwd())
if (os.path.exists("blogs/services.py")):
    from . import services
else:
    print("Blogs Services file does not exist")
    