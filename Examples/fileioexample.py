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

# Weapons List
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

lw.append(Weapon())
lw[3].name = "Spear"
lw[3].damage = 200
lw[3].health = 5000

lw.append(Weapon())
lw[4].name = "Axe"
lw[4].damage = 50
lw[4].health = 300

lw.append(Weapon())
lw[5].name = "Hammer"
lw[5].damage = 5000
lw[5].health = 50

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
