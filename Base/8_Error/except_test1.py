#! /usr/bin/python

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except (ValueError, RuntimeError, TypeError, NameError):
        #pass         #继续执行(不打印任何信息)
        print("Oops!  That was no valid number. Try again...")

print ("You had entered The Number: ", x)
