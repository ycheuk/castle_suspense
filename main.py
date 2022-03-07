from room import Room
from player import Player
from item import Item
import os
import updater
import time
from time import sleep
import sys
from routes import Routes

player = Player()
Routes = Routes()

#Shortcuts:
choice = "\n➥ "
choose = "\nChoose an option: "
command = "\nType a command: "
enter = "\n\n\n\n\nPress enter to continue..."

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def showHelpMM():
    clear()
    print("╔══════════════════════════════════════════════════════╗	")
    print("    In-Game Commands")
    print("    ────────────────")
    print('    ➣ "char" -- current characters and their \n      description')
    print('    ➣ "cont" -- go to another room')
    print('    ➣ "drop <item name>" -- drops item from your \n      inventory')
    print('    ➣ "eat <food>" -- consumes food and restores \n      sanity')
    print('    ➣ "help" -- list of commands')
    print('    ➣ "inv" -- current items held ')
    print('    ➣ "<letter>" -- chooses this option')
    print('    ➣ "map" -- shows map')
    print('    ➣ "pickup <item name>" -- moves item to your \n      inventory')
    print("╚══════════════════════════════════════════════════════╝")
    print()
    input("Enter to return to menu.\n> ")
    startUp_frozen()
    mm_commands()

def showTutorial():
    clear()
    print("╔══════════════════════════════════════════════════════╗")
    print("    Tutorial Menu")
    print("    ─────────────")
    print("    ➣ Characters - Try to be nice to the other ")
    print("      characters. They just might help you along the ")
    print("      way.")
    print("    ➣ Choices - Your choices affect the route you will ")
    print("      take. Choose carefully! Some options are better ")
    print("      than others!")
    print("    ➣ Inventory - This is where your items are being ")
    print("      stored. Your inventory does have a limit! ")
    print("    ➣ Items - Pick up items you think will be useful ")
    print("      to the murder case. You have a limited inventory, ")
    print("      so don\'t pick up useless items!")
    print("    ➣ Levels ⇧ - As you level up, you will get to ")
    print("      unlock many features.")
    print("    ➣ Rooms - There are 7 main rooms you want to go to. ")
    print("      This does not include the castle courtroom, ")
    print("      corridor, and penetralium.")
    print("    ➣ Sanity ♡ - Some rooms will decrease your sanity. ")
    print("      Being around other characters and interacting ")
    print("      with them increases your sanity. You room is ")
    print("      also a place where your sanity will regenrate ")
    print("      Make sure your sanity does not hit 0%! Eating")
    print("      chocos is also an option!")
    print("    ➣ XP - The more you progress through the story, ")
    print("      the more xp you will earn. ")
    print("    ➣ Winning - In order to win, you must determine who ")
    print("      the murder is. Choosing the WRONG person is a ")
    print("      loss!")
    print("╚══════════════════════════════════════════════════════╝")
    input("Enter to return to menu.\n")
    startUp_frozen()
    mm_commands_tutorial_check()

def startUp():
    clear()
    sleep(0.3)
    print("╭─────────────────╮".center(50))
    sleep(0.3)
    print("│ Castle Suspense │".center(50))
    sleep(0.3)
    print("╰─────────────────╯".center(50))
    sleep(0.3)
    print("Main Menu".center(50))
    sleep(0.3)
    print("─────────".center(50))
    sleep(0.3)
    print("« Start »".center(50))
    sleep(0.3)
#    print("« Continue »".center(50))
#    sleep(0.3)
    print("« Help »".center(50))
    sleep(0.3)
    print("« Tutorial »".center(50))
    sleep(0.3)
    print()
    print("                           __/)")
    sleep(0.1)
    print("                        .-(__(=:")
    sleep(0.1)
    print("                     |\\ |    \\)")
    sleep(0.1)
    print("                     \ ||")
    sleep(0.1)
    print("                      \||")
    sleep(0.1)
    print("                       \|")
    sleep(0.1)
    print("                        |")
    sleep(0.3)
    print()
    print("Type command:".center(50))
    sleep(0.3)
    mm_commands()
    
def startUp_frozen():
    clear()
    print("╭─────────────────╮".center(50))
    print("│ Castle Suspense │".center(50))
    print("╰─────────────────╯".center(50))
    print("Main Menu".center(50))
    print("─────────".center(50))
    print("« Start »".center(50))
    print("« Help »".center(50))
    print("« Tutorial »".center(50))
    print()
    print("                           __/)")
    print("                        .-(__(=:")
    print("                     |\\ |    \\)")
    print("                     \ ||")
    print("                      \||")
    print("                       \|")
    print("                        |")
    print()
    print("Type command:".center(50))
    mm_commands_tutorial_check()

def mm_commands():
    #For some reason, if I put "or" it doesn't work?
    #so i had to put them separately
    insert = "                  > "
    action = input(insert)
    if action == "Start":
        Routes.introduction()
        playing = True
    elif action == "start":
        print()
        print("Reading the tutorial is recommended.".center(50))
        print("Are you sure you want to start?".center(50))
        print("                    yes / no")
        second = input("                  > ")
        if second == "yes":
            Routes.introduction()
            playing = True
        elif second == "Yes":
            Routes.introduction()
            playing = True
        elif second == "no":
            startUp_frozen()
            mm_commands_tutorial_check()
        elif second == "No":
            startUp_frozen()
            mm_commands_tutorial_check()
    #elif action == "Continue" or "continue":
        #cwd = os.getcwd()
        #print("{0}".format(cwd))
        #path = ("{0}".format(cwd)),"/saved"
        #return path
    elif action == "Help":
        showHelpMM()
    elif action == "help":
        showHelpMM()
    elif action == "characters":
        print()
        print("Please play story first.".center(50))
        mm_commands()
    elif action == "Characters":
        print()
        print("Please play story first.".center(50))
        mm_commands()
    elif action == "char":
        print()
        print("Please play story first.".center(50))
        mm_commands()
    elif action == "inventory":
        print()
        print("Please play story first.".center(50))
        mm_commands()
    elif action == "Inventory":
        print()
        print("Please play story first.".center(50))
        mm_commands()
    elif action == "inv":
        print()
        print("Please play story first.".center(50))
        mm_commands()
    elif action == "tutorial":
        showTutorial()
    elif action == "Tutorial":
        showTutorial()
    else:
        print()
        print("Try again.".center(50))
        mm_commands()

def mm_commands_tutorial_check():
    #For some reason, if I put "or" it doesn't work?
    #so i had to put them separately
    insert = "                  > "
    action = input(insert)
    if action == "Start":
        Routes.introduction()
        playing = True
    elif action == "start":
        Routes.introduction()
        playing = True
    #elif action == "Continue" or "continue":
        #cwd = os.getcwd()
        #print("{0}".format(cwd))
        #path = ("{0}".format(cwd)),"/saved"
        #return path
    elif action == "Help":
        showHelpMM()
    elif action == "help":
        showHelpMM()
    elif action == "characters":
        print()
        print("Please play story first.".center(50))
        mm_commands()
    elif action == "Characters":
        print()
        print("Please play story first.".center(50))
        mm_commands()
    elif action == "char":
        print()
        print("Please play story first.".center(50))
        mm_commands()
    elif action == "inventory":
        print()
        print("Please play story first.".center(50))
        mm_commands()
    elif action == "Inventory":
        print()
        print("Please play story first.".center(50))
        mm_commands()
    elif action == "inv":
        print()
        print("Please play story first.".center(50))
        mm_commands()
    elif action == "tutorial":
        showTutorial()
    elif action == "Tutorial":
        showTutorial()
    else:
        print()
        print("Try again.".center(50))
        mm_commands()
        

startUp()
Routes.introduction()
Routes.your_room()
playing = True
while playing and player.alive:
    player.location = courtroom
    #Routes.intwroduction()
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        Routes.commands()
        
        
