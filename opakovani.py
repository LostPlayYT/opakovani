import random

pole1 = []
pole2 = []

def nahodny_pocet ():
    global pole1
    global pole2
    for i in range(random.randint(1,10)):
        pole1.append(random.randint(1,20))
    for a in range(random.randint(1,10)):
        pole2.append(random.randint(1,20))

nahodny_pocet()

if len(pole1) > len(pole2):
    print ("")