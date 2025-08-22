import sys
import os

print ("Version->",sys.version)
# one way
# print("Current directory:",os.getcwd())

current_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
print("Directory->",current_directory)