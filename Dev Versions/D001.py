from os import system
from time import sleep
from random import randint, choice

def clearConsole():
    system('clear')

def wait(dur):
    sleep(dur)

def loading(msg='null', dur=1, speed=0.5):
    if msg == 'null':
        clearConsole()
        print("No message specified.")
        wait(2)
        clearConsole()
    else:
        for i in range(0, dur*2):
            i = i
            clearConsole()
            print(f"{msg}.")
            wait(speed/3)
            clearConsole()
            print(f"{msg}..")
            wait(speed/3)
            clearConsole()
            print(f"{msg}...")
            wait(speed/3)
            clearConsole()

clearConsole()

biomes = ['Plains','Desert','Taiga','Savana','Birch Forest','Jungle','Snowy Plains','Dark Oak Forest','Swamp','Extreme Hills']

biome = choice(biomes)

maxed = False

stoSpeed = 5

vilFound = False

havCraftingTable = 0
havSmithingTable = 0

dimMinable = False
ironMinable = False
stoMinable = False
netMinable = False
inNether = False

woodtype = ''

inv = {
    'log':8,
    'gravel':0,
    'emerald':0,
    'diamond':16,
    'iron':16,
    'stone':16,
    'netherite':0,
    'flint':0,
    'flintnsteel':1
}

woodspeed = 5
sandspeed = 1

print("Note: Caps DON'T Matter")
wait(0.5)

while True:
    clearConsole()
    print("Commands:\nR - Gather Resources\nE - Explore\nC - Craft\nI - Check Inventory\nT - Trade\nN - Go To Nether\nA - Advancement List\n")
    cmd = input(f"[{biome} | CMD]>>> ").lower()
    clearConsole()
    if cmd == 'r':
        thing = input(f"[Wood, Sand, Gravel, Stone, Iron, Diamond, Netherite]>>> ").lower()
        clearConsole()
        if thing == 'wood':
            if biome != 'Desert':
                loading("Breaking Wood Nearby", woodspeed)
                inv[f'log'] = inv[f'log']+4
                print(f"You got {inv[f'log']} logs.")
                wait(2)
                clearConsole()
            else: 
                print("You cannot get wood in this biome.")
                wait(2)
                continue
        elif thing == 'gravel':
            if biome != 'Desert' or biome != 'Jungle' or biome != 'Savana':
                loading("Breaking Gravel", sandspeed)
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
                continue
        elif thing == 'iron':
            if ironMinable:
                loading("Searching for a cave", 5)
                rnum = randint(0,5)
                if rnum == 1:
                    print("You found a cave with iron.")
                    loading("Mining Iron", 2)
                    inv['iron'] = inv['iron']+4
                else:
                    print("You didn't find a cave.")
                    wait(2)
                    continue
            else:
                print("You can't mine iron yet. Get some stone tools.")
                wait(2)
                continue
        elif thing == 'diamond':
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
                    continue
            else:
                print("You cannot get diamonds. Get iron tools first.")
                wait(2)
                continue
        elif thing == 'netherite':
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
                        continue
                else:
                    print("You need to get to the nether first.")
                    wait(2)
                    continue
            else:
                print("You cannot get netherite. Get diamond tools first.")
                wait(2)
                continue
        elif thing == 'stone':
            if stoMinable:
                loading('Mining Stone', 2)
                inv['stone'] = inv['stone']+4
            else:
                print("You can't mine stone yet. Make some wood tools first.")
                wait(2)
                continue
        else:
            print("Invalid Input"); wait(2);continue
    elif cmd == 'c':
        craft = input(f"[Crafting Table, Smithing Table, Flint and Steel, Wood Tools, Stone Tools, Iron Tools, Diamond Tools, Netherite Tools]>>> ").lower()
        if craft == 'crafting table':
            if inv['log'] >= 1:
                loading("Making A Crafting Table", 1)
                havCraftingTable += 1
                inv['log'] -= 1
            else:
                print('You cannot make a crafting table. You need atleast 1 log')
                wait(2)
                continue
        elif craft == 'wood tools':
            if inv['log'] >= 4 and havCraftingTable > 0:
                loading("Making A Wood Tools", 2)
                stoMinable = True
                inv['log']-=4
                woodspeed = 3
                havCraftingTable -= 1
            else:
                print("You need 4 logs and a crafting table to make wood tools.")
                wait(2)
                continue
        elif craft == 'stone tools':
            if inv['stone'] >= 16 and havCraftingTable > 0:
                loading("Making Stone Tools", stoSpeed)
                ironMinable = True
                stoMinable = False
                inv['stone']-=16
                havCraftingTable -= 1
            else:
                print("You need 16 stone and a crafting table to make wood tools.")
        elif craft == 'iron tools':
            if inv['iron'] >= 16 and havCraftingTable > 0:
                loading("Making Iron Tools", 2)
                iroMinable = False
                dimMinable = True
                inv['iron'] -= 16
                havCraftingTable -= 1
            else:
                print("You need 16 iron and a crafting table to make iron tools.")
                wait(1)
                continue
        elif craft == 'diamond tools':
            if inv['diamond'] >= 16 and havCraftingTable > 0:
                loading("Making Diamond Tools", 2)
                netMinable = True
                dimMinable = False
                inv['diamond']-=16
                havCraftingTable -= 1
            else:
                print("You need 16 diamonds and a crafting table to make diamond tools.")
        elif craft == 'netherite tools':
            if inv['netherite'] >= 5 and havSmithingTable > 0:
                loading("Making Netherite Tools", 2)
                maxed = True
                havSmithingTable -= 1
                inv['netherite'] -= 5
                print("You have maxed your player. You have beaten the game.")
                quit()
            else:
                print("You need 5 netherite and a crafting table to make netherite tools.")
        elif craft == 'smithing table':
            if inv['log']>0 and inv['iron']>1 and havCraftingTable>0:
                loading("Crafting Smithing Table", 2)
                havCraftingTable -= 1
                havSmithingTable +=1
            else:
                print("You need a atleast one crafting table, one log and two iron to make a smithing table.")
        elif craft == 'flint and steel':
            if inv['flint']>0 and inv['iron']>0:
                loading("Crafting Flint and Steel", 2)
                inv['flint'] -= 1
                inv['iron'] -= 1
                inv['flintnsteel'] += 1
        else:
            print("Invalid Input");wait(2);continue
    elif cmd == 'n':
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
                wait(1); continue
        else:
            print("You need diamond tools to go to the nether")
            wait(2); continue
    elif cmd == 'e':
        loading("Exploring around", 5) 
        rnum = randint(0, 30)
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
                    continue
    elif cmd == 't':
        if vilFound:
            print("Villagers will trade you one diamond for 4 emeralds.")
            prompt = input("[Y/N]>>> ").lower()
            if prompt == "y":
                if inv['emerald'] > 4:
                    print('Added one diamond')
                    inv['diamond'] = inv['diamond']+1
                    inv['emerald'] = inv['emerald']-4
                else:
                    print("You cannot buy diamonds as you don't have enough emeralds.")
                    wait(2)
                    continue
            else:
                continue
        else:
            print("You need to find a village first. Use the explore command to do so.")
            wait(2)
            continue
    elif cmd == 'i':
        print(f"Crafting Tables: {havCraftingTable}\nSmithing Tables: {havSmithingTable}\n\nLxogs: {inv['log']}\nGravel: {inv['gravel']}\n\nEmeralds: {inv['emerald']}\nDiamonds: {inv['diamond']}\nIron: {inv['iron']}\nStone: {inv['stone']}\nNetherite: {inv['netherite']}\n\nFlint: {inv['flint']}\nFlint and Steel: {inv['flintnsteel']}\n")
        if stoMinable:
            val = 'Stone'
        elif ironMinable:
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

        print(f"Dimension: {val1}")
        conf = input("[Y]>>> ").lower()
        continue
    elif cmd == 'a':
        print("Method 1:\nGet Wood\nMake A Crafting Table\nCraft Wood Tools\nGet Stone\nMake Stone Tools\nGet Iron\nMake Iron Tools\nGet Diamonds\nMake Diamond Tools\nGet Flint and Steel\nGo to the Nether\nGet netherite\nMake Smithing Table\nGet Netherite Tools\n\nMethod 2:\nFind a Village\nFind More Villages to get Emeralds\nTrade Diamonds from them\nGet Wood for a Crafting Table\nMake Diamond Tools\nGet Flint and Steel\nGo to the Nether\nGet Netherite\nMake a Smithing Table\nMake Netherite Tools\n")
        conf = input("[Y]>>> ").lower()
        continue
    else:
        print("Invalid Input");wait(2);continue
