# If you want to call other files from here itself, we need to import some of the modules

import subprocess

# subprocess.call
# subprocess.check_call

# the above methods are legacy ones! 
result = subprocess.run(["ls", "-l"])

print(type(result)) #it is a class of subprocess.CompletedProcess
