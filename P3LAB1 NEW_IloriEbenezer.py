# cti 110
# P3LAB1
# Ilori
# 10/22/24

def main():
    print("Choose your own adventure")
    front_door()
    Once_inside()
    Second_floor()
    Floor_cleared()

def front_door():
    print("You decide to go inside.")
    print("But should you knock?")
    print("1. Go inside")
    print("2. Knock door")
    choice = int(input())
    if choice == 1:
        Go_inside()
    elif choice == 2:
        Knock_door()

def Go_inside():
    print("Not good")

def Knock_door():
    print("Great idea")

def Once_inside():
    print("You decide to go upstairs!.")
    print("Should you scan your surrounding?")
    print("1. Go upstairs")
    print("2. Scan your surrounding!")
    choice = int(input())
    if choice == 1:
        Go_upstairs()
    elif choice == 2:
        scan_surrounding()

def Go_upstairs():
    print("Not good")
    print("***Take Caution***")

def scan_surrounding():
    print("Be Vigilant!")
    print("***Ready Arm***")

def Second_floor():
    print("You are upstairs!.")
    print("Should you clear the first room?")
    print("Start clearing from the rear room")
    print("1. Start clearing first room!")
    print("2. Begin clearing from the rear")
    choice = int(input())
    if choice == 1:
        Clear_first()
    elif choice == 2:
        Clear_rear()

def Clear_first():
    print("Fantastic")
    print("***Take Caution***")

def Clear_rear():
    print("Not safe!")

def Floor_cleared():
    print("Mount surveillance cameras!.")
    print("Should you make camera visible?")
    print("May be conceal camera")
    print("1. Make camera visible!")
    print("2. Conceal camera!")
    choice = int(input())
    if choice == 1:
        Make_visible()
    elif choice == 2:
        Conceal_camera()

def Make_visible():
    print("Not a good idea")


def Conceal_camera():
    print("Good choice!")
    print("...MISSION COMPLETE...!")

#start the program
main()
