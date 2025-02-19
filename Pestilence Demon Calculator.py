import math
import time

for x in range(20):
    print()

print("###PESTILENCE DEMON CALCULATOR###")

x = float(input("your life: "))  
y= float(input("highest health amongst opponents: "))

oddtriggers=math.floor(x/3)
3#EDGE CASE OF ONLY BEING ABLE TO AFFORD 1 TRIGGER

#TRIGGERS I CAN AFFORD
if x % 3 == 0:
    ##########print("you can afford", int((x/3)-1), "triggers")
    triggers=int((x/3)-1)
else:
    #########print("you can afford",oddtriggers, "triggers")
    triggers=int(oddtriggers)
#GIVES triggers allowed

if x % 2 == 0:
    healthneeded=math.floor(3*y-x+1)
elif x % 2 != 0:
    healthneeded=math.floor(3*y-x+1)

mananeeded=math.ceil(healthneeded/2)
ynew=y-mananeeded

#if sufficient health for lethal damage
if triggers >= y:
    print("you can win.")
    time.sleep(2)
    print("spend",int(3*y), "life to deal",int(y), "damage to every player and creature.")
    time.sleep(0.5)
    print("you will have",int(x-3*y), "life remaining.")

#if not enough for lethal 
#each mana i tap saves 2 life
if triggers < y:
    answer = input(f"dou need {mananeeded} mana to win. do you have it? (y/n) ")
    if answer == "y":
        time.sleep(0.5)
        print("win with",int(mananeeded),"mana and pay",int(3*ynew),"life w/ k'riik to do",mananeeded,"+",int(ynew),"=",int(ynew+mananeeded), "damage.")
        print("you will have:",int(x),"-",mananeeded,"-",int(3*ynew),"=",int(x-mananeeded-3*ynew),"life remaining.")
    elif answer == "n":
        print("damn sucks to suck.")
    else:
        print("that is not 'y' or 'n'")
   
    