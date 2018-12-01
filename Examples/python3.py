#!/usr/bin/python

# Open a file
fo = open('foo.txt', 'w')

# Write a int
intVal = 1
strIntVal = str(intVal)
fo.writelines(strIntVal + "\n")

# Write a string
stringVal = "Hejsan"
fo.writelines(stringVal + "\n")

fo.close()

# Open a file
fo = open('foo.txt', 'r')

intVal2 = int(fo.readline())
stringVal2 = fo.readline().rstrip()

fo.close()
