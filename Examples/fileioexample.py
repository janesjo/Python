#!/usr/bin/python

class Weapon():
    def __init__ (self):
        self.name = ""
        self.damage = 0
        self.health = 0

    def read(self, fo):
        self.name = fo.readline().rstrip()
        self.damage = int(fo.readline())
        self.health = int(fo.readline())

    def write(self, fo):
        fo.writelines(self.name + "\n")
        fo.writelines(str(self.damage) + "\n")
        fo.writelines(str(self.health) + "\n")

# Weapon List
lw = []

# Create weapons
lw.append(Weapon())
lw[0].name = "Sword"
lw[0].damage = 100
lw[0].health = 1000

lw.append(Weapon())
lw[1].name = "Dagger"
lw[1].damage = 10
lw[1].health = 100

lw.append(Weapon())
lw[2].name = "Staff"
lw[2].damage = 1000
lw[2].health = 10

# Open a file
fo = open('foo.txt', 'w')

# Write weapons to disk
fo.writelines(str(len(lw)) + "\n") # Number of weapons
for w in lw:
    w.write(fo)

# Close file
fo.close()

# Open a file
fo = open('foo.txt', 'r')

wc = int(fo.readline())

lw2 = []
for i in range(0,wc):
    lw2.append(Weapon())
    lw2[i].read(fo)

fo.close()
