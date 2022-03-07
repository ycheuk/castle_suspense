from room import Room
import random
from player import Player
from item import Item
import os
import updater
import time
from time import sleep
import sys
from datetime import datetime

player = Player()
now = datetime.now()
current_time = datetime.now().strftime("%H:%M:%S")

#┌────────────────────────────────── Cool Features ──────────────────────────────────┐

# The delay print code is from the internet. I thought the print would make a cool
# effect to my game.

# Clears screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Countdown from t
def countdown(t):  
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

# Prints texts letter by letter. This is normal speed.
# Default = 0.05
seconds = 0.05
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(seconds)

# Prints texts letter by letter. This is slow speed, primarily for location texts.
def delay_print_location(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2)

# Prints texts letter by letter. This is quick speed.
def delay_print_quick(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

# ASCII art of a totally useless digital clock that shows the current time of the player in 24 hour.
def show_time():
    print("╔═════════╗")
    print("║ ",datetime.now().strftime("%H:%M")," ║")
    print("╚═════════╝")
    print("───┴───┴───")

#└────────────────────────────────── Cool Features ──────────────────────────────────┘

#┌─────────────────────────────── Character Shortcuts ───────────────────────────────┐
    
# Easter Egg List
eat_character_list = ["eat Butler","eat Doctor","eat Duchess","eat Viscount","eat Young Duke","eat butler","eat doctor","eat duchess","eat viscount","eat young duke"]
pickup_character_list = ["pickup Butler","pickup Doctor","pickup Duchess","pickup Viscount","pickup Young Duke","pickup butler","pickup doctor","pickup duchess","pickup viscount","pickup young duke"]

# Characters:

character_list = ["Butler","Doctor","Duchess","Viscount","Young Duke"]

butler = "Butler:"
doctor = "Doctor:"
duchess = "Duchess:"
duke = "Duke:"
viscount = "Viscount:"
who = "???:"
you = "You:"
young_duke = "Young Duke:"

#└─────────────────────────────── Character Shortcuts ───────────────────────────────┘

#┌─────────────────────────────────── Destination ───────────────────────────────────┐

butler_room = Room("▼ Butler's Room")
courtroom = Room("▼ Castle Courtroom")
corridor = Room("▼ Castle Corridor")
doctor_room = Room("▼ Doctor's Room")
duchess_room = Room("▼ Duchess' Room")
old_duke_room = Room("▼ Old Duke's Study")
penetralium = Room("▼ Penetralium")
viscount_room = Room("▼ Viscount's Room")
young_duke_room = Room("▼ Young Duke's Room")
your_room = Room("▼ Your Room")

trash = Room("trash")

#└─────────────────────────────────── Destination ───────────────────────────────────┘

#┌────────────────────────────────────── Items ──────────────────────────────────────┐

eat_item_list = ["eat body","eat diary","eat journal","eat key","eat letter","eat lillies","eat matches","eat notebook","eat notes","eat photo","eat silk"]

#alchemy_notebook = Item("Alchemy Notebook", "✎", "belongs to the Doctor, contains information on black magic and alchemy.")
#alchemy_notebook.putInRoom(courtroom)

body = Item("Body", "⚰", "The dead body of the old Duke.")
body.putInRoom(old_duke_room)

#bookmark = Item("Bookmark", "❀", "Descritpion needs to be written.")
#bookmark.putInRoom(old_duke_room)

choco = Item("Choco", "❤", "Can be used to restore 20 \n    bars of sanity.")
choco.putInRoom(your_room)

diary = Item("Diary", "❦", "Your diary... maybe it could remind you of \n    the events that occured last night.")
diary.putInRoom(your_room)

journal = Item("Journal", "✩", "The Viscount\'s journal, who is the heir \n    of the position of Viscount?")
journal.putInRoom(viscount_room)

key = Item("Key", "✑", "What could this key unlock?")
key.putInRoom(viscount_room)

#knife = Item("Knife", "⚔", "Description needs to be written.")
#knife.putInRoom(courtroom)

letter = Item("Letter", "✉", "A letter to the Vatican from the young Duke,\n    asks for the release of scholars that were labeled as\n    heretics.")
letter.putInRoom(young_duke_room)

lilies = Item("Lilies", "⚘", "There were many lilies were scattered in the\n    old Duke\'s room... what does this represent?")
lilies.putInRoom(old_duke_room)

matches = Item("Matches", "☄", "This could help you see in dark places\n    better.")
matches.putInRoom(duchess_room)

notebook = Item("Notebook", "✐", "Young Duke\'s notebook, contains banned\n    practices of alchemy.")
notebook.putInRoom(young_duke_room)

notes = Item("Notes", "❐", "The Doctor\'s notes, it contains mysterious\n    sigils and a language you can\'t seem to understand.")
notes.putInRoom(doctor_room)

photo = Item("Photo", "❏", "A photo of a couple.")
photo.putInRoom(butler_room)

silk = Item("Silk", "✿", "A fabric you found in your room, covered with\n    lily embroiders.")
silk.putInRoom(your_room)

#└────────────────────────────────────── Items ──────────────────────────────────────┘

#┌──────────────────────────────────── Shortcuts ────────────────────────────────────┐

action = "\n\n\nAction: "
arrow = "\n\n\n➥ "
choose = "\n\n\nChoose an option: "
enter = "\n\n\nPress enter to continue ▶ "

#└──────────────────────────────────── Shortcuts ────────────────────────────────────┘

class Routes:

    def __init__(self):
        #self.seconds = 0.05
        
        self.partner = None
        self.Bgender = None
        self.BgenderHisHer = None
        self.Rpartner= None
        self.Sgender = None
        self.Sgenderhisher = None
        
        self.alone = False
        self.before_first_room = True
        self.destination = False
        self.letter_opened = False    
        self.journal_opened = False
        self.first = False
        self.second = False
        self.intro = False
        self.room_count = 0
        self.the_truth = False
        self.matches_candle = False
        self.need_matches = False
        self.body_searched = False

        self.choco = False
        self.diary_found = False
        self.journal_found = False
        self.key_found = False
        self.letter_found = False
        self.lilies_found = False
        self.matches_found = False
        self.notebook_found = False
        self.notes_found = False
        self.photo_found = False
        self.silk_found = False

        self.been_to_your_room = False
        self.been_to_viscount_room = False
        self.been_to_duchess_room = False
        self.been_to_butler_room = False
        self.been_to_doctor_room = False
        self.been_to_young_duke_room = False
        self.been_to_old_duke_room = False
        self.old_duke_room_unlocked = False

#┌───────────────────────────────── Story Shortcuts ─────────────────────────────────┐

    def repeating_first_time(self):
        clear()
        player.level_and_sanity()
        delay_print_location(player.location.desc)
        print("\n───────────────────────")
        sleep(0.5)
        if player.location.hasItems():
            print("This room contains:")
            sleep(0.5)
            for i in player.location.items:
                print(i.name,i.symbol)
            print("───────────────────────")
            sleep(0.5)
                
    def repeating(self):
        clear()
        player.level_and_sanity()
        print(player.location.desc)
        print("───────────────────────")
        if player.location.hasItems():
            print("This room contains:")
            for i in player.location.items:
                print(i.name,i.symbol)
            print("───────────────────────")

    def showCharacters(self):
        print()
        print("╔══════════════════════════════════════════════════════╗	")
        print("    Current characters and descriptions:")
        print("    ───────────────────────────────────")
        print("    Main Characters:")
        print("    ────────────────")
        print("    ➣ You -- recently suffered from amnesia, (most \n      likely) a witness to the murder.")
        print("    ➣ Butler -- the old Duke\'s butler.")
        print("    ➣ Duchess -- has a daughter, not the wife of the \n      old Duke.")
        print("    ➣ Family doctor -- secretly studies alchemy and \n      black magic.")
        print("    ➣ Viscount -- a high ranking nobleman, has an \n      adopted child.")
        print("    ➣ Young Duke -- adopted son of the old Duke, \n      studies banned anatomy.")
        print()
        print("    Minor Characters:")
        print("    ─────────────────")
        print("    ➣ Old Duke ✝ -- murdered.")
        print("    ➣ Vatican -- a priest of the church.")
        print()
        print("    Note: As you progress, more characters will be \n    revealed.")
        print("╚══════════════════════════════════════════════════════╝")
        print()
        Routes.commands(self)

    def showDestination(self):
        self.destination = True
        print()
        print("╔══════════════════════════════════════════════════════╗")
        print("    Where would you like to go?")
        print("    ───────────────────────────")
        print("    Locations:")
        print('    a) Your room (lvl 1)')
        print('    b) Butler\'s Room (lvl 1)')
        print('    c) Duchess\' Room (lvl 1)')
        print('    d) Viscount\'s Room (lvl 3)')
        print('    e) Doctor\'s Room (lvl 4)')
        print('    f) Young Duke\'s Room (lvl 4)')
        print('    g) Old Duke\'s Room (locked)')
        print("╚══════════════════════════════════════════════════════╝")
        print()
        Routes.commands(self)
        self.destination = False

    def showHelp(self):
        print()
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
        Routes.commands(self)

    def showMap(self):
        print()
        print("╔════════════════════════════════════════════════════════════════════╗")
        print("         First Floor Plan                 Second Floor Plan")
        print("         ────────────────                 ─────────────────")
        print()
        print("       ┌─────────────────┐")
        print("       │      porch      │               ┌─────────────────┐")
        print("   ┌───┘    ┌───────┐    └───┐       ┌───┘     balcony     └───┐")
        print("   │     ┌╍╍┤ fire. ├╍╍┐     │       │     ┌────╍╍┬╍╍────┐     │")
        print(" ┌╍┵───╍╍┤  └───────┘  ├╍╍───┶╍┐   ┌╍┵───╍╍┘      │      └╍╍───┶╍┐")
        print(" ┇       ┘             └       │   ┇       ┐ bath │ bath ┌       │")
        print(" ┇kitchen    dining      living┇   │  Old  │      │      │ Young ┇")
        print(" ├─      ┐             ┌       ┇   ┇  Duke ┼──────┼──────┼  Duke ┇")
        print(" │       │             │       │   │        closet│closet        │")
        print(" ├─   ┌ └┴┤  └─┘ └─┘  ├┘       ┇   ┇    │ └┴──────┴──────┴──┘ └──┤")
        print(" │ ┌──┘      corridor          ┇   │ ┌──┘   corridor balcony     │")
        print(" │ │stair┌┴╍╍┴┐   ┌┴╍╍┴──┬┐ ┌─┬┘   │ │stair┌─╍╍──╍╍╍╍──╍╍──┬┐ ┌─┬┘")
        print(" ├─┴────┬┘               ┇    ┇    ├─┴─┬┐ ┌┘               ┇    │")
        print(" │      │                │    │    ┇Duc└┤ ┇                │    │")
        print(" │  s   │                ┇    ┇    │hess  ┇                ┇    │")
        print(" │  e   │               ┌┴┘ └─┴┐   ┇   ┌┤ │               ┌┴┘ └─┴┐")
        print(" │  c   │  ╭╨───╨───╨╮  ┘      ┇   ├───┼┤ │               ┇      ┇")
        print(" │  r   │  ╡courtroom╞    lib. │   │   └┤ ┇               │Butler│")
        print(" │  e   │  ╰╥───╥───╥╯  ┐      ┇   ┇Your┘ ┇               ┇      ┇")
        print(" │  t   │               └┬  ┬──┤   ┇Room┐ │               └┬  ┬╍╍┤")
        print(" │      │                │  │  │   │   ┌┤ │                │  │  ┇")
        print(" │  r   │             ┌──┤  ┤──┤   ├───┼┤ ┇             ┌──┤  ├╍╍┤")
        print(" │  o   │             ┇        ┇   ┇Vis└┤ ┇             ┇        ┇")
        print(" │  o   │             ┇ study  │   │Count ├─────────────┤ Doctor │")
        print(" │  m   ├───┐     ┌───┤        ┇   ┇   ┌┤    corridor            ┇")
        print(" └──────┴───┴─────┴───┴──╍╍╍───┘   └╍╍─┴┴─┴─────────────┴──╍╍╍───┘")
        print()
        print("╚════════════════════════════════════════════════════════════════════╝")
        Routes.commands(self)

#└───────────────────────────────── Story Shortcuts ─────────────────────────────────┘

#┌───────────────────────────────── Commands System ─────────────────────────────────┐

    def commands(self):
        command = input(arrow)
        commandWords = command.split()
        if player.sanity <= 0:
            Routes.lose(self)
        if command == "a":
            if self.second:
                Routes.meeting_one_a_and_c(self)
            if self.destination:
                if player.location == your_room:
                    print("You\'re already here.")
                    Routes.commands(self)
                if player.level_number >= 1:
                    if self.before_first_room == True:
                        if self.alone == False:
                            Routes.corridor_talk(self)
                    Routes.your_room(self)
                else:
                    print("Not enough levels.")
                    Routes.commands(self)
                Routes.your_room(self)
            if self.intro == True:
                Routes.introduction_a(self)
            if self.first == True:
                Routes.first_a(self)
            else:
                print("Try again.")
                Routes.commands(self)
        if command == "b":
            if self.second:
                Routes.meeting_one_b_and_d(self)
            if self.destination:
                if player.location == butler_room:
                    print("You\'re already here.")
                    Routes.commands(self)
                if player.level_number >= 1:
                    if self.before_first_room == True:
                        if self.alone == False:
                            Routes.corridor_talk(self)
                    Routes.butler_room(self)
                else:
                    print("Not enough levels.")
                    Routes.commands(self)
            if self.intro:
                Routes.introduction_b(self)
            if self.first:
                Routes.first_b(self)
            else:
                print("Try again.")
                Routes.commands(self)
        if command == "c":
            if self.second:
                Routes.meeting_one_a_and_c(self)
            if self.destination:
                if player.location == duchess_room:
                    print("You\'re already here.")
                    Routes.commands(self)
                if player.level_number >= 1:
                    if self.before_first_room == True:
                        if self.alone == False:
                            Routes.corridor_talk(self)
                    Routes.duchess_room(self)
                else:
                    print("Not enough levels.")
                    Routes.commands(self)
            if self.first:
                Routes.first_c(self)
            else:
                print("Try again.")
                Routes.commands(self)
        if command == "d":
            if self.second:
                Routes.meeting_one_b_and_d(self)
            if self.destination:
                if player.location == viscount_room:
                    print("You\'re already here.")
                    Routes.commands(self)
                if player.level_number >= 3:
                    if self.before_first_room == True:
                        if self.alone == False:
                            Routes.corridor_talk(self)
                    Routes.viscount_room(self)
                else:
                    print("Not enough levels.")
                    Routes.commands(self)
            if self.first:
                Routes.first_d(self)
            else:
                print("Try again.")
                Routes.commands(self)
        if command == "e":
            if self.destination:
                if player.location == doctor_room:
                    print("You\'re already here.")
                    Routes.commands(self)
                if player.level_number >= 4:
                    if self.before_first_room == True:
                        if self.alone == False:
                            Routes.corridor_talk(self)
                    Routes.doctor_room(self)
                else:
                    print("Not enough levels.")
                    Routes.commands(self)
            else:
                print("Try again.")
                Routes.commands(self)
        if command == "f":
            if self.destination:
                if player.location == young_duke_room:
                    print("You\'re already here.")
                    Routes.commands(self)
                if player.level_number >= 4:
                    if self.before_first_room == True:
                        if self.alone == False:
                            Routes.corridor_talk(self)
                    Routes.young_duke_room(self)
                else:
                    print("Not enough levels.")
                    Routes.commands(self)
            else:
                print("Try again.")
                Routes.commands(self)
        if command == "g":
            if self.destination:
                if self.old_duke_room_unlocked == False:
                    print("This room is currently locked.")
                    Routes.commands(self)
                if self.old_duke_room_unlocked == True:
                    Routes.old_duke_room(self)
            else:
                print("Try again.")
                Routes.commands(self)
        if command == "cont":
            if self.room_count >= 6 and player.level_number >= 5:
                Routes.before_meeting_one(self)
            if self.the_truth == True:
                Routes.bookmark(self)
            else:
                Routes.showDestination(self)
        #For some reason, if I write an "or" command, it becomes super buggy and crashes?
        if command == "char":
            Routes.showCharacters(self) 
        if command == "inv":
            player.showInventory()
            Routes.commands(self)
        if command == "help":
            Routes.showHelp(self)
        if command == "map":
            Routes.showMap(self)
        if command == "pickup photo":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.photo_found == True:
                player.pickup(photo)
                print("Photo has been placed in your inventory.")
                Routes.commands(self)
            else: 
                player.pickup(photo)
                Routes.photo(self)
        if command == "pickup Photo":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.photo_found == True:
                player.pickup(photo)
                print("Photo has been placed in your inventory.")
                Routes.commands(self)
            else: 
                player.pickup(photo)
                Routes.photo(self)
        if command == "drop Photo":
            player.drop(photo)
            print("Photo has been removed from your inventory")
            Routes.commands(self)
        if command == "drop photo":
            player.drop(photo)
            print("Photo has been removed from your inventory")
            Routes.commands(self)
        if command == "pickup diary":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.diary_found == True:
                player.pickup(diary)
                print("Diary has been placed in your inventory.")
                Routes.commands(self)
            else: 
                player.pickup(diary)
                Routes.locked_diary(self)
        if command == "pickup Diary":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.diary_found == True:
                player.pickup(diary)
                print("Diary has been placed in your inventory.")
                Routes.commands(self)
            else: 
                player.pickup(diary)
                Routes.locked_diary(self)
        if command == "drop Diary":
            player.drop(diary)
            print("Diary has been removed from your inventory")
            Routes.commands(self)
        if command == "drop diary":
            player.drop(diary)
            print("Diary has been removed from your inventory")
            Routes.commands(self)
        if command == "pickup silk":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(sekf)
            if self.silk_found == True:
                player.pickup(silk)
                print("Silk has been placed in your inventory.")
                Routes.commands(self)
            else: 
                player.pickup(silk)
                Routes.silk(self)
        if command == "pickup Silk":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.silk_found == True:
                player.pickup(silk)
                print("Silk has been placed in your inventory.")
                Routes.commands(self)
            else: 
                player.pickup(silk)
                Routes.silk(self)
        if command == "drop Silk":
            player.drop(silk)
            print("Silk has been removed from your inventory")
            Routes.commands(self)
        if command == "drop silk":
            player.drop(silk)
            print("Silk has been removed from your inventory")
            Routes.commands(self)
        if command == "pickup journal":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.journal_found == True:
                player.pickup(journal)
                print("Journal has been placed in your inventory.")
                Routes.commands(self)
            else: 
                player.pickup(journal)
                Routes.journal(self)
        if command == "pickup Journal":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.journal_found == True:
                player.pickup(journal)
                print("Journal has been placed in your inventory.")
                Routes.commands(self)
            else: 
                player.pickup(journal)
                Routes.journal(self)
        if command == "drop Journal":
            player.drop(journal)
            print("Journal has been removed from your inventory")
            Routes.commands(self)
        if command == "drop journal":
            player.drop(journal)
            print("Journal has been removed from your inventory")
            Routes.commands(self)
        if command == "pickup key":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.key_found == True:
                player.pickup(key)
                print("Key has been placed in your inventory.")
                Routes.commands(self)
            else: 
                player.pickup(key)
                Routes.key(self)
        if command == "pickup Key":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.key_found == True:
                player.pickup(key)
                print("Key has been placed in your inventory.")
                Routes.commands(self)
            else: 
                player.pickup(key)
                Routes.key(self)
        if command == "drop Key":
            player.drop(key)
            print("Key has been removed from your inventory")
            Routes.commands(self)
        if command == "drop key":
            player.drop(key)
            print("Key has been removed from your inventory")
            Routes.commands(self)
        if command == "pickup lilies":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.lilies_found == True:
                player.pickup(lilies)
                print("Lilies has been placed in your inventory.")
                Routes.commands(self)
            else: 
                player.pickup(lilies)
                Routes.lilies(self)
        if command == "pickup Lilies":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.lilies_found == True:
                player.pickup(lilies)
                print("Lilies has been placed in your inventory.")
                Routes.commands(self)
            else:
                player.pickup(lilies)
                Routes.lilies(self)
        if command == "drop Lilies":
            player.drop(lilies)
            print("Lilies has been removed from your inventory")
            Routes.commands(self)
        if command == "drop lilies":
            player.drop(lilies)
            print("Lilies has been removed from your inventory")
            Routes.commands(self)
        if command == "pickup notebook":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.notebook_found == True:
                player.pickup(notebook)
                print("Notebook has been placed in your inventory.")
                Routes.commands(self)
            else:
                player.pickup(notebook)
                Routes.notebook(self)
        if command == "pickup Notebook":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.notebook_found == True:
                player.pickup(notebook)
                print("Notebook has been placed in your inventory.")
                Routes.commands(self)
            else:
                player.pickup(notebook)
                Routes.notebook(self)
        if command == "drop Notebook":
            player.drop(notebook)
            print("Notebook has been removed from your inventory")
            Routes.commands(self)
        if command == "drop notebook":
            player.drop(notebook)
            print("Notebook has been removed from your inventory")
            Routes.commands(self)
        if command == "pickup letter":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.letter_found == True:
                player.pickup(letter)
                print("Letter has been placed in your inventory.")
                Routes.commands(self)
            else:
                player.pickup(letter)
                Routes.letter(self)
        if command == "pickup Letter":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.letter_found == True:
                player.pickup(letter)
                print("Letter has been placed in your inventory.")
                Routes.commands(self)
            else:
                player.pickup(letter)
                Routes.letter(self)
        if command == "drop Letter":
            player.drop(letter)
            print("Letter has been removed from your inventory")
            Routes.commands(self)
        if command == "drop letter":
            player.drop(letter)
            print("Letter has been removed from your inventory")
            Routes.commands(self)
        if command == "pickup bookmark":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.bookmark_found == True:
                player.pickup(bookmark)
                print("Bookmark has been placed in your inventory.")
                Routes.commands(self)
            else:
                player.pickup(bookmark)
                Routes.bookmark(self)
        if command == "pickup Bookmark":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.bookmark_found == True:
                player.pickup(bookmark)
                print("Bookmark has been placed in your inventory.")
            else:
                player.pickup(bookmark)
                Routes.bookmark(self)
        if command == "drop Bookmark":
            player.drop(bookmark)
            print("Bookmark has been removed from your inventory")
            Routes.commands(self)
        if command == "drop bookmark":
            player.drop(bookmark)
            print("Bookmark has been removed from your inventory")
            Routes.commands(self)
        if command == "pickup notes":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.notes_found == True:
                player.pickup(notes)
                print("Notes has been placed in your inventory.")
                Routes.commands(self)
            else:
                player.pickup(notes)
                Routes.notes(self)
        if command == "pickup Notes":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.notes_found == True:
                player.pickup(notes)
                print("Notes has been placed in your inventory.")
                Routes.commands(self)
            else:
                player.pickup(notes)
                Routes.notes(self)
        if command == "drop Notes":
            player.drop(notes)
            print("Notes has been removed from your inventory")
            Routes.commands(self)
        if command == "drop botes":
            player.drop(notes)
            print("Notes has been removed from your inventory")
            Routes.commands(self)
        if command == "pickup matches":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.matches_found == True:
                player.pickup(matches)
                print("Matches has been placed in your inventory.")
                Routes.commands(self)
            else:
                player.pickup(matches)
                Routes.matches(self)
        if command == "pickup Matches":
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            if self.matches_found == True:
                player.pickup(matches)
                print("Matches has been placed in your inventory.")
                Routes.commands(self)
            else:
                player.pickup(matches)
                Routes.matches(self)
        if command == "drop Matches":
            player.drop(matches)
            print("Matches has been removed from your inventory")
            Routes.commands(self)
        if command == "drop matches":
            player.drop(matches)
            print("Matches has been removed from your inventory")
            Routes.commands(self)
        if command == "pickup body":
            if self.body_searched == True:
                Routes.body_searched(self)
            else:
                Routes.body(self)
        if command == "pickup Body":
            if self.body_searched == True:
                Routes.body_searched(self)
            else:
                Routes.body(self)
        if command == "pickup choco":
            self.choco = True
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            else:
                player.pickup(choco)
                print("Choco has been placed in your inventory.")
                Routes.commands(self)
        if command == "pickup Choco":
            self.choco = True
            if len(player.items) >= 5:
                print("Your inventory is currently full.")
                Routes.commands(self)
            else:
                player.pickup(choco)
                print("Choco has been placed in your inventory.")
                Routes.commands(self)
        if command == "eat choco":
            if self.choco:
                player.consume(choco)
                self.choco = False
                print("You regained 20 sanity!")
                Routes.commands(self)
            else:
                print("Good try, but you don\'t have any chocos!")
                Routes.commands(self)
        if command == "eat Choco":
            if self.choco_found:
                player.consume(choco)
                self.choco = False
                print("You regained 20 sanity!")
                Routes.commands(self)
            else:
                print("Good try, but you don\'t have any chocos!")
                Routes.commands(self)
        if command == "drop choco":
            player.drop(choco)
            print("Choco has been removed from your inventory")
            Routes.commands(self)
        if command == "drop choco":
            player.drop(choco)
            print("Choco has been removed from your inventory")
            Routes.commands(self)
        if command == "cry":
            print("Feel better?")
            Routes.commands(self)
        if command in eat_item_list:
            print("You can\'t eat that silly!")
            Routes.commands(self)
        if command in eat_character_list:
            print("┌───┐")
            print("│┌─┐│")
            print("└┘┌┘│")
            print("  │┌┘")
            print("  ┌┐")
            print("  └┘")
            Routes.commands(self)
        if command in pickup_character_list:
            print("Like... in a bridal carry? No...")
            Routes.commands(self)
        #if command == "text speed":
        #    print("What do you want your text speed to be?")
        #    player_text_speed = input(arrow)
        #    seconds = 1
        #    seconds = player_text_speed
        #    Routes.commands(self)
        if command == "die":
            print("You can\'t die yet! :(")
            Routes.commands(self)
        else:
            print("Not a valid command")
            Routes.commands(self)

#└───────────────────────────────── Commands System ─────────────────────────────────┘

#┌────────────────────────────────────── Intro ──────────────────────────────────────┐

    def introduction(self):
        player.location = courtroom
        
        Routes.repeating_first_time(self)
        print(you)
        delay_print('"Huh? ')
        sleep(0.5)
        delay_print("No one\'s here? ")
        sleep(0.5)
        delay_print('Did I get the location wrong perhaps..."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nAs you think that, a man with a small mustache enters the lobby.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        self.intro = True
        print(who)
        delay_print('"There you are! ')
        sleep(0.5)
        delay_print('I was worried sick.')
        sleep(0.5)
        delay_print('\nIt\'s best you don\'t wander alone with your condition."')
        sleep(0.5)
        print(choose)
        print('a) What condition?\nb) I understand.')
        Routes.commands(self)

    def introduction_a(self):
        player.location = courtroom
        player.xp += 10
        
        Routes.repeating(self)
        print(who)
        delay_print('"Your amnesia, obviously! ')
        sleep(0.5)
        delay_print('Did no one tell you yet?"')
        sleep(0.5)
        input(enter)

        Routes.introduction_continued(self)

    def introduction_b(self):
        player.location = courtroom
        player.xp += 5
        
        Routes.repeating(self)
        print(who)
        delay_print('"Now let\'s start from the beginning. ')
        sleep(0.5)
        delay_print('Maybe letting you know a portion of last night would help recover your memories."')
        sleep(0.5)
        input(enter)

        Routes.introduction_continued(self)

    def introduction_continued(self):
        self.intro = False
        Routes.repeating(self)
        player.sanity -= 3
        delay_print('\nWhile waiting for the others, the man presents himself as the Viscount, and tells you what happened the previous night.')
        sleep(0.5)
        delay_print('\n\nThe owner of this castle, the old Duke, was murdered after the banquet last night.')
        sleep(0.5)
        delay_print('\n\nSix individuals attended this banquet:')
        sleep(0.5)
        delay_print('\nThe Duchess, the Young Duke, the Butler, the Viscount, the family doctor, and you.')
        sleep(0.5)
        delay_print('\n\nAfter finding him dead in his study room at midnight, the Vatican sent an investigator.')
        sleep(0.5)
        input(enter)
        
        Routes.repeating(self)
        print(viscount)
        player.sanity -=3
        delay_print('"However, unable to track down the culprit, they locked everyone in this castle, leaving us to find the murderer ourselves before any of us can leave."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nAs he was describing the case to you, a man with messy hair walks in, looking extremely annoyed.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(who)
        delay_print('"He was a terrible man. ')
        sleep(0.5)
        delay_print('Why waste time finding the killer? ')
        sleep(0.5)
        delay_print('I could be doing my research instead of being here."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(viscount)
        delay_print('"This is the doctor. ')
        sleep(0.5)
        delay_print('He hates it when people take up his valuable time."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(doctor)
        delay_print('"There\'s more people that aren\'t here yet? ')
        sleep(0.5)
        delay_print('If we\'re not investigating, then I\'m leaving."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(who)
        delay_print('"Of course we need to investigate. ')
        sleep(0.5)
        delay_print('How else will we bring my father\'s murderer to justice?"')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nThe resounding thud of his metal scepter silences all the unnecessary noise. ')
        player.sanity -= 3
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(viscount)
        delay_print('"This is the young Duke. ')
        sleep(0.5)
        delay_print('Son of the old Duke, as you can probably guess."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nIn royal attire, the young Duke rests his hands on the tip of his sceptar, standing on the second-story platform.')
        player.sanity -=2 
        sleep(0.5)
        delay_print('\n\nAs he walks down the balcony stairs, the Duchess and castle Butler walk into the room as well. ')
        sleep(0.5)
        delay_print('Everyone takes their seats around the meeting table.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(young_duke)
        delay_print('"I do believe that everyone is aware of the situation?"')
        sleep(0.5)
        delay_print('"Then let us begin. ')
        sleep(0.5)
        delay_print('We must find the murderer soon, or else everyone will be punished."')
        player.sanity -=5
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nAfter everyone introduces themselves, the young Duke suggests we begin searching for evidence in pairs.')
        sleep(0.5)
        delay_print('\nEveryone chooses where they want to investigate and begins searching.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('(Where should I search... ')
        sleep(0.5)
        delay_print('Going to my own room seems like a good start for now. ')
        sleep(0.5)
        delay_print('It could help me with my memories.)')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nWhile you were deep in thought, people leave one-by-one. ')
        sleep(0.5)
        delay_print('Soon, there is only one person left with you.')
        sleep(0.5)
        delay_print('\nYou stare at that person curiously.')
        player.sanity -= 2
        sleep(0.5)
        input(enter)
        
        Routes.repeating(self)
        print('\nWho do you want as your partner?')
        print()
        print('a) Butler')
        print('b) Doctor')
        print('c) Duchess')
        print('d) Viscount')
        print('e) Young Duke')
        Routes.choose_partner(self)

    def choose_partner(self):
        player.location = courtroom
    
        your_partner = input('\n\n➥ ')
        if your_partner == "a":
            self.partner = "Butler"
            self.Rpartner = "Butler:"
            self.Bgender = "He"
            self.BgenderHisHer = "His"
            self.Sgender = "he"
            self.Sgenderhisher = "his"
            Routes.first_choice(self)
        if your_partner == "b":
            self.partner = "Doctor"
            self.Rpartner = "Doctor:"
            self.Bgender = "He"
            self.BgenderHisHer = "His"
            self.Sgender = "he"
            self.Sgenderhisher = "his"
            Routes.first_choice(self)
        if your_partner == "c":
            self.partner = "Duchess"
            self.Rpartner = "Duchess:"
            self.Bgender = "She"
            self.BgenderHisHer = "Her"
            self.Sgender = "she"
            self.Sgenderhisher = "her"
            Routes.first_choice(self)
        if your_partner == "d":
            self.partner = "Viscount"
            self.Rpartner = "Viscount:"
            self.Bgender = "He"
            self.BgenderHisHer = "His"
            self.Sgender = "he"
            self.Sgenderhisher = "his"
            Routes.first_choice(self)
        if your_partner == "e":
            self.partner = "Young Duke"
            self.Rpartner = "Young Duke:"
            self.Bgender = "He"
            self.BgenderHisHer = "His"
            self.Sgender = "he"
            self.Sgenderhisher = "his"
            Routes.first_choice(self)
        else:
            print("Please try again.") 
            Routes.choose_partner(self)
        
    def first_choice(self):
        player.location = courtroom
        character_list.remove(self.partner)
        player.xp += 5
        
        Routes.repeating(self)
        print(you)
        delay_print('(Oh, it\'s the ')
        delay_print(self.partner)
        delay_print('... ')
        delay_print(self.Bgender)
        delay_print(' wasn\'t in a rush to leave?')
        sleep(0.5)
        delay_print('\nMaybe ')
        delay_print(self.Sgender)
        delay_print('\'s thinking the same thing as me?)')
        sleep(0.5)
        print(choose)
        self.first = True
        print('a) May I invite you to come with me...?\nb) (Then again, think it\'s best if I\'m alone for now.)\nc) What are you staring at?!\nd) ...')

        Routes.commands(self)

    def first_a(self):
        player.xp += 10
        
        Routes.repeating(self)
        print(self.Rpartner)
        delay_print('"I would be honored."')
        player.sanity += 5
        sleep(0.5)
        input(enter)

        Routes.introduction_final(self)

    def first_b(self):

        Routes.repeating(self)
        print(self.Rpartner)
        delay_print('"Would you like to investigate together?"')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"I think I would rather be alone right now. ')
        sleep(0.5)
        delay_print('You know... ')
        sleep(0.5)
        delay_print('to collect my thoughts."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(self.Rpartner)
        delay_print('"I understand. ')
        sleep(0.5)
        delay_print('In that case, please stay safe then."')
        player.sanity -= 3
        sleep(0.5)
        input(enter)
        self.alone = True

        Routes.introduction_final(self)
        
    def first_c(self):
        player.location = courtroom
        player.xp += 5
        
        Routes.repeating(self)
        print(self.Rpartner)
        delay_print('"I thought it would be best if we investigated together. We are the only pair left after all."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"Oh... you\'re right. Shall we investigate together then?"')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(self.Rpartner)
        delay_print('"I would be honored."')
        player.sanity += 5
        sleep(0.5)
        input(enter)

        Routes.introduction_final(self)
        
    def first_d(self):
        player.location = courtroom
        player.xp += 5
        
        Routes.repeating(self)
        print(self.Rpartner)
        delay_print('"Would you like to investigate together?"')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"I suppose so..."')
        sleep(0.5)
        input(enter)
        
        Routes.introduction_final(self)
        
    def introduction_final(self):
        self.first = False
        player.location = courtroom
        
        Routes.repeating(self)
        delay_print('\nThe only places that can be searched for evidence are the scene of the murder and the rooms of the suspects.')
        sleep(0.5)
        input(enter)

        if self.alone == True:
            Routes.repeating(self)
            print(you)
            delay_print('(Where should I go first?)')
            sleep(0.5)

        else:
            Routes.repeating(self)
            print(self.Rpartner)
            player.sanity += 3
            delay_print('"Where would you like to go?"')
            sleep(0.5)

        Routes.showDestination(self)
        Routes.commands(self)

#└────────────────────────────────────── Intro ──────────────────────────────────────┘

#┌────────────────────────────────── Corridor Talk ──────────────────────────────────┐ 

    def corridor_talk(self):
        player.location = corridor
        self.before_first_room = False
        
        Routes.repeating_first_time(self)
        #INPUT FOR THE "SECOND FLOOR" MAYBE?
        delay_print('\nThe two of you walk towards the second floor. ')
        sleep(0.5)
        if self.partner == "Young Duke":
            delay_print('You feel a familiar feeling when walking next to him, but yet, somehow different. ')
            sleep(0.5)
        delay_print('\nTo break the silence, you decide to take the initiative and talk about something.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"')
        delay_print(self.partner)
        delay_print('?"')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(self.Rpartner)
        delay_print('"Hmm? What is it?"')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"Ah... um, ')
        sleep(0.5)
        delay_print('I just... have a question I\'d like to ask you."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(self.Rpartner)
        delay_print('"Please do ask then."')
        player.sanity += 3
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"Did the old Duke know me... ')
        sleep(0.5)
        delay_print('before I lost my memory? ')
        sleep(0.5)
        delay_print('Can you possibly tell me more about myself?"')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nThe ')
        delay_print(self.partner)
        delay_print(' gives you a long look before gently shaking ')
        delay_print(self.Sgenderhisher)
        delay_print(' head.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(self.Rpartner)
        delay_print('"We only met at the banquet last night. ')
        sleep(0.5)
        delay_print('As for the events prior to that, I\'m afraid I do not know. ')
        sleep(0.5)
        delay_print('\n\nBut there is one thing they probably failed to mention to you."')
        sleep(0.5)
        input(enter)
        
        Routes.repeating(self)
        delay_print('\nThe smile disappears from the ')
        delay_print(self.partner)
        delay_print('\'s face. ')
        sleep(0.5)
        delay_print('Seeing this expression, you get a bad feeling.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(self.Rpartner)
        delay_print('"Last night, you were unconscious next to the deceased at the scene of murder. ')
        sleep(0.5)
        delay_print('I was the one who brought you back to your room. ')
        sleep(0.5)
        delay_print('\nSo... ')
        sleep(0.5)
        delay_print('you were probably a witness to the murder before you lost your memory."')
        player.sanity -= 10
        sleep(0.5)
        input(enter)

#└────────────────────────────────── Corridor Talk ──────────────────────────────────┘

#┌──────────────────────────────────── Your Room ────────────────────────────────────┐

    def your_room(self):
        player.location = your_room
        player.sanity += 5

        if self.been_to_your_room == False:
            self.room_count += 1
            player.xp += 40

            if self.alone:
                Routes.repeating_first_time(self)
                player.sanity += 3
                print(you)
                delay_print('(So this is my room. ')
                sleep(0.5)
                delay_print('Maybe if I look around, some of my memories will return.)')
                sleep(0.5)
                input(enter)

                Routes.repeating(self)
                player.sanity += 3
                delay_print("\nWhat would you like to do in here?")
                self.been_to_your_room = True
                Routes.commands(self)

            if self.alone == False:
                Routes.repeating_first_time(self)
                print(self.Rpartner)
                player.sanity += 5
                delay_print('"This is your room. ')
                sleep(0.5)
                delay_print('You should take a look around. ')
                sleep(0.5)
                delay_print('Maybe some of your memories will return."')
                sleep(0.5)
                input(enter)

                Routes.repeating(self)
                player.sanity += 5
                delay_print("\nWhat would you like to do in here?")
                self.been_to_your_room = True
                Routes.commands(self)
            
        if self.been_to_your_room == True:
            Routes.repeating_first_time(self)
            delay_print("\nWhat would you like to do in here?")
            Routes.commands(self)

    def locked_diary(self):
        self.diary_found = True
        player.location = your_room
        player.xp += 50

        Routes.repeating(self)
        delay_print('\nAs you open your drawers, you find your personal diary.')
        sleep(0.5)
        input(enter)

        if self.key_found == True:
            Routes.repeating(self)
            print(you)
            delay_print('(It\'s locked... ')
            sleep(0.5)
            delay_print('Wait, I found a key in the Viscount\'s room earlier. ')
            sleep(0.5)
            delay_print('I should test the key in this diary.)')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print('(To test the key in your diary, type: "test key")')
            sleep(0.5)

            Routes.open_diary(self)
            
        if self.key_found == False:
            Routes.repeating(self)
            print(you)
            delay_print('(It\'s locked. ')
            sleep(0.5)
            delay_print('I wonder where the key is... ')
            sleep(0.5)
            delay_print('It should be here somewhere since it\'s my diary. ')
            sleep(0.5)
            delay_print('I suppose I\'ll keep an eye on a key.)')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print("\nWhat else would you like to do in here?")
            Routes.commands(self)

    def silk(self):
        self.silk_found = True
        player.location = your_room
        player.xp += 15

        Routes.repeating(self)
        delay_print('\n(On your chair, there lays a small silk fabric. ')
        sleep(0.5)
        delay_print('It is decorated with floral lily embroiders.)')
        input(enter)

        if self.alone == False:
            Routes.repeating(self)
            print(self.Rpartner)
            delay_print('"Lily embroiders... ')
            sleep(0.5)
            delay_print('How interesting..."')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            print(you)
            delay_print('"What is it?"')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            print(self.Rpartner)
            delay_print('"Sorry, it\'s nothing."')
            sleep(0.5)
            input(enter)

        Routes.repeating(self)
        delay_print("\nWhat else would you like to do in here?")
        Routes.commands(self)

#└──────────────────────────────────── Your Room ────────────────────────────────────┘

#┌─────────────────────────────────── Butler Room ───────────────────────────────────┐

    def butler_room(self):
        player.location = butler_room

        if self.been_to_butler_room == False:
            self.room_count += 1
            player.xp += 15
            
            if self.alone:
                player.sanity -= 5
                Routes.repeating_first_time(self)
                print(you)
                delay_print('(This is the butler\'s room. ')
                sleep(0.5)
                delay_print('I should take a look around.)')
                sleep(0.5)
                self.been_to_butler_room = True
                Routes.commands(self)

            if self.alone == False:
                if self.partner == "Butler":
                    player.sanity += 5
                    Routes.repeating_first_time(self)
                    print(self.Rpartner)
                    delay_print('"This is my room. ')
                    sleep(0.5)
                    delay_print('Let\'s begin investigating."')
                    sleep(0.5)
                    input(enter)
                else:
                    player.sanity += 5
                    Routes.repeating_first_time(self)
                    print(self.Rpartner)
                    delay_print('"This is the Butler\'s room. ')
                    sleep(0.5)
                    delay_print('Let\'s begin investigating."')
                    sleep(0.5)
                    input(enter)

                Routes.repeating(self)
                delay_print("\nWhat would you like to do in here?")
                self.been_to_butler_room = True
                Routes.commands(self)
            
        if self.been_to_butler_room == True:            
            Routes.repeating_first_time(self)
            delay_print("\nWhat would you like to do in here?")
            Routes.commands(self)

    def photo(self):
        self.photo_found = True
        player.location = butler_room
        player.xp += 10

        Routes.repeating(self)
        delay_print('\nOn the butler\'s table, you find a framed photo of two people.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('(I wonder who these two people are...)')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print("\nWhat else would you like to do in here?")
        Routes.commands(self)
            
#└─────────────────────────────────── Butler Room ───────────────────────────────────┘

#┌─────────────────────────────────── Doctor Room ───────────────────────────────────┐

    def doctor_room(self):
        player.location = doctor_room

        if self.been_to_doctor_room == False:
            self.room_count += 1
            player.xp += 40

            if self.alone:
                player.sanity -= 5
                Routes.repeating_first_time(self)
                print(you)
                delay_print('(This is the doctor\'s room. ')
                sleep(0.5)
                delay_print('I should take a look around.)')
                sleep(0.5)
                self.been_to_doctor_room = True
                Routes.commands(self)

            if self.alone == False:
                if self.partner == "Doctor":
                    player.sanity += 5
                    Routes.repeating_first_time(self)
                    print(self.Rpartner)
                    delay_print('"This is my room. ')
                    sleep(0.5)
                    delay_print('Let\'s begin investigating."')
                    sleep(0.5)
                    input(enter)
                else:
                    player.sanity += 5
                    Routes.repeating_first_time(self)
                    print(self.Rpartner)
                    delay_print('"This is the Doctor\'s room. ')
                    sleep(0.5)
                    delay_print('Let\'s begin investigating."')
                    sleep(0.5)
                    input(enter)

                Routes.repeating(self)
                delay_print("\nWhat would you like to do in here?")
                self.been_to_doctor_room = True
                Routes.commands(self)
            
        if self.been_to_doctor_room == True:
            Routes.repeating_first_time(self)
            delay_print("\nWhat would you like to do in here?")
            Routes.commands(self)

    def notes(self):
        self.notes_found = True
        player.location = doctor_room
        player.xp = 15

        Routes.repeating(self)
        delay_print('\nYou find many scribbled notes that are scattered across the doctor\'s work desk. ')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('(What are all these words and symbols? ')
        sleep(0.5)
        delay_print('I can barely make a word out of these words.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print("\nWhat else would you like to do in here?")
        Routes.commands(self)
        
#└─────────────────────────────────── Doctor Room ───────────────────────────────────┘

#┌────────────────────────────────── Duchess Room ───────────────────────────────────┐

    def duchess_room(self):
        player.location = duchess_room

        if self.been_to_duchess_room == False:
            self.room_count += 1
            player.xp += 15

            if self.alone == True:
                player.sanity -= 5
                Routes.repeating_first_time(self)
                print(you)
                delay_print('(This is the duchess\' room. ')
                sleep(0.5)
                delay_print('I should take a look around.)')
                sleep(0.5)
                self.been_to_duchess_room = True
                Routes.commands(self)

            if self.alone == False:
                if self.partner == "Duchess":
                    player.sanity += 5
                    Routes.repeating_first_time(self)
                    print(self.Rpartner)
                    delay_print('"This is my room. ')
                    sleep(0.5)
                    delay_print('Let\'s begin investigating."')
                    sleep(0.5)
                    input(enter)
                else:
                    player.sanity += 5
                    Routes.repeating_first_time(self)
                    print(self.Rpartner)
                    delay_print('"This is the Duchess\' room. ')
                    sleep(0.5)
                    delay_print('Let\'s begin investigating."')
                    sleep(0.5)
                    input(enter)

                Routes.repeating(self)
                delay_print("\nWhat would you like to do in here?")
                self.been_to_duchess_room = True
                Routes.commands(self)
                
        if self.been_to_duchess_room == True:
            Routes.repeating_first_time(self)
            delay_print("\nWhat would you like to do in here?")
            Routes.commands(self)

    def matches(self):
        self.matches_found = True
        player.location = duchess_room
        player.xp += 40

        if self.need_matches == True:
            player.sanity -= 5
            Routes.repeating(self)
            print(you)
            delay_print('(Found them! ')
            sleep(0.5)
            delay_print('I should go back to the old Duke\'s study now.)')
            sleep(0.5)

            self.matches_candle = True
            Routes.body_continued(self)
            

        else:
            Routes.repeating(self)
            print(you)
            delay_print('(Matches. ')
            sleep(0.5)
            delay_print('This should come in handy.)')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print("\nWhat else would you like to do in here?")
            Routes.commands(self)



#└────────────────────────────────── Duchess Room ───────────────────────────────────┘

#┌────────────────────────────────── Viscount Room ──────────────────────────────────┐

    def viscount_room(self):
        player.location = viscount_room

        if self.been_to_viscount_room == False:
            self.room_count += 1
            player.xp += 60

            if self.alone:
                player.sanity -=3
                Routes.repeating_first_time(self)
                print(you)
                delay_print('(This is the Viscount\'s room. ')
                sleep(0.5)
                delay_print('I should take a look around.)')
                sleep(0.5)
                self.been_to_viscount_room = True
                Routes.commands(self)

            if self.alone == False:
                if self.partner == "Viscount":
                    player.sanity += 5
                    Routes.repeating_first_time(self)
                    print(self.Rpartner)
                    delay_print('"This is my room. ')
                    sleep(0.5)
                    delay_print('Let\'s begin investigating."')
                    sleep(0.5)
                    input(enter)
                else:
                    player.sanity += 5
                    Routes.repeating_first_time(self)
                    print(self.Rpartner)
                    delay_print('"This is the Viscount\'s room. ')
                    sleep(0.5)
                    delay_print('Let\'s begin investigating."')
                    sleep(0.5)
                    input(enter)

                Routes.repeating(self)
                delay_print("\nWhat would you like to do in here?")
                self.been_to_viscount_room = True
                Routes.commands(self)
                
        if self.been_to_viscount_room == True:
            Routes.repeating_first_time(self)
            delay_print("\nWhat would you like to do in here?")
            Routes.commands(self)

    def journal(self):
        self.journal_found = True
        player.location = viscount_room
        player.xp += 25

        Routes.repeating(self)
        delay_print('\n(On the pile of books on the Viscount\'s desk lays his journal with a family crest on it.)')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('(Should I open the journal?)')
        Routes.open_journal(self)
        
    def open_journal(self):
        print('\n\nyes / no')
        open_journal = input('➥ ')

        if open_journal == "yes":
            player.xp += 45
            self.journal_opened = True
            
            Routes.repeating(self)
            delay_print('\nYou open the Viscount\'s journal. ')
            sleep(0.5)
            delay_print('The latest entry reads: ')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            print(viscount)
            delay_print('"It\'s almost time when my child assumes control over my position as the following Viscount.')
            sleep(0.5)
            delay_print('\nIs it even safe to say that they are prepared for the role yet I wonder?')
            sleep(0.5)
            delay_print('\nAs of late, they have been acting rather... ')
            sleep(0.5)
            delay_print('odd... ')
            sleep(0.5)
            delay_print('particularly after we arrived at the Duke\'s banquet earlier today.')
            sleep(0.5)
            delay_print('\nI should check up on them."')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            print(you)
            delay_print('(Wait. ')
            sleep(0.5)
            delay_print('The heir of the next Viscount also attended the banquet the previous evening? ')
            sleep(0.5)
            delay_print('Is it one of us six?)')
            sleep(0.5)
            input(enter)

            if self.alone == False:
                player.sanity += 5

                Routes.repeating(self)
                print(self.Rpartner)
                delay_print('"Find something that interests you?"')
                sleep(0.5)
                input(enter)

                Routes.repeating(self)
                print(you)
                delay_print('"Who is the sucessor of the position of Viscount?"')
                sleep(0.5)
                input(enter)

                if self.partner != "Viscount":
                    Routes.repeating(self)
                    print(self.Rpartner)
                    delay_print('"...')
                    sleep(0.5)
                    delay_print('\n\nIf he didn\'t tell you yet, I believe it\'d be more ideal if you asked him yourself."')
                    sleep(0.5)
                    input(enter)

                if self.partner == "Viscount":
                    Routes.repeating(self)
                    print(self.Rpartner)
                    delay_print('"You will know... ')
                    sleep(0.5)
                    delay_print('in due time. "')
                    sleep(0.5)
                    input(enter)

                Routes.repeating(self)
                print(you)
                delay_print('"Okay... I guess."')
                sleep(0.5)
                input(enter)

                Routes.repeating(self)
                delay_print("\nWhat else would you like to do in here?")
                Routes.commands(self)

            if self.alone == True:
                player.sanity -= 5
                Routes.repeating(self)
                print(you)
                delay_print('(Who is the sucessor of the position of Viscount? ')
                sleep(0.5)
                delay_print('I need to ask someone about this.)')
                sleep(0.5)
                input(enter)

                Routes.repeating(self)
                delay_print("\nWhat else would you like to do in here?")
                Routes.commands(self)

        if open_journal == "no":
            Routes.repeating(self)
            delay_print("\nWhat else would you like to do in here?")
            Routes.commands(self)

        else:
            print('\nPlease try again.')
            Routes.open_journal(self)

    def key(self):
        self.key_found = True
        player.location = viscount_room        
        player.xp += 40
        

        if self.diary_found == True:
            Routes.repeating(self)
            print(you)
            delay_print('(Is this the key to my diary? ')
            sleep(0.5)
            delay_print('I should test it out.)')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print('\n(To test the key in your diary, type: "test key")')
            sleep(0.5)
            
            Routes.open_diary(self)

        if self.diary_found == False:
            Routes.repeating(self)
            print(you)
            delay_print('(I wonder what this key is for?)')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print("\nWhat else would you like to do in here?")
            Routes.commands(self)

    def open_diary(self):
        player.xp += 50
        test_key = input("\n\n➥ ")
            
        if test_key == "test key":
            Routes.repeating(self)
            print(you)
            delay_print('(Wow, it really did open my diary! ')
            sleep(0.5)
            delay_print('But why does the Viscount have the key to my diary?)')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print('\nYou read the latest entry that you wrote. ')
            sleep(0.5)
            delay_print('This entry was written yesterday evening. ')
            sleep(0.5)
            delay_print('\n\nIt reads: ')
            sleep(0.5)
            delay_print('\n"My father and the Duke seem pretty close. ')
            sleep(0.5)
            delay_print('The Duke personally invited me to his study room tonight, saying he has something to talk to me about. ')
            sleep(0.5)
            delay_print('\nI wonder what it could be?"')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            print(you)
            delay_print('"I really was in his study last night! ')
            sleep(0.5)
            delay_print('Meaning, the murder of the old Duke definitely happened before my eyes. ')
            sleep(0.5)
            delay_print('This must be the cause to my amnesia!"')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print("\nWhat else would you like to do in here?")
            Routes.commands(self)

        else:
            print("Don\'t you want to read what\'s in your diary?")
            Routes.open_diary(self)
                

#└────────────────────────────────── Viscount Room ──────────────────────────────────┘

#┌───────────────────────────────── Young Duke Room ─────────────────────────────────┐

    def young_duke_room(self):
        player.location = young_duke_room

        if self.been_to_young_duke_room == False:
            self.room_count += 1
            player.xp += 20

            if self.alone:
                player.sanity -= 3
                Routes.repeating_first_time(self)
                print(you)
                delay_print('(This is the young duke\'s room. ')
                sleep(0.5)
                delay_print('I should take a look around.)')
                sleep(0.5)
                self.been_to_young_duke_room = True
                Routes.commands(self)

            if self.alone == False:
                player.sanity += 5

                if self.partner == "Young Duke":
                    Routes.repeating_first_time(self)
                    print(young_duke)
                    delay_print('"This is my room. ')
                    sleep(0.5)
                    delay_print('I\'ll go explore somewhere else for now and let you thoroughly search my room. ')
                    sleep(0.5)
                    delay_print('We\'ll meet back later."')
                    sleep(0.5)
                    input(enter)
                    self.alone = True

                if self.partner != "Young Duke":
                    player.sanity += 3
                    Routes.repeating_first_time(self)
                    print(self.Rpartner)
                    delay_print('"This is the Young Duke\'s room. ')
                    sleep(0.5)
                    delay_print('Let\'s begin investigating."')
                    sleep(0.5)
                    input(enter)

                Routes.repeating(self)
                delay_print("\nWhat would you like to do in here?")
                self.been_to_young_duke_room = True
                Routes.commands(self)
                
        if self.been_to_young_duke_room == True:
            Routes.repeating_first_time(self)
            delay_print("\nWhat would you like to do in here?")
            Routes.commands(self)

    def notebook(self):
        self.notebook_found = True
        player.xp += 20

        Routes.repeating(self)
        delay_print('\nOn the little podium lays a notebook with unusual sigils marked on it. ')
        sleep(0.5)
        delay_print('Subsequent to opening and assessing what was inside, you discover that the young Duke has been secretly researching anatomy.')
        sleep(0.5)
        input(enter)
        
        Routes.repeating(self)
        print(you)
        delay_print('(But isn\'t human dissection a taboo during this time? ')
        sleep(0.5)
        delay_print('The Duke even goes to a school run by the religious monastery... ')
        sleep(0.5)
        delay_print('I\'ll have to ask him about it later.)')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print("\nWhat else would you like to do in here?")
        Routes.commands(self)

    def letter(self):
        letter_found = True
        player.xp += 5

        Routes.repeating(self)
        delay_print('\nInside the young Duke\'s drawer, there is a small white envelope stamped with a seal.')
        sleep(0.5)
        input(enter)
        Routes.repeating(self)
        print(you)
        delay_print('(Should I open and read it?)')
        sleep(0.5)
        Routes.open_letter(self)

    def open_letter(self):
        print('\n\nyes / no')
        open_letter = input('➥ ')

        if open_letter == "yes":
            player.xp += 10
            self.letter_opened = True
            
            Routes.repeating(self)
            delay_print('\nThe letter is written to the Vatican, requesting the release of the researchers that were labeled as heretics.')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            print(you)
            delay_print('(For what reason would the young Duke request this from the Vatican? ')
            sleep(0.5)
            delay_print('Does he pity those individuals perhaps?)')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print("\nWhat else would you like to do in here?")
            Routes.commands(self)

        if open_letter == "no":
            Routes.repeating(self)
            delay_print("\nWhat else would you like to do in here?")
            Routes.commands(self)

        else:
            print("\nPlease try again.")
            Routes.open_letter(self)

#└───────────────────────────────── Young Duke Room ─────────────────────────────────┘

#┌─────────────────────────────────── Meeting One ───────────────────────────────────┐

    def before_meeting_one(self):
        player.location = corridor
        
        Routes.repeating_first_time(self)
        delay_print('\nAfter collecting evidence from the last room, you and the ')
        delay_print(self.partner)
        delay_print(' decide to go your separate ways to look for more evidence.')
        sleep(0.5)
        delay_print('\nAbout an hour later, ')
        sleep(0.5)
        delay_print('the bell in the castle sounds, ')
        sleep(0.5)
        delay_print('signaling everyone to return and gather at the hall.')
        sleep(0.5)
        delay_print('\nThe first discussion takes place in the courtroom. ')
        sleep(0.5)
        delay_print('Everyone needs to discuss the clues they found and use them to narrow down the potential suspects.')
        sleep(0.5)
        input(enter)

        player.location = courtroom

        Routes.repeating_first_time(self)
        delay_print('\nAs you sit down at the table, ')
        sleep(0.5)
        delay_print('you can feel the tension in the air as everyone starts suspecting each other.')
        sleep(0.5)
        delay_print('\nAs your mind runs wild, the young Duke begins to speak first, breaking the silence in the room.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(young_duke)
        delay_print('"Let us begin now that everyone is here."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nEveryone provided the clues that they found, but it was mostly items that were unrelated to the case.')
        sleep(0.5)
        delay_print('\nAfter the discussion, nobody is eliminated as a suspect. ')
        sleep(0.5)
        delay_print('However, you end up being the most suspicious.')
        sleep(0.5)
        input(enter)

        self.second = True
        Routes.repeating(self)
        print(you)
        delay_print('(Huh...? ')
        sleep(0.5)
        delay_print('So in the end, I\'m the one that everyone suspects the most!?)')
        player.sanity -= 10
        sleep(0.5)
        print(choose)
        print('a) Um.... I don\'t think having amnesia is reason enough to grant suspicion.\nb) (I think I\'m the most suspicious here as well...)\nc) What evidence do you all have that I am the most suspicious here? \nd) ...')
        Routes.commands(self)

    def meeting_one_a_and_c(self):
        Routes.repeating(self)
        player.xp += 5
        print(you)
        delay_print('"Maybe I did witness the murder last night, and my brain made me forget about it in an act of self-defense?')
        sleep(0.5)
        delay_print('\nAnyways, evidence must be provided to suspect anyone. ')
        sleep(0.5)
        delay_print('Simple speculations will only misguide people\'s judgment."')
        sleep(0.5)
        input(enter)

        Routes.meeting_one_continued(self)

    def meeting_one_b_and_d(self):
        Routes.repeating(self)
        player.xp += 5
        print(you)
        delay_print('(Even if I am the most suspicious here, there must be valid evidence.)')
        sleep(0.5)
        input(enter)

        Routes.meeting_one_a_and_c(self)

    def meeting_one_continued(self):
        self.second = False
        
        Routes.repeating(self)
        print(doctor)
        delay_print('"I may have the evidence you speak of... ')
        sleep(0.5)
        delay_print('\n\nHow is this? Is this sufficient to prove that you had something to do with this?"')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        knife = Item("Knife", "⚔", "A silver knife found in your room.")
        knife.putInRoom(courtroom)
        print('       .---.')
        print('       |---|')
        print('       |---|')
        print('   .---^ - ^---.')
        print('   :___________:')
        print('      |  |//|')
        print('      |  |//|')
        print('      |  |//|')
        print('      |  |//|')
        print('      |  |//|')
        print('      |  |.-|')
        print("      |.-'**|")
        print('       \\***/')
        print('        \\*/')
        print('         V')   
        delay_print('\nThe doctor drops a small silver knife onto the table.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(doctor)
        delay_print('"I found this in the heart of the body."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nThen, the doctor takes something else out from his pocket. ')
        sleep(0.5)
        delay_print('It is a sheath made of silver.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(doctor)
        delay_print('"After taking the knife, I coincidentally found the sheath in your room.')
        sleep(0.5)
        delay_print('\nThe Viscount confirms that he gave this silver knife to you, who always has it on your person."')
        player.sanity -= 5
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        player.sanity -= 13
        delay_print('\nIn a matter of seconds, everyone is focused on you.')
        sleep(0.5)
        input(enter)
        
        Routes.repeating(self)
        print(you)
        delay_print('(How can this be... ')
        sleep(0.5)
        delay_print('How can I prove my timeline without my memories... ')
        sleep(0.5)
        delay_print('I have no alibi... ')
        sleep(0.5)
        delay_print('What can I do?)')
        player.sanity -= 3
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nYou remain silent, unable to refute what he just said. ')
        sleep(0.5)
        delay_print('Suddenly, the young Duke stands up and puts a notebook down on the table.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        alchemy_notebook = Item("Alchemy Notebook", "✎", "belongs to the Doctor, contains information on black magic and alchemy.")
        alchemy_notebook.putInRoom(courtroom)
        print(young_duke)
        delay_print('"If that\'s all the evidence you can provide, then I also have evidence..."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)        
        print()
        print('        _.-"\\')
        print('     .-"     \\')
        print(' ,-"          \\')
        print('( \\            \\')
        print(' \\ \\            \\')
        print('  \\ \\            \\')
        print('   \\ \\         _.-;')
        print('    \\ \\    _.-"   :')
        print('     \\ \\,-"    _.-"')
        print('      \\(   _.-"  ')
        print('       `--"')
        print(young_duke)
        delay_print('"This was in your room. ')
        sleep(0.5)
        delay_print('As a doctor, you have many books on black magic, including this notebook on alchemy."')
        player.sanity += 5
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print()
        print('      __...--~~~~~-._   _.-~~~~~--...__')
        print("    //               `V'               \\\\ ")
        print('   //                 |                 \\\\ ')
        print('  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\\\ ')
        print(' //__.....----~~~~._\ | /_.~~~~----.....__\\\\')
        print('====================\\|//====================')
        print('                    `---`')
        delay_print('\nThe young Duke turns the notebook to one of the pages, and pushes it to the middle of the round table. ')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print()
        print('      __...--~~~~~-._   _.-~~~~~--...__')
        print("    //               `V'               \\\\ ")
        print('   //                 |                 \\\\ ')
        print('  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\\\ ')
        print(' //__.....----~~~~._\ | /_.~~~~----.....__\\\\')
        print('====================\\|//====================')
        print('                    `---`')
        print(young_duke)
        delay_print('"This magic circle, in the last entry from two days ago, is identical to the one found under the body."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print()
        print('      __...--~~~~~-._   _.-~~~~~--...__')
        print("    //               `V'               \\\\ ")
        print('   //                 |                 \\\\ ')
        print('  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\\\ ')
        print(' //__.....----~~~~._\ | /_.~~~~----.....__\\\\')
        print('====================\\|//====================')
        print('                    `---`')
        print(young_duke)
        delay_print('"Based on this, the doctor, who wants to experiment on real people using alchemy, seems much more suspicious, am I right?"')
        sleep(0.5)
        player.sanity += 10
        input(enter)

        Routes.repeating(self)
        delay_print('\nAfter the young Duke\'s speech, the doctor doesn\'t utter another word. ')
        sleep(0.5)
        delay_print('\n\nThen... the young Duke suddenly looks at you.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(young_duke)
        delay_print('"In your room however, other than the sheath and a piece of silk with lily embroiders, there was nothing suspicious."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nAfter the young Duke\'s analysis, it becomes hard for you the be the only sole suspect.')
        sleep(0.5)
        player.sanity += 10
        delay_print('\nAfter everyone shares their suspicions, no one is eliminated as a suspect, so the discussion goes nowhere.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nOne hour later... ')
        sleep(0.5)
        delay_print('Everyone decides to continue investigating.')
        input(enter)

        if self.notebook_found or self.letter_opened:
            Routes.repeating(self)
            print(you)
            delay_print('"Duke... ')
            sleep(0.5)
            delay_print('I have a question for you!"')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print('\nYou stop the young Duke after everyone else has left the room.')
            sleep(0.5)
            input(enter)

            if self.notebook_found == True:

                Routes.repeating(self)
                print(you)
                delay_print('"Don\'t you go to school at a monastery? ')
                sleep(0.5)
                delay_print('Why would you be learning about the banned practices of dissections?"')
                sleep(0.5)
                input(enter)

            if self.letter_opened == True:
                Routes.repeating(self)
                print(you)
                delay_print('"What about the written letter in your drawer asking the Vatican to release the scholars labeled as heretics...?')
                sleep(0.5)
                delay_print('\nAre you unahppy with the Vatican?"')
                sleep(0.5)
                input(enter)

            Routes.repeating(self)
            print(young_duke)
            delay_print('"They refuse to investigate the truth behind a murder simply because of taboo. ')
            sleep(0.5)
            delay_print('The foundations of their existence were shaken. ')
            sleep(0.5)
            delay_print('In response, they harmed the scholars who desire and bring change. ')
            sleep(0.5)
            delay_print('\nGiven that, would you still feel safe leaving your faith and future with the Vatican?"')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print('\nHis cold voice makes you sink deep into thought.')
            player.sanity -= 5
            sleep(0.5)
            input(enter)

        elif self.been_to_young_duke_room == False:
            Routes.repeating(self)
            delay_print('\nAfter everyone has left the room, the young Duke stops you.')
            sleep(0.5)
            input(enter)

        #need another check command for 2nd option in same def function
        Routes.repeating(self)
        print(young_duke)
        delay_print('"That doctor... be wary of him. ')
        sleep(0.5)
        delay_print('He shared too little information during the discussion. ')
        sleep(0.5)
        delay_print('\nThe magic circle under the body had alchemy sigils. ')
        sleep(0.5)
        delay_print('Even if he is not the murderer, he is still somehow involved."')
        sleep(0.5)
        input(enter)

        if self.partner != "Young Duke":
            Routes.repeating(self)
            delay_print('\nAfter the young Duke takes his leave, you spot a person waiting for you across the courtroom.')
            sleep(0.5)
            input(enter)

        Routes.repeating(self)
        print(Rpartner)
        delay_print('"There is a room in this castle that you might want to see. ')
        sleep(0.5)
        delay_print('Do you want to go take a look? ')
        sleep(0.5)
        delay_print('If you are afraid... "')
        sleep(0.5)
        input(enter)
        
        Routes.repeating(self)
        print(you)
        delay_print('"Of course I\'m going!"')
        sleep(0.5)
        input(enter)
        
        Routes.repeating(self)
        print(Rpartner)
        delay_print('"Alright... ')
        sleep(0.5)
        delay_print('It is not something you will want to see though... ')
        sleep(0.5)
        delay_print('Please follow me."')
        player.sanity += 5
        sleep(0.5)
        input(enter)
        self.alone = False
        Routes.penetralium(self)

#└─────────────────────────────────── Meeting One ───────────────────────────────────┘

#┌────────────────────────────────── Penetralium ────────────────────────────────────┐

    def penetralium(self):
        player.location = penetralium

        Routes.repeating_first_time(self)
        delay_print('\nUpon reaching the end of the corridor, you finally see what the ')
        delay_print(self.partner)
        delay_print(' didn\'t want you to see.')
        sleep(0.5)
        delay_print('\nRusted red chains lay on the floor. ')
        player.sanity -= 3
        sleep(0.5)
        delay_print('\nBehind the heavy doors, alchemy sigils cover the walls in the secret candle-lit room. ')
        sleep(0.5)
        delay_print('\n\nOn the wall, it reads:')
        delay_print('\n"If the God I worship cannot save my lover, then I will sell my soul to the devil in exchange for her second life."')
        sleep(0.5)
        input(enter)

        Routes.old_duke_room(self)

#└────────────────────────────────── Penetralium ────────────────────────────────────┘

#┌────────────────────────────────── Old Duke Room ──────────────────────────────────┐

    def old_duke_room(self):
        self.alone = False
        self.the_truth = True
        
        player.location = old_duke_room
        self.old_duke_room_unlocked = True

        if self.been_to_old_duke_room == False:
            self.room_count += 1

        Routes.repeating_first_time(self)
        delay_print('\nLeaving the creepy secret room, you and the ')
        delay_print(self.partner)
        delay_print(' go to the crime scene in silence to look for clues.')
        sleep(0.5)
        input(enter)

        if self.alone == False:
            if self.partner == "Young Duke":
                Routes.repeating(self)
                print(young_duke)
                delay_print('"This is my father\'s room. ')
                sleep(0.5)
                delay_print('Preliminary analysis indicates that he suffered blunt force trauma to the head, and died due to blood loss."')
                sleep(0.5)
                input(enter)
                
            if self.partner != "Young Duke":
                Routes.repeating(self)
                print(Rpartner)
                delay_print('"This is the old Duke\'s room. ')
                sleep(0.5)
                delay_print('Preliminary analysis indicates that he suffered blunt force trauma to the head, and died due to blood loss."')
                sleep(0.5)
                input(enter)

            Routes.repeating(self)
            print(you)
            delay_print('"Preliminary...? ')
            player.sanity += 5
            sleep(0.5)
            delay_print('Sounds like they didn\'t do a thorough investigation on the cause of death yet."')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            print(Rpartner)
            delay_print('"Maybe there was something that stopped them from continuing with their investigation. ')
            sleep(0.5)
            delay_print('Something... ')
            sleep(0.5)
            delay_print('that scares even the Vatican... "')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            print(you)
            delay_print('"What would the churches be afraid of?"')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            print(Rpartner)
            delay_print('"Black magic. ')
            sleep(0.5)
            delay_print('Black magic that twists humanity.')
            sleep(0.5)
            delay_print('\nMany forward thinkers were labeled as heretics by the church. ')
            sleep(0.5)
            delay_print('Thus, suffered execution or exile."')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print("\nWhat would you like to do in here?")
            Routes.commands(self)
                
        if self.been_to_old_duke_room == True:
            Routes.repeating_first_time(self)
            delay_print("\nWhat would you like to do in here?")
            self.been_to_old_duke_room = True
            Routes.commands(self)

    def lilies(self):
        lilies_found = True
        player.location = old_duke_room

        Routes.repeating(self)
        print('               __/)')
        print('            .-(__(=:')
        print('            |    \\)')
        print('      (\__  |')
        print('     :=)__)-|  __/)')
        print('      (/    |-(__(=:')
        print('    ______  |  _ \\)')
        print('   /      \\ | / \\')
        print('        ___\\|/___\\')
        print('       [         ]\\')
        print('        \\       /  \\')
        print('         \\     /')
        print('          \\___/')
        print(you)
        delay_print('"Why are there so many lilies in this room?"')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nWalking into the room, the large vases of lily blooms on the table are what immediately catches your eye. ')
        sleep(0.5)
        delay_print('\nThe pure white flowers are a stark contrast to the very dim light and the scattered books on the ground.')
        sleep(0.5)
        delay_print('\nAmidst the piles of books, a body is covered with a black cloth. ')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print('               __/)')
        print('            .-(__(=:')
        print('            |    \\)')
        print('      (\__  |')
        print('     :=)__)-|  __/)')
        print('      (/    |-(__(=:')
        print('    ______  |  _ \\)')
        print('   /      \\ | / \\')
        print('        ___\\|/___\\')
        print('       [         ]\\')
        print('        \\       /  \\')
        print('         \\     /')
        print('          \\___/')
        print(you)
        delay_print('(The ')
        delay_print(self.partner)
        delay_print(' said that I was found laying here. ')
        sleep(0.5)
        delay_print('Could my amnesia have something to do with having witnessed the murder?')
        sleep(0.5)
        delay_print('\nAnd why are there so many lilies in this room?)')
        input(enter)

        Routes.repeating(self)
        delay_print("\nWhat else would you like to do in here?")
        Routes.commands(self)

    def body(self):
        player.location = old_duke_room

        if self.alone == False:
            Routes.repeating(self)
            delay_print('\nThe ')
            delay_print(self.partner)
            delay_print(' squats down next to the body, seeing a strange symbol hidden between the scattered books on the ground.')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            print(Rpartner)
            delay_print('"It\'s hard to see in here... ')
            sleep(0.5)
            delay_print('Would you have anything to light up the candles around this room?"')
            sleep(0.5)
            input(enter)

            if self.matches_found == True:
                if self.partner == "Duchess":
                    Routes.repeating(self)
                    print(you)
                    delay_print('"I do! ')
                    sleep(0.5)
                    delay_print('I found it earlier in the Duchess\' room actually...')
                    sleep(0.5)
                    input(enter)
                    
                if self.partner != "Duchess":
                    Routes.repeating(self)
                    print(you)
                    delay_print('"I do! ')
                    sleep(0.5)
                    delay_print('I found it in your room earlier actually...')
                    sleep(0.5)
                    input(enter)

                Routes.repeating(self)
                delay_print('\nYou light the match onto the candle and light up the area in front of you.')
                sleep(0.5)
                input(enter)

                Routes.body_continued(self)

            if self.matches_found == False:
                Routes.repeating(self)
                print(you)
                delay_print('"No, I do not. ')
                sleep(0.5)
                delay_print('Would you know where I could find some matches around here?"')
                sleep(0.5)
                input(enter)

                if self.partner == "Duchess":
                    Routes.repeating(self)
                    print(Rpartner)
                    delay_print('"I think I have some in my room. ')
                    sleep(0.5)
                    delay_print('Do you mind getting them?"')
                    sleep(0.5)
                    input(enter)

                if self.partner != "Duchess":
                    Routes.repeating(self)
                    print(Rpartner)
                    delay_print('"I think I saw some matches in the Duchess\' room earlier. ')
                    sleep(0.5)
                    delay_print('Do you mind getting them?"')
                    sleep(0.5)
                    input(enter)

                Routes.repeating(self)
                print(you)
                delay_print('"No, of course I don\'t mind, I\'ll go get them.')
                sleep(0.5)
                delay_print('I\'ll be back. ')
                sleep(0.5)
                delay_print('Please stay safe!"')
                sleep(0.5)
                input(enter)

                self.alone = True
                self.need_matches = True
                player.sanity -= 5
                Routes.duchess_room(self)

    def body_continued(self):
        player.location = old_duke_room
        
        if self.matches_candle == True:
            Routes.repeating_first_time(self)
            print(you)
            delay_print('"I got the matches."')
            sleep(0.5)
            input(enter)

        Routes.repeating(self)
        delay_print('\nYou light the match and the candle from the wall, and light up the area in front of you.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(Rpartner)
        delay_print('"We should move some of these books. ')
        sleep(0.5)
        delay_print('Something red seems to have been drawn on the ground."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nYou and the ')
        delay_print(self.partner)
        delay_print(' move the books to the side. ')
        sleep(0.5)
        delay_print('Soon, the full image is revealed before your eyes.')
        sleep(0.5)
        delay_print('\n\n... It\'s a magic circle made of many symbols. ')
        sleep(0.5)
        input(enter)
        
        Routes.repeating(self)
        print(you)
        delay_print('"This is... ')
        sleep(0.5)
        delay_print('a magic circle... ')
        sleep(0.5)
        delay_print('drawn with... ')
        sleep(0.5)
        delay_print('blood."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(Rpartner)
        delay_print('"Alchemy sigils. ')
        sleep(0.5)
        delay_print('I do not know much about alchemy. ')
        sleep(0.5)
        delay_print('My knowledge is limited to these symbols."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nIn the corners of the magic circle, there is a shattered cryolite, a feather, a silver cup, and a burnt candle. ')
        sleep(0.5)
        delay_print('\nThe bottom of the items, having been on the magic circle, are stained with blood, especially the crystal.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"Looks like the death of the old Duke is related to some sort of ritual... "')
        sleep(0.5)
        input(enter)
        
        Routes.repeating(self)
        delay_print('\nIn an instant, the black cloth was removed by the ')
        delay_print(self.partner)
        delay_print('.')
        sleep(0.5)
        delay_print('What was hidden underneath became revealed.')
        sleep(0.5)
        delay_print('\nThe old Duke was dressed in lavished clothing, and is soaked in blood, facing down in the middle of the magic circle.')
        sleep(0.5)
        delay_print('You can see blood stains on the cryolite.')
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"This must have been what was used to attack him."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nYou both then flip the body over, and notice that the scarf was dyed in blood. ')
        sleep(0.5)
        delay_print('With his gloves on, the ')
        delay_print(self.partner)
        delay_print(' tugs the scarf away... ')
        sleep(0.5)
        delay_print('\nThere is a small wound near the heart on the chest, but you can\'t determine how deep the wound is.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(Rpartner)
        delay_print('"It is a small wound, probably made by a weapon that is sharp, thin, and long. ')
        sleep(0.5)
        delay_print('But it is no longer here. "')
        player.sanity += 5
        sleep(0.5)
        input(enter)

        if self.partner == "Doctor":
            Routes.repeating(self)
            print(you)
            delay_print('(Yeah... you took it earlier...)')
            sleep(0.5)
            input(enter)

        if self.partner != "Doctor":
            Routes.repeating(self)
            print(you)
            delay_print('"Oh right... the Doctor took it earlier."')
            sleep(0.5)
            input(enter)

        Routes.repeating(self)
        delay_print("\nWhat else would you like to do in here?")
        self.body_searched = True
        Routes.commands(self)

    def body_searched(self):
        player.location = old_duke_room

        Routes.repeating(self)
        print(you)
        delay_print('(I already searched through the body.)')
        sleep(0.5)
        input(enter)

        Routes.commands(self)

    def bookmark(self):
        player.location = old_duke_room
        Routes.repeating(self)
        delay_print('\n(On the bookshelf, you find the old Duke\'s diary, revealing the dark secrets behind the penetralium.)')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('(The old Duke was in love with a nun, but the rules of the monastery forbade her from marriage, forcing him to leave her.')
        sleep(0.5)
        delay_print('\nThe lily bookmark inside this diary seems to be the final gift she gave him before their breakup.')
        sleep(0.5)
        input(enter)
        
        if self.alone == False:
            Routes.repeating(self)
            delay_print('\n(The ')
            delay_print(self.partner)
            delay_print(' stands in front of the desk. ')
            sleep(0.5)
            delay_print(self.Bgender)
            delay_print('looks down, gently running ')
            delay_print(BgenderHisHer)
            delay_print(' fingers across the white lily petals.')
            sleep(0.5)
            input(enter)

        Routes.repeating(self)
        print(Rpartner)
        delay_print('"Lilies are the divine flower of the Vatican, and also her favorite. ')
        sleep(0.5)
        delay_print('The lilies in his room remind him of her, and his study is always filled with them')
        sleep(0.5)
        input(enter)

        if self.alone == True:
            Routes.repeating(self)
            delay_print('\nThe ')
            delay_print(self.partner)
            delay_print(' walks into the room with a melancholy look in ')
            delay_print(Sgenderhisher)
            delay_print(' eyes.')
            sleep(0.5)
            input(enter)

        Routes.repeating(self)
        delay_print('\n(You continue to read the diary.)')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"Soon after they split, the nun was burned to death for violating the religious doctrine."')
        sleep(0.5)
        delay_print('\n\n(Why? ')
        sleep(0.5)
        delay_print('What did the nun do to have to go through such a painful torture?)')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(Rpartner)
        delay_print('"After the nun\'s death, he was driven insane. ')
        sleep(0.5)
        delay_print('He even invited an alchemist to stay at the castle to perform rituals in hopes of reviving her. ')
        sleep(0.5)
        delay_print('\nThis alchemist... ')
        sleep(0.5)
        delay_print('is the doctor here.')
        sleep(0.5)
        delay_print('\nThey built a penetralium in this castle and used his status as the Duke to lure many common men and women that had any of the same features as her. ')
        sleep(0.5)
        delay_print('\nThose innocent people believed they were going to be enjoying a lifetime of riches, but ended up becoming sacrifices."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('(...and the young Duke was a witness to it ever since a young age too...)')
        sleep(0.5)
        input(enter)

        if self.partner == "Viscount":
            Routes.repeating(self)
            print(Rpartner)
            delay_print('"He eventually grew tired of trying to resurrect his lover. ')
            sleep(0.5)
            delay_print('Thus, the penetralium was abandoned.')
            sleep(0.5)
            delay_print('\nA year ago, I wrote in a letter, saying that I hoped to visit with my newly adopted child...')
            sleep(0.5)
            delay_print('\n\nYou."')
            sleep(0.5)
            input(enter)
            
        if self.partner != "Viscount":
            Routes.repeating(self)
            print(Rpartner)
            delay_print('"He eventually grew tired of trying to resurrect his lover. ')
            sleep(0.5)
            delay_print('Thus, the penetralium was abandoned.')
            sleep(0.5)
            delay_print('\nA year ago, the Viscount wrote in a letter, saying that he hoped to visit with his newly adopted child...')
            sleep(0.5)
            delay_print('\n\nYou."')
            sleep(0.5)
            input(enter)

        if self.journal_opened == True:
            Routes.repeating(self)
            print(you)
            delay_print('"So, the person the Viscount mentioned in his journal was... me?? ')
            sleep(0.5)
            delay_print('I\'m the heir to the position as Viscount?"')
            sleep(0.5)
            input(enter)

        if self.journal_opened == False:
            Routes.repeating(self)
            print(you)
            delay_print('"..."')
            sleep(0.5)
            input(enter)

        Routes.repeating(self)
        delay_print('\n(You continued to read the diary.)')
        sleep(0.5)
        input(enter)

        if self.partner == "Viscount":
            Routes.repeating(self)
            print(you)
            delay_print('"It writes, as you arrived, the old Duke was shocked to find that my face was... "')
            sleep(0.5)
            player.sanity -= 5
            input(enter)

        if self.partner != "Viscount":
            Routes.repeating(self)
            print(you)
            delay_print('"It writes, as the Viscount arrived, the old Duke was shocked to find that my face was... "')
            sleep(0.5)
            player.sanity -= 5
            input(enter)

        Routes.repeating(self)
        print(Rpartner)
        delay_print('"Yes. ')
        sleep(0.5)
        delay_print('Your looks were identical to the nun. ')
        sleep(0.5)
        delay_print('The brooch you are wearing is proof of his love for the nun, something he gave her back then..."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        player.sanity -= 5
        delay_print('\nSuddenly, a small smile appears on the ')
        delay_print(self.partner)
        delay_print('\'s face.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(Rpartner)
        delay_print('"It is just as you think. ')
        sleep(0.5)
        delay_print('His first encounter with you rekindled his desire for a wish he had almost given up. ')
        sleep(0.5)
        delay_print('This time, he decided to try one last time by using you to complete the ritual and reunite them once more."')
        input(enter)

        if self.partner == "Viscount":
            Routes.repeating(self)
            print(you)
            delay_print('"So... your adopted child, meaning me, is actually the old Duke\'s..."')
            sleep(0.5)
            input(enter)

        if self.partner == "Viscount":  
            Routes.repeating(self)
            print(you)
            delay_print('"So... the adopted child of the Viscount, meaning me, is actually the old Duke\'s..."')
            sleep(0.5)
            input(enter)

        Routes.repeating(self)
        print(Rpartner)
        delay_print('"Yes. ')
        sleep(0.5)
        delay_print('You are the true child of him and the nun. ')
        sleep(0.5)
        delay_print('Your birth is also the reason for the nun\'s death by burning."')
        player.sanity -= 10
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"So... ')
        sleep(0.5)
        delay_print('the banquet last night was actually a trap set up by the old Duke to kidnap me... ')
        sleep(0.5)
        delay_print('and to sacrifice me for the ritual.')
        sleep(0.5)
        delay_print('\n\nAll the others might have motives for murder, but I was the only one whose life was actually in danger."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(Rpartner)
        delay_print('"Although, I do know that the cause of your amnesia was not because of shock. ')
        sleep(0.5)
        delay_print('The old Duke performed a ritual on you without you knowing, which ultimately led you to lose your memories."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"You... ')
        sleep(0.5)
        delay_print('You knew all along... ')
        sleep(0.5)
        delay_print('Why didn\'t you say anything?"')
        player.sanity -= 2
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(Rpartner)
        delay_print('"You killed the demon, saved yourself, and at the same time, saved countless lives that could have fell at his hands.')
        sleep(0.5)
        delay_print('\nWhat you did was just, but you will end up tried and punished as a murderer."')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"..."')
        sleep(0.5)
        input(enter)
        
        if self.partner != "Doctor":
            Routes.repeating(self)
            print(Rpartner)
            delay_print('"Although... ')
            sleep(0.5)
            delay_print('For years, the castle has practiced black magic, which the Vatican vehemently forbids. ')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            print(you)
            delay_print('"You mean... ')
            sleep(0.5)
            delay_print('that I should redirect the blame onto the doctor, who\'s also an alchemist...?"')
            sleep(0.5)
            input(enter)

        if self.partner == "Doctor":
            Routes.repeating(self)
            print(Rpartner)
            delay_print('"Although... ')
            sleep(0.5)
            delay_print('For years, the castle has practiced human dissection, which the Vatican vehemently forbids. ')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            print(you)
            delay_print('"You mean... ')
            sleep(0.5)
            delay_print('that I should redirect the blame onto the young Duke, who also studies banned anatomy...?"')
            sleep(0.5)
            input(enter)


        Routes.repeating(self)
        print(Rpartner)
        delay_print('"It is not my choice to make."')
        sleep(0.5)
        input(enter)

        Routes.finale(self)
            

#└────────────────────────────────── Old Duke Room ──────────────────────────────────┘

#┌───────────────────────────────────── Finale ──────────────────────────────────────┐

    def finale(self):
        player.location = your_room
        player.sanity += 20

        Routes.repeating_first_time(self)
        delay_print('\nAfter that, you used the remaining time to collect your thoughts in your room.')
        sleep(0.5)
        delay_print('\nYou give a big sigh.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"The ')
        delay_print(self.partner)
        delay_print(' was trying to hide the truth from me because ')
        delay_print(Sgender)
        delay_print(' thinks what I did was right... ')
        sleep(0.5)
        delay_print('\n\nWhat do I do...?"')
        player.sanity -= 5
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nWith all the evidence grasped tightly in your hands, the final bell sounds.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"Well... here goes nothing."')
        player.sanity -= 3
        sleep(0.5)
        input(enter)

        player.location = courtroom

        Routes.repeating_first_time(self)
        delay_print('\nThe other are already waiting for you when you arrive.')
        player.sanity += 2
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(duchess)
        delay_print('"So, what is our conclusion?"')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('(Well... ')
        sleep(0.5)
        delay_print('this is it... ')
        sleep(0.5)
        delay_print('I should tell everyone what I have decided.)')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        delay_print('\nYou stand up from your chair, and everyone has their eyes on you.')
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(you)
        delay_print('"I... ')
        sleep(0.5)
        delay_print('I have made a conclusion..."')
        player.sanity -= 3
        sleep(0.5)
        input(enter)

        Routes.repeating(self)
        print(young_duke)
        delay_print('"Let us all hear it then."')
        sleep(0.5)
        input(enter)

        Routes.final_choice(self)

    def final_choice(self):
        player.location=courtroom

        Routes.repeating(self)
        print(you)
        print("\nWho murdered the old Duke?:")
        print('a) You')
        print('b) Viscount')
        print('c) Duchess')
        print('d) Butler')
        print('e) Doctor')
        print('f) Young Duke')
        final_decision = input("\n\n➥ ")

        if final_decision == "a":
            Routes.repeating(self)
            delay_print('\nYou told everyone who the murderer most likely was, and laid out all the evidence, particularly the old Duke\'s diary.')
            sleep(0.5)
            delay_print('\nYou decide to not mention the banned practices of alchemy performed by the Doctor.')
            sleep(0.5)
            input(enter)
            
            Routes.victory(self)

        if final_decision == "b":
            Routes.repeating(self)
            delay_print('\nAfter redirecting the blame to someone else, your evidence was insufficient. ')
            sleep(0.5)
            delay_print('Thus, your conclusion was invalid to everyone.')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print('\nAfter everyone gives their conclusion, the majority vote for the ')
            delay_print(self.partner)
            delay_print('\'s conclusion.')
            sleep(0.5)
            input(enter)

            Routes.victory_i_guess(self)

        if final_decision == "c":
            Routes.repeating(self)
            delay_print('\nAfter redirecting the blame to someone else, your evidence was insufficient. ')
            sleep(0.5)
            delay_print('Thus, your conclusion was invalid to everyone.')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print('\nAfter everyone gives their conclusion, the majority vote for the ')
            delay_print(self.partner)
            delay_print('\'s conclusion.')
            sleep(0.5)
            input(enter)

            Routes.victory_i_guess(self)

        if final_decision == "d":
            Routes.repeating(self)
            delay_print('\nAfter redirecting the blame to someone else, your evidence was insufficient. ')
            sleep(0.5)
            delay_print('Thus, your conclusion was invalid to everyone.')
            sleep(0.5)
            input(enter)

            Routes.repeating(self)
            delay_print('\nAfter everyone gives their conclusion, the majority vote for the ')
            delay_print(self.partner)
            delay_print('\'s conclusion.')
            sleep(0.5)
            input(enter)

            Routes.victory_i_guess(self)

        if final_decision == "e":
            if self.partner != "Doctor":
                Routes.repeating(self)
                delay_print('\nYou decide to redirect the blame to the doctor. ')
                sleep(0.5)
                delay_print('With the help of the old Duke\'s diary as your primary evidence, your concusion was succesful.')
                sleep(0.5)
                input(enter)
                
            if self.partner == "Doctor":
                Routes.repeating(self)
                delay_print('\nAfter redirecting the blame to someone else, your evidence was insufficient for everyone to agree upon. ')
                sleep(0.5)
                delay_print('Thus, your conclusion did not go through.')
                sleep(0.5)
                input(enter)

                Routes.repeating(self)
                delay_print('\nAfter everyone gives their conclusion, the majority vote for the ')
                delay_print(self.partner)
                delay_print('\'s conclusion.')
                sleep(0.5)
                input(enter)

            Routes.victory_i_guess(self)

        if final_decision == "f":
            if self.partner != "Young Duke":
                Routes.repeating(self)
                delay_print('\nYou decide to redirect the blame to the young Duke. ')
                sleep(0.5)
                delay_print('With the help of his own notebook as your primary evidence, your concusion was succesful.')
                sleep(0.5)
                input(enter)

            if self.partner == "Young Duke":
                Routes.repeating(self)
                delay_print('\nAfter redirecting the blame to someone else, your evidence was insufficient for everyone to agree upon. ')
                sleep(0.5)
                delay_print('Thus, your conclusion did not go through.')
                sleep(0.5)
                input(enter)

                Routes.repeating(self)
                delay_print('\nAfter everyone gives their conclusion, the majority vote for the ')
                delay_print(self.partner)
                delay_print('\'s conclusion.')
                sleep(0.5)
                input(enter)

            Routes.victory_i_guess(self)
            
        else:
            print("Please try again.")
            Routes.final_choice(self)

    def victory(self):
        clear()
        delay_print('So... ')
        sleep(0.5)
        delay_print('You found the murderer in the end... ')
        sleep(0.5)
        delay_print('\n\nBut at what cost? ')
        sleep(0.5)
        input(enter)

        Routes.fireworks(self)

    def victory_i_guess(self):
        clear()
        delay_print('So... ')
        sleep(0.5)
        delay_print('You were able to escape the castle in one peace... ')
        sleep(0.5)
        delay_print('\n\nBut at what cost? ')
        sleep(0.5)
        input(enter)

        Routes.fireworks(self)

    def fireworks(self):
        clear()
        print("")
        print("")
        print("")
        print("")
        print("")                             
        print("                            '")         
        print("                           .")
        print("                           .")
        print("")
        print("                          '")
        print("                          .")
        print("                         .")
        sleep(0.3)

        clear()
        print("")
        print("")
        print("")
        print("                            _\/_")
        print("                             /\\")
        print("                            '")
        print("                           .")
        print("                           .")
        print("")
        print("                          '")
        print("                          .")
        print("                         .")
        sleep(0.3)

        clear()
        print("")
        print("")           
        print("                            *  *")
        print("                           *_\/_*") 
        print("                           * /\ *")    
        print("                            *  *")
        print()
        print()
        print()
        print()
        print()
        print()
        sleep(0.3)

        clear()
        print("")
        print("")           
        print("                            *  *")
        print("               _\/_        *    * .::.")
        print("          .''.  /\         *    *:_\/_:")   
        print("         :_\/_:             *  * : /\ :")
        print("         : /\ :              o    '::'")
        print("          '::'")
        print()
        print()
        print()
        print()
        sleep(0.3)

        clear()
        print("")
        print("")                              
        print("               .''.          *    ")
        print("              :_\/_:              .::.")
        print("          .''.: /\ :             :    :")  
        print("         :    :'::'         \\'/  :    :")
        print("         :    :            = o =  '::'") 
        print("         :    :             /.\\")
        print("          '..'")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("")
        print("                           _\\)/_")  
        print("               .''.         /(\\   ")
        print("              :    :              _\\/_")
        print("          .''.:    :         :     /\\")  
        print("         :    :'..'       '.\\'/.'   ")
        print("         :    :           -= o =-   ") 
        print("         :    :           .'/.\\'.")
        print("          '..'               :   ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("")
        print("                           _\\)/_")  
        print("               .''.         /(\\   .''. ")
        print("              :    :         '   :_\\/_:")
        print("              :    :         :   : /\\ :")  
        print("               '..'       '  '  ' '..'")
        print("                          -=   =-   ") 
        print("                          .' . '.")
        print("                             :   ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("")
        print("                               ")  
        print("               _\\/_               .''. ")
        print("                /\\               :    :")
        print("                                 :    :")  
        print("                                  '..'")
        print("                              ") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("                              \\'/      ")
        print("               *  *          = o = ")  
        print("              *_\\/_*          /.\\ .''. ")
        print("              * /\\ *             :    :")
        print("               *  *              :    :")  
        print("                                  '..'")
        print("                              ") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("                            '.\\'/.'    ")
        print("               *  *          = o = ")  
        print("              *    *        .'/.\\'. ")
        print("              *    *           :")
        print("               *  *              ")  
        print("                                ")
        print("                              ") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("                            '.\\'/.'    ")
        print("                             =   = ")  
        print("                  o         .'/.\\'. ")
        print("        o                      :")
        print("                                  .:. ")  
        print("                                  ':'")
        print("                              ") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("                            '. ' .'    ")
        print("                 \\'/         =   = ")  
        print("       \\'/      = o =       .' . '. ")
        print("      = o =      /.\\           :  .:::.")
        print("       /.\\                       :::::::")  
        print("                                  ':::'")
        print("                              ") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("                  :        ")
        print("        :      '.\\'/'.   ")  
        print("     '.\\'/.'   -= o =-            .:::. ")
        print("     -= o =-   .'/.\\'.           :::::::")
        print("     .'/.\\'.      :              :::::::")  
        print("        :                         ':::'")
        print("                              ") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("                  :        ")
        print("        :      '.\\'/'.               ")  
        print("     '.\\'/.'   -=   =-        *   .:::. ")
        print("     -=   =-   .'/.\\'.           ::' '::")
        print("     .'/.\\'.      :              ::. .::")  
        print("        :                         ':::'")
        print("                              ") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.5)

        clear()
        print("                  :           .")
        print("        :      '. ' '.      _\\)/)     ")  
        print("     '. ' .'   -=   =-       /(\\  .'''. ")
        print("     -=   =-   .' . '.        '  :     :")
        print("     .' . '.      :              :     :")  
        print("        :                         '...'")
        print("                              ") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("                              .")
        print("                            _\\)/)         _\\/_")  
        print("                             /(\\   _\\/_    /\\")
        print("                              '     /\\")
        print("                                  ")  
        print("                                 ")
        print("                              ") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("                              .           .''.")
        print("                            _\\)/)  .''.  :_\\/_:")  
        print("                             /(\\  :_\\/_: : /\\ :")
        print("                              '   : /\\ :  '..'")
        print("           o                       '..' ")  
        print("                                 ")
        print("                              ") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("                                          .''.")
        print("                                   .''.  :    :")  
        print("                           _\\/_   :    : :    :")
        print("          \\'/               /\\    :    :  '..'")
        print("         = o =                _\\/_ '..' ")  
        print("          /.\\                  /\\")
        print("                              ") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("                                     ")
        print("                           .''.     ")  
        print("           :              :_\\/_:  ")
        print("        '.\\'/.'           : /\\.:'  ")
        print("        -= o =-            '.:_\\/_: ")  
        print("        .'/.\\'.              : /\\ :")
        print("           :                  '..'") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("                                     ")
        print("                           .''.     ")  
        print("           :              :    :  ")
        print("        '.\\'/.'           :   .:'  ")
        print("        -=   =-            '.:    : ")  
        print("        .'/.\\'.              :    :")
        print("           :                  '..'") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.3)

        clear()
        print("                                     ")
        print("                           .''.     ")  
        print("           :              :    :  ")
        print("        '. ' .'           :   .:'  ")
        print("        -=   =-            '.:    : ")  
        print("        .' . '.              :    :")
        print("           :                  '..'") 
        print("                          ")
        print("                                ")
        print("")
        print("")
        print("")
        sleep(0.3)

        Routes.fireworks(self)

    def lose(self):
        clear()
        delay_print('You have lost all of your sanity, making you go insane, just like how the old Duke was.')
        sleep(0.5)
        delay_print('\nPity... ')
        sleep(0.5)
        delay_print('\nI guess the apple... ')
        sleep(0.5)
        delay_print('doesn\'t fall far from the tree after all.')
        sleep(0.5)
        input(enter)

        Routes.fireworks(self)
#└───────────────────────────────────── Finale ──────────────────────────────────────┘
        
