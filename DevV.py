from os import system
from time import sleep
from random import randint, choice

guardDef, witDef, dragDrf = False, False, False

CHEATCODE = 'begodpls'

def clearConsole():
    system('clear')

def wait(dur):
    sleep(dur)

def loading(msg='null', dur=1):
    print(msg)
    wait(1)

def cheat():
    c = input("Cheat in what item(to see the items go to the inventory page)>>> ").lower()
    clearConsole()
    try:
        num = int(input("How Much>>> "))
        inv[c] += num
        invmsg = c[0].upper()+c[1:]
        print(f"Got {num} {invmsg}s.");wait(1)
    except:
        print("That item isn't there in the game try checking the inventory page to see it's closest match."); wait(2); pass

clearConsole()

class Health:
    def __init__(self):
        self.health = 20
        self.saturation = 0
    def getHealth(self):
        return self.health
    def changeHealth(num,self):
        return self.health + num
    def isDead(self):
        if self.health == 0:
            print('Game Over.')
            quit()
    def kill(self):
        print('Game Over.')
        quit()
    def verify(self):
        if self.health > 20:
            self.health = 20
            return False
        elif self.health < 0:
            self.health = 0
            return False
        else:
            return True

health = Health()

biomes = ['Plains','Desert','Taiga','Savana','Birch Forest','Jungle','Snowy Plains','Dark Oak Forest','Swamp','Extreme Hills']

biome = choice(biomes)

global maxed, vilFound, havCraftingTable, havSmithingTable, dimMinable, iroMinable, stoMinable, netMinable, inNether

maxed, vilFound, havCraftingTable, havSmithingTable, dimMinable, iroMinable, stoMinable, netMinable, inNether = False, False, 0, 0, False, False, False, False, False

def invInp():
    print("Invalid Input"); wait(2);pass

class Resource:
    def __init__(self):
        pass
    def wood(self):
        if biome != 'Desert':
            loading("Breaking Wood Nearby", 5)
            inv[f'log'] = inv[f'log']+4
            print(f"You got {inv[f'log']} logs.")
            wait(2)
            clearConsole()
        else: 
            print("You cannot get wood in this biome.")
            wait(2)
            pass
    def gravel(self):   
        if biome != 'Desert' or biome != 'Jungle' or biome != 'Savana':
            loading("Breaking Gravel", 1)
            inv['gravel'] = inv[f'gravel']+1
            print(f"You got {inv[f'gravel']} gravel.")
            wait(2)
            print("Would you like to convert it to flint?")
            fl = input("[Y/N]>>> ").lower()
            if fl == 'y':
                print("Converted")
                wait(2)
                inv['gravel'] -= 1
                inv['flint'] += 1
                clearConsole()
        else: 
            print("You cannot get gravel in this biome.")
            wait(2)
            pass    
    def iron(self):
        if iroMinable:
            loading("Searching for a cave", 5)
            rnum = randint(0,5)
            if rnum == 1:
                print("You found a cave with iron.")
                loading("Mining Iron", 2)
                inv['iron'] = inv['iron']+4
            else:
                print("You didn't find a cave.")
                wait(2)
                pass
        else:
            print("You can't mine iron yet. Get some stone gear.")
            wait(2);pass
    def sand(self):
        if biome == 'Desert':
            loading("Breaking Sand", 1)
            inv['sand'] = inv[f'sand']+1
            print(f"You got {inv[f'sand']} sand.")
            wait(2)
            clearConsole()
        else: 
            print("You cannot get sand in this biome.")
            wait(2)                
            pass
    def diamond(self):
        if dimMinable:
            loading("Searching for a cave", 5)
            rnum = randint(0,20)
            if rnum <= 3:
                print("You found a cave which goes down to diamonds.")
                loading("Mining Diamonds", 10)
                inv['diamond'] = inv['diamond']+2
            else:
                print("You didn't find a cave which leads to diamonds.")
                wait(2)
                pass
        else:
            print("You cannot get diamonds. Get iron gear first.")
            wait(2)
            pass
    def gold(self):
        if dimMinable:
            loading("Searching for a cave", 5)
            rnum = randint(0,20)
            if rnum <= 6:
                print("You found a cave which goes down to gold.")
                loading("Mining Gold", 10)
                inv['gold'] = inv['gold']+2
            else:
                print("You didn't find a cave which leads to gold.")
                wait(2)
                pass
        else:
            print("You cannot mine gold. Get iron gear first.")
            wait(2)
            pass
    def netherite(self):
        if netMinable:
            if inNether:
                loading("Searching for a cave", 5)
                rnum = randint(0,20)
                if rnum <= 3:
                    print("You found a cave which goes down to diamonds.")
                    loading("Mining Ancient Debris", 15)
                    loading('Mining Gold to Get Netherite', 3)
                    inv['netherite'] = inv['netherite']+1
                else:
                    print('No cave found with netherite.')
                    wait(2)
                    pass
            else:
                print("You need to get to the nether first.")
                wait(2)
                pass
        else:
            print("You cannot get netherite. Get diamond gear first.")
            wait(2)
            pass
    def stone(self):
        if stoMinable:
            loading('Mining Stone', 2)
            inv['stone'] = inv['stone']+4
            print(f"Obtained {4} stone")
            wait(1)
        else:
            print("You can't mine stone yet. Make some wood gear first.")
            wait(2)
            pass

class Commands:
    def __init__(self):
        pass
    def resource(self):
        r = Resource()
        thing = input(f"[Wood, Sand, Gravel, Stone, Iron, Gold, Diamond, Netherite]>>> ").lower()
        clearConsole()
        if thing == 'wood':
            r.wood()
        elif thing == 'gravel':
            r.gravel()
        elif thing == 'sand':
            r.sand()
        elif thing == 'iron':
            r.iron()
        elif thing == 'diamond':
            r.diamond()
        elif thing == 'gold':
            r.gold()
        elif thing == 'netherite':
            r.netherite()
        elif thing == 'stone':
            r.stone()
        else:
            invInp()
    def craft(self):
        global maxed, vilFound, havCraftingTable, havSmithingTable, dimMinable, iroMinable, stoMinable, netMinable, inNether
        stoMinable = True
        craft = input(f"[Crafting Table, Smithing Table, Flint and Steel, Wood gear, Stone gear, Iron gear, Diamond gear, Netherite gear, Ender Eyes]>>> ").lower()
        if craft == 'crafting table':
            if inv['log'] >= 1:
                loading("Making A Crafting Table", 1)
                havCraftingTable += 1
                inv['log'] -= 1
                print(f"You have {havCraftingTable} crafting tables.")
            else:
                print('You cannot make a crafting table. You need atleast 1 log')
                wait(2)
                pass
        elif craft == 'wood gear':
            if inv['log'] >= 4 and havCraftingTable > 0:
                loading("Making Wood gear", 2)
                stoMinable = True
                inv['log']-=4
                havCraftingTable -= 1
            else:
                print("You need 4 logs and a crafting table to make wood gear.")
                wait(1)
                pass
        elif craft == 'stone gear':
            if inv['stone'] >= 16 and havCraftingTable > 0:
                loading("Making Stone gear", 5)
                iroMinable = True
                stoMinable = False
                inv['stone']-=16
                havCraftingTable -= 1
            else:
                print("You need 16 stone and a crafting table to make wood gear.")
                wait(1);pass
        elif craft == 'iron gear':
            if inv['iron'] >= 16 and havCraftingTable > 0:
                loading("Making Iron gear", 2)
                iroMinable = False
                dimMinable = True
                inv['iron'] -= 16
                havCraftingTable -= 1
            else:
                print("You need 16 iron and a crafting table to make iron gear.")
                wait(1)
                pass
        elif craft == 'diamond gear':
            if inv['diamond'] >= 16 and havCraftingTable > 0:
                loading("Making Diamond gear", 2)
                netMinable = True
                dimMinable = False
                inv['diamond']-=16
                havCraftingTable -= 1
            else:
                print("You need 16 diamonds and a crafting table to make diamond gear.")
                wait(1);pass
        elif craft == 'netherite gear':
            if inv['netherite'] >= 5 and havSmithingTable > 0:
                loading("Making Netherite gear", 2)
                maxed = True
                havSmithingTable -= 1
                inv['netherite'] -= 5
                print("You have the best gear in the game now")
            else:
                print("You need 5 netherite and a crafting table to make netherite gear.")
                wait(1);pass
        elif craft == 'smithing table':
            if inv['log']>0 and inv['iron']>1 and havCraftingTable>0:
                loading("Crafting Smithing Table", 2)
                havCraftingTable -= 1
                inv['iron'] -= 2
                inv['log'] -= 1
                havSmithingTable +=1
            else:
                print("You need a atleast one crafting table, one log and two iron to make a smithing table.")
                wait(1);pass
        elif craft == 'ender eyes':
            if inv['blazerods']>=7 and inv['enderpearls']>=14 and havCraftingTable>0:
                loading("Crafting Ender Eyes", 2)
                havCraftingTable -= 1
                inv['blazerods'] -= 7
                inv['enderpearls'] -= 14
                inv['endereyes'] += 12
            else:
                print("You need a atleast one crafting table, one log and two iron to make a smithing table.")
                wait(1);pass
        elif craft == 'flint and steel':
            if inv['flint']>0 and inv['iron']>0:
                loading("Crafting Flint and Steel", 2)
                inv['flint'] -= 1
                inv['iron'] -= 1
                inv['flintnsteel'] += 1
        else:
            print("Invalid Input");wait(2);pass

inv = {
    'log':0,
    'gravel':0,
    'emerald':0,
    'diamond':0,
    'iron':0,
    'stone':0,
    'netherite':0,
    'flint':0,
    'flintnsteel':0,
    'blazerods': 0,
    'enderpearls':0,
    'endereyes':0,
    'sand':0,
    'gold':0
}

print("Note: Caps DON'T Matter")
wait(1)

if inNether:
    biome = "Nether Wastes"

cmds = Commands()

while True:
    clearConsole()
    print("Commands:\nR - Gather Resources\nE - Explore\nC - Craft\nI - Check Inventory\nT - Trade\nN - Go To Nether\nA - Advancement List\nF - Fight\nS - Save and Quit\nL - Load Save\n")
    cmd = input(f"[{biome} | CMD]>>> ").lower()
    clearConsole()
    if cmd == 'r':
        cmds.resource()
    elif cmd == 'c':
        craft = input(f"[Crafting Table, Smithing Table, Flint and Steel, Wood gear, Stone gear, Iron gear, Diamond gear, Netherite gear, Ender Eyes]>>> ").lower()
        if craft == 'crafting table':
            if inv['log'] >= 1:
                loading("Making A Crafting Table", 1)
                havCraftingTable += 1
                inv['log'] -= 1
                print(f"You have {havCraftingTable} crafting tables.")
            else:
                print('You cannot make a crafting table. You need atleast 1 log')
                wait(2)
                pass
        elif craft == 'wood gear':
            if inv['log'] >= 4 and havCraftingTable > 0:
                loading("Making Wood gear", 2)
                stoMinable = True
                inv['log']-=4
                woodspeed = 3
                havCraftingTable -= 1
            else:
                print("You need 4 logs and a crafting table to make wood gear.")
                wait(1)
                pass
        elif craft == 'stone gear':
            if inv['stone'] >= 16 and havCraftingTable > 0:
                loading("Making Stone gear", 5)
                iroMinable = True
                stoMinable = False
                inv['stone']-=16
                havCraftingTable -= 1
            else:
                print("You need 16 stone and a crafting table to make wood gear.")
                wait(1);pass
        elif craft == 'iron gear':
            if inv['iron'] >= 16 and havCraftingTable > 0:
                loading("Making Iron gear", 2)
                iroMinable = False
                dimMinable = True
                inv['iron'] -= 16
                havCraftingTable -= 1
            else:
                print("You need 16 iron and a crafting table to make iron gear.")
                wait(1)
                pass
        elif craft == 'diamond gear':
            if inv['diamond'] >= 16 and havCraftingTable > 0:
                loading("Making Diamond gear", 2)
                netMinable = True
                dimMinable = False
                inv['diamond']-=16
                havCraftingTable -= 1
            else:
                print("You need 16 diamonds and a crafting table to make diamond gear.")
                wait(1);pass
        elif craft == 'netherite gear':
            if inv['netherite'] >= 5 and havSmithingTable > 0:
                loading("Making Netherite gear", 2)
                maxed = True
                havSmithingTable -= 1
                inv['netherite'] -= 5
                print("You have the best gear in the game now")
            else:
                print("You need 5 netherite and a crafting table to make netherite gear.")
                wait(1);pass
        elif craft == 'smithing table':
            if inv['log']>0 and inv['iron']>1 and havCraftingTable>0:
                loading("Crafting Smithing Table", 2)
                havCraftingTable -= 1
                inv['iron'] -= 2
                inv['log'] -= 1
                havSmithingTable +=1
            else:
                print("You need a atleast one crafting table, one log and two iron to make a smithing table.")
                wait(1);pass
        elif craft == 'ender eyes':
            if inv['blazerods']>=7 and inv['enderpearls']>=14 and havCraftingTable>0:
                loading("Crafting Ender Eyes", 2)
                havCraftingTable -= 1
                inv['blazerods'] -= 7
                inv['enderpearls'] -= 14
                inv['endereyes'] += 12
            else:
                print("You need a atleast one crafting table, one log and two iron to make a smithing table.")
                wait(1);pass
        elif craft == 'flint and steel':
            if inv['flint']>0 and inv['iron']>0:
                loading("Crafting Flint and Steel", 2)
                inv['flint'] -= 1
                inv['iron'] -= 1
                inv['flintnsteel'] += 1
        else:
            print("Invalid Input");wait(2);pass
    elif cmd == 'n':
        if inNether:
            print("Going to Overworld.")
            wait(1)
            inNether = False
            biome = choice(biomes)
            pass
        else:
            if netMinable and inv['flintnsteel']>0:
                loading("Searching For Lava", 5)
                rnd = randint(1,10)
                if rnd <= 5:
                    print("Found Lava")
                    loading("Making Portal", 3)
                    inNether = True
                    biome = 'Nether Wastes'
                else:
                    print("Didn't Find Lava")
                    wait(1); pass
            else:
                print("You need diamond gear to go to the nether")
                wait(2); pass
    elif cmd == 'e':
        loading("Exploring around", 5) 
        rnum = randint(0, 30)
        if not inNether:
            if rnum < 15:
                print("You found nothing your biome is the same")
                wait(3)
            elif rnum <= 25 and rnum > 15:
                bio = choice(biomes)
                print(f"You found a different biome a {bio}")
                biome = bio
                wait(3)
            else:
                print('You found a village would you like to loot it?')
                loot = input("[Y/N]>>> ").lower()
                if loot == 'y':
                    rin = randint(3,8)
                    print(f"You got {rin} emeralds")
                    inv[f'emerald'] = inv[f'emerald']+rin
                    print("Emeralds can be used to trade with villagers. Would you like to take the coordinates so that you can come back here later?")
                    inp = input("[Y/N]>>> ").lower()
                    if inp == "y":
                        vilFound = True
                    else:
                        pass
        else:
            if rnum > 20:
                print("You found a bastion")
                print("Would you like to trade gold for ender pearls? You will need them for the Ender Dragon.")
                conf = input("[Y/N]>>> ").lower()
                if conf == 'y':
                    if inv['gold']>=14:
                        print("You got 14 ender pearls. You just need blaze rods to convert them into ender eyes.")
                        inv['enderpearls'] += 7*2
                        inv['gold'] -= 14
                    else:
                        print("You don't have enough gold. You need 14."); wait(1)
                        pass
                else:
                    print("You got out of there"); wait(1); pass
            elif rnum > 15 and rnum <= 20:
                print("You found a fortress")
                print("Would you like to kill the blazes? Note: You will die and will have to start over if you don't have diamond gear yet(i.e. Netherite Mining Level).")
                conf = input("[Y/N]>>> ").lower()
                if conf == 'y':
                    if netMinable:
                        print("You got 7 blaze rods. That's enough for the dragon.")
                        inv['blazerods'] += 7
                    else:
                        health.kill()
                else:
                    print("You got out of there"); wait(1); pass
    elif cmd == 't':
        if vilFound:
            print("Villagers will trade you one diamond for 4 emeralds or 16 gravel/sand for 1 emerald.")
            prompt = input("[Get/Give(Emeralds)]>>> ").lower()
            if prompt == "get":
                prompted = input("[Sand/Gravel]>>> ").lower()
                if prompted == 'sand':
                    if inv['sand'] >= 16:
                        print('Added one emerald.')
                        inv['emerald'] = inv['emerald']+1
                        inv['sand'] = inv['sand']-16
                        wait(1)
                    else:
                        print("You cannot buy emeralds as you don't have enough sand.")
                        wait(2)
                        pass
                elif prompted == 'gravel':
                    if inv['gravel'] >= 16:
                        print('Added one emerald.')
                        inv['emerald'] = inv['emerald']+1
                        inv['gravel'] = inv['gravel']-16
                        wait(1)
                    else:
                        print("You cannot buy emeralds as you don't have enough gravel.")
                        wait(2)
                        pass
                else:
                    print("Invalid Input");wait(1);pass
            elif prompt == 'give':
                if inv['emerald']>=4:
                    conf = input("Confirmation[Y/N]>>> ").lower()
                    if conf == 'y':
                        print("Added one diamond")
                        inv['emerald'] -= 4
                        inv["diamond"] += 1
                    elif conf == 'n':
                        print("Not Traded"); wait(1); pass
                    else:
                        pass
            else:
                pass
        else:
            print("You need to find a village first. Use the explore command to do so.")
            wait(2)
            pass
    elif cmd == 'i':
        print(f"Crafting Tables: {havCraftingTable}\nSmithing Tables: {havSmithingTable}\n\nLogs: {inv['log']}\nGravel: {inv['gravel']}\n\nEmeralds: {inv['emerald']}\nDiamonds: {inv['diamond']}\nIron: {inv['iron']}\nStone: {inv['stone']}\nNetherite: {inv['netherite']}\n\nFlint: {inv['flint']}\nFlint and Steel: {inv['flintnsteel']}\nBlaze Rods: {inv['blazerods']}\nEnder Pearls: {inv['enderpearls']}\nEyes of Ender: {inv['endereyes']}\n")
        if stoMinable:
            val = 'Stone'
        elif iroMinable:
            val = 'Iron'
        elif dimMinable:
            val = 'Diamond'
        elif netMinable:
            val = 'Netherite'
        else:
            val = 'Wood'
        print(f"Mining Level: {val}\n")
        if inNether:
            val1 = 'Nether'
        else:
            val1 = 'Overworld'

        print(f"Dimension: {val1}\n")
        conf = input("[Y]>>> ").lower()
        pass
    elif cmd == 'a':
        print("Method 1:\nGet Wood\nMake A Crafting Table\nCraft Wood gear\nGet Stone\nMake Stone gear\nGet Iron\nMake Iron gear\nGet Diamonds\nMake Diamond gear\nGet Flint and Steel\nGo to the Nether\nGet netherite\nMake Smithing Table\nGet Netherite gear\n\nMethod 2:\nFind a Village\nFind More Villages to get Emeralds\nTrade Diamonds from them\nGet Wood for a Crafting Table\nMake Diamond gear\nGet Flint and Steel\nGo to the Nether\nGet Netherite\nMake a Smithing Table\nMake Netherite gear\n")
        conf = input("[Y]>>> ").lower()
        pass
    elif cmd == 'f':
        print("Would you like to fight the Elder Guardian, Wither or the Ender Dragon?")
        boss = input("[G/W/D]>>> ").lower()
        clearConsole()
        if boss == 'g':
            rng = randint(1,10)
            print("Going to a Monument")
            wait(1)
            print("The chances of beating the guardian are based on your gear. Iron gear has certainity of defeating it.")
            wait(1)
            if stoMinable:
                print("The chances of you dying are extremely high. Are you sure you want to pass?")
                conf = input("[Y/N]>>> ").lower()
                if conf == 'y':
                    loading("Fighting The Guardian", 3)
                    if rng <= 1:
                        print("You defeated the guardian!")
                        guardDef = True
                    else:
                        health.kill()
                else:
                    pass
            elif iroMinable:
                print("There is a possibility you will die. Are you sure you want to pass?")
                conf = input("[Y/N]>>> ").lower()
                if conf == 'y':
                    loading("Fighting The Guardian", 3)
                    if rng <= 6:
                        print("You defeated the guardian!")
                        guardDef = True
                    else:
                        health.kill()
                else:
                    pass
            elif dimMinable:
                print("It is certain that you will win. Do you want to pass??")
                conf = input("[Y/N]>>> ").lower()
                if conf == 'y':
                    loading("Fighting The Guardian", 3)
                    print("You defeated the guardian!")
                    guardDef = True
                else:
                    pass
            elif netMinable:
                print("It is certain that you will win. Do you want to pass??")
                conf = input("[Y/N]>>> ").lower()
                if conf == 'y':
                    loading("Fighting The Guardian", 3)
                    print("You defeated the guardian!")
                    guardDef = True
                else:
                    pass 
            else:
                clearConsole()
                print("You need atleast wood gear to attempt to fight a boss.")
                wait(1)

        elif boss == 'w':
            rng = randint(1,10)
            print("Going to the boss")
            wait(1)
            print("The chances of beating the wither are based on your gear. Diamond gear has certainity of defeating it.")
            wait(1)
            clearConsole()
            if stoMinable:
                print("It is certain that you will die. Are you sure you want to attempt it?")
                conf = input("[Y/N]>>> ").lower()
                if conf == 'y':
                    loading("Fighting The Wither", 3)
                    health.kill()
                else:
                    pass
            elif iroMinable:
                print("The chances of you dying are extremely high. Are you sure you want to attempt it?")
                conf = input("[Y/N]>>> ").lower()
                if conf == 'y':
                    loading("Fighting The Wither", 3)
                    if rng <= 4:
                        print("You defeated the wither!")
                        witDef = True
                    else:
                        health.kill()
                else:
                    pass
            elif dimMinable:
                print("There is a possibility that you will die. Do you want to attempt it?")
                conf = input("[Y/N]>>> ").lower()
                if conf == 'y':
                    loading("Fighting The Wither", 3)
                    if rng <= 7:
                        print("You defeated the wither!")
                        witDef = True
                    else:
                        health.kill()
                else:
                    pass
            elif netMinable:
                print("It is certain that you will win. Do you want to attempt it?")
                conf = input("[Y/N]>>> ").lower()
                if conf == 'y':
                    loading("Fighting The Wither", 3)
                    print("You defeated the wither!")
                    witDef = True
                else:
                    pass 
            else:
                clearConsole()
                print("You need atleast wood gear to attempt to fight a boss.")
                wait(1)
        elif boss == 'd':
            if inv['endereyes'] >= 12:
                rng = randint(1,10)
                print("Going to a Fortress to Get Wither Skulls")
                wait(1)
                print("The chances of beating the wither are based on your gear. Diamond gear has certainity of defeating it.")
                if stoMinable:
                    print("It is certain that you will die. Are you sure you want to pass?")
                    conf = input("[Y/N]>>> ").lower()
                    if conf == 'y':
                        loading("Fighting The Dragon", 3)
                        health.kill()
                    else:
                        pass
                elif iroMinable:
                    print("It is certain that you will die. Are you sure you want to pass?")
                    conf = input("[Y/N]>>> ").lower()
                    if conf == 'y':
                        loading("Fighting The Dragon", 3)
                        health.kill()
                    else:
                        pass
                elif dimMinable:
                    print("The chances of you dying are extremely high. Are you sure you want to pass?")
                    conf = input("[Y/N]>>> ").lower()
                    if conf == 'y':
                        loading("Fighting The Dragon", 3)
                        if rng <= 1:
                            print("You defeated the dragon!")
                            dragDef = True
                        else:
                            health.kill()
                    else:
                        pass
                elif netMinable:
                    print("There is a possibility that you will die. Are you sure you want to pass?")
                    conf = input("[Y/N]>>> ").lower()
                    if conf == 'y':
                        loading("Fighting The Dragon", 3)
                        if rng <= 6:
                            print("You defeated the dragon!")
                            dragDef = True
                        else:
                            health.kill()
                    else:
                        pass
                elif maxed:
                    print("There is a possibility that you will die. Are you sure you want to pass?")
                    conf = input("[Y/N]>>> ").lower()
                    if conf == 'y':
                        loading("Fighting The Dragon", 3)
                        if rng <= 8:
                            print("You defeated the dragon!")
                            dragDef = True
                        else:
                            health.kill()
                    else:
                        pass
                else:
                    print("You need atleast wood gear to fight a boss.")
                    wait(1)
            else:
                print("You need atleast 12 ender eyes to fight the dragon.")
                wait(1)
    elif cmd == 's':
        savename = input("[Save Name]>>> ").lower()
        with open(f'{savename}.txt', 'a') as f:
            with open(f'    {savename}.txt', 'w') as j:
                j.write(f"{inv['log']}\n{inv['gravel']}\n{inv['emerald']}\n{inv['diamond']}\n{inv['iron']}\n{inv['stone']}\n{inv['netherite']}\n{inv['flint']}\n{inv['flintnsteel']}\n{inv['blazerods']}\n{inv['enderpearls']}\n{inv['endereyes']}\n{inv['sand']}\n{inv['gold']}\n{biome}\n{maxed}\n{vilFound}\n{havCraftingTable}\n{havSmithingTable}\n{dimMinable}\n{iroMinable}\n{stoMinable}\n{netMinable}\n{inNether}")
    elif cmd == CHEATCODE:
        cheat()
    elif cmd == 'l':
        savename = input("[Save Name]>>> ").lower()
        with open(f'{savename}.txt', 'r') as f:
            content = f.read()
            inv['log'] = content.split('\n')[0]
            inv['gravel'] = content.split('\n')[1]
            inv['emerald'] = content.split('\n')[2]
            inv['diamond'] = content.split('\n')[3]
            inv['iron'] = content.split('\n')[4]
            inv['stone'] = content.split('\n')[5]
            inv['netherite'] = content.split('\n')[6]
            inv['flint'] = content.split('\n')[7]
            inv['flintnsteel'] = content.split('\n')[8]
            inv['blazerods'] = content.split('\n')[9]
            inv['enderpearls'] = content.split('\n')[10]
            inv['endereyes'] = content.split('\n')[11]
            inv['sand'] = content.split('\n')[12]
            inv['gold'] = content.split('\n')[13]
            biome = content.split('\n')[14]
            maxed = content.split('\n')[15]
            vilFound = content.split('\n')[16]
            havCraftingTable = content.split('\n')[17]
            havSmithingTable = content.split('\n')[18]
            dimMinable = content.split('\n')[19]
            iroMinable = content.split('\n')[20]
            stoMinable = content.split('\n')[21]
            netMinable = content.split('\n')[22]
            inNether = content.split('\n')[23]
    else:
        print("Invalid Input");wait(2);pass
