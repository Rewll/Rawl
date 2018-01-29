#Chapter 1 


#Imported Modules
import time 
import random

#String Variables
RING = "*RING* *RING* *RING*"

#Integer Variables

    
#Boolean Variables
running = True


#Lists
sarcasm = ["It seems that Henry has found a new hobby.", "It seems like Henry was enjoying this.", "Poor alarm clock.", "What did the alarm clock ever do to Henry?"]


#Main Code
print(RING)
time.sleep(2)
print("Henry woke up very tired.")
time.sleep(2)
print("He did not get much sleep.")
time.sleep(2)
print("This was obviously because of what was happening today.")
time.sleep(2)
print(RING)
time.sleep(2)
choice1 = int(input("Type 1 to smash the alarm clock\nType 2 to ignore the alarm\nType 3 to get out of bed.\n"))

if choice1 == 1:
    print(RING)
    time.sleep(3)
    print("Henry smashed the alarm clock.")
    time.sleep(3)
    print("The alarm clock broke in a lot of pieces.")
    time.sleep(3)
    print("The room went quiet for 10 seconds.")
    time.sleep(3)
    print("The smash was not really helpfull, the alarm fixed itself.")
    time.sleep(3)
    print(RING)
    choice2 = int(input("Type 1 to smash the alarm clock again.\nType 2 to get out of bed.\n"))
    if choice2 == 1:
        while running:
            print(RING)
            time.sleep(2)
            print("Henry smashed the alarm clock again.")
            time.sleep(2)
            print("The alarm fixed itself almost instantly.")
            time.sleep(2)
            print(random.choice(sarcasm))
            time.sleep(3)
            print(RING)
            choice3 = int(input("Type 1 to smash the alarm clock again.\nType 2 to get out of bed.\n"))
            if choice3 == 1:
                continue
            elif choice3 == 2:
                break
    if choice2 == 2:
        print("Henry stood up.")



if choice1 == 2:
    print(RING)
    time.sleep(3)
    print("Because of the messing around with illegal substances from 6 months ago.")
    print("He has to show his clarification to the goverment today.")
    print(RING)
    time.sleep(3)
    print("Henry has prepared a lot, he has made a long and clear explanation.")
    time.sleep(3)
    print("He has prepared a lot of evidence of why he had done it.")
    time.sleep(3)
    print(RING)
    time.sleep(2)
    print("Henry has a good feeling about it.")
    time.sleep(2)
    print("The presentation is in 10 earth hours, so he has time to prepare.")
    time.sleep(2)
    print(RING)
    choice4 = int(input("Type 1 to get out of bed\nType 2 to smash the alarm clock.\n"))
    if choice4 == 1:
        print("Henry stood up.")
    if choice4 == 2:
            while running:
                print(RING)
                time.sleep(2)
                print("Henry smashed the alarm clock again.")
                time.sleep(2)
                print("The alarm fixed itself almost instantly.")
                time.sleep(2)
                print(random.choice(sarcasm))
                time.sleep(3)
                print(RING)
                choice3 = int(input("Type 1 to smash the alarm clock again.\nType 2 to get out of bed.\n"))
                if choice3 == 1:
                    continue
                elif choice3 == 2:
                    break
     
    
if choice1 == 3:
    print("Henry stood up.")
    time.sleep(2)
    
print("The alarm clock stopped ringing.")
time.sleep(2)   
choice5 = int(input("Type 1 to look out of the window\nType 2 to get dressed\nType 3"))

if choice5 == 1:
    print("Henry pushed on a small black button.")
    time.sleep(2)
    print("Where there was a solid wall a few seconds ago, there now appeared a big squared window.")
    time.sleep(4)
    print("The view was stunning.")
    time.sleep(2)
    print("Henry took a second to admire the view.")
    time.sleep(2)
    print("")