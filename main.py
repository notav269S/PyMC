import os
import time
import random
import webbrowser

url = 'https://youtu.be/dQw4w9WgXcQ'

clearConsole()

loading("Creating World", 2)

intromsgl = ["Plains", "Taiga", "Jungle", "Snowy Taiga", "Savana"]
intromsg = random.choice(intromsgl)
print("You spawned in a", intromsg)

while True:
    wood = input("Do you want to break wood(y/n)? ").lower().strip()
    if wood == 'n':
        print("DIE")
        webbrowser.open(url)
    elif wood == 'y':
        loading("Breaking Wood", 12)
        while True:
            clearConsole()
            wood = input(
                "You have wood, do you want to make full wood tools(y/n) "
            ).lower().strip()
            clearConsole()
            if wood == 'y':
                while True:
                    explore = input(
                        "Do you want to explore(y/n)? ").lower().strip()
                    if explore == 'n':
                        continue
                    elif explore == 'y':
                        loading("Searching for structures", 3)
                        rnd = randInt(1, 5)
                        if rnd == 5:
                            print("You have found a village")
                        else:
                            print("There is nothing for a mile")
                            explore = input("Do you want to continue(y/n)? "
                                            ).lower().strip()
                            if explore == 'y':
                                continue
                            elif explore == 'n':
                                print("You stopped")
            elif wood == 'n':
                tools = input(
                    "So what wood tools would you like to make(pickaxe, axe, shovel, sword or hoe)? "
                ).lower().strip()
                if tools == 'pickaxe':
                    print("You made a wooden pickaxe. You can mine stone now.")
                    
                elif tools == 'axe':
                    print(
                        "You made a wooden axe. You can mine wood faster now.")
                elif tools == 'shovel':
                    print(
                        "You made a wooden shovel. You can mine dirt faster now."
                    )
                elif tools == 'sword':
                    print(
                        "You made a wooden sword. You have increased strength")
                elif tools == 'hoe':
                    print("no")
                    wait(3)
                    webbrowser.open(url)
                  
            else:
                continue
              

    else:
        continue
