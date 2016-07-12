#! /usr/bin/python

class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.arg = arg

 
try:
   raise Networkerror("Bad hostname")
except Networkerror as e:
   print ("Catch Exception: " ,e.arg)
