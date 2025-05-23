
import os
# **Exception Handling **

# Take user input for two integers and divide them. Handle: ValueError if input is not an integer, ZeroDivisionError for division by zero.
try: 
    a,b=input().split(" ")
    print(int(a)/int(b))
except ZeroDivisionError:
    print("value should be greater than zero")


# Try to open a file named important_config.txt. If it doesn’t exist, print "Config file not found!" instead of crashing.
try:
    with open("important_config.txt",'r') as fr:
        print(fr.read())
except FileNotFoundError:
    print("Config file not found!")

# Modify the previous task and add a finally block to print "Operation complete" no matter what happens.
try:
    with open("important_config.txt",'r') as fr:
        print(fr.read())
except FileNotFoundError:
    print("Config file not found!")
finally:
    print("Operation complete")

# Create a custom exception class InvalidPortException. Raise it if a given port number is not in the range 1-65535
class InvalidPortError(Exception):
    def __int__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
port=int(input())
try:
    if not(port >=1 and port <=65535):
        raise InvalidPortError
except InvalidPortError:
    print("port no not in range")



# Try to delete a file using os.remove() and handle PermissionError, FileNotFoundError, and generic OSError
try:
    os.remove("file.txt")
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("no enough permission to delet the file")
except OSError:
    print("os issue")