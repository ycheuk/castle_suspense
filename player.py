import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.sanity = 100
        self.xp = 0
        self.level_bar = None
        self.bar = None
        self.bar_gone = None
        self.alive = True
        self.level_number = 1
    def level_and_sanity(self):
        # This is what shows the sanity and level bar:
        if self.xp >= 100:
            leftover = self.xp - 100
            self.level_number += 1
            self.xp = 0 + leftover
        self.bar = "█" * (int(self.sanity)//10)
        self.bar_gone = "▒" * (10 - len(self.bar))
        self.level_bar = "▒" * ((100 - int(self.xp)) // 10)
        self.level_bar_left = "█" * (10 - len(self.level_bar))
        if self.sanity > 100:
            self.sanity = 100
        print(str("Sanity ♡: "+ self.bar + self.bar_gone + (" ") + str(self.sanity) + str("%") + ("    ") + "Level " + str(self.level_number) + (" ⇧:") + str(self.level_bar_left) + str(self.level_bar) + (" ") + str(self.xp) + ("/100xp") + ("\n─────────────────────────────────────────────────────────")))
    def goDirection(self, direction):
        self.location = self.location.getDestination(direction)
    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.location.removeItem(item)
    def drop(self, item):
        self.items.remove(item)
        item.loc = self.location
        self.location.addItem(item)
    def consume(self, item):
        # This consumes food.
        self.sanity += 20
        self.items.remove(item)
        item.loc = None # Item disappears from the game
    def showInventory(self):
        #clear()
        print("╔══════════════════════════════════════════════════════╗	")
        print("    You are currently carrying:")
        print("    ──────────────────────────")
        for i in self.items:
            print("  ➣",i.name,"-",i.desc)
        print("╚══════════════════════════════════════════════════════╝")
        print()    
