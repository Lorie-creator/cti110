# cti 110
# P3LAB1
# Ilori
# 10/22/24

def main():
    print("Choose your own adventure")
    front_door()
    Once_inside()

def front_door():
    print("You decide to go inside.")
    print("But should you knock?")
    print("1. Go inside")
    print(". Knock door")
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
    print(". Scan your surrounding!")
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

#start the program
main()

    
    
