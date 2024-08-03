# cla -> Command line arguments. 

import sys
print(sys.argv) #it prints all the values you pass at the command line level

if len(sys.argv) == 1:
    print("USAGE: python3 app.py <password>")
