#!/usr/bin/python

print "Hello, Python!"

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise Networkerror("Bad hostname")
except Networkerror,e:
    print e.args

raw_input("\n\nPress the enter key to exit.")

if True:
    print "Answer"
    print "True"
else:
    print "Answer"
print "False"


a = b = c = 1

print a
print b
print c

b = b+1

print a
print b
print c


dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values
print dict.keys()
print dict.values()