# Kolb & the Dragon

from sys import exit


def start():
    print("""
    Kolb was a brave Nord warrior.
    One day his Chief asked Kolb to slay an evil dragon that threatened
    their village.
    "Go through the mountain pass, Kolb," his Chief said.
    "You will find the Dragon on the other side."
    """)
    print("'Enter' to Continue or 'CTRL+C' to Exit")
    input()

    print("""
    Kolb took his favorite axe and shield and walked to the pass,
    where he found a cold cave, a windy cave, and a narrow trail.
    """)

    choice = input("> ")

    if "cold" in choice:
        cold_cave()
    elif "windy" in choice:
        windy_cave()
    elif "trail" in choice:
        ladder()
    else:
        else_end()


def the_end():
    print("THE END")
    exit(0)


def else_end():
    print("Sorry! Try again!")
    exit(0)


def cold_cave():
    print("""
    Kolb stepped into the frozen cave, but his Nord blood kept him warm.
    A smelly tunnel climbed ahead of him, and wind howled from another
    to his left.
    A ladder was nearby as well.
    """)

    choice = input("> ")

    if "smelly" in choice:
        smelly_tunnel()
    elif "windy" in choice:
        windy_cave()
    elif "ladder" in choice:
        ladder()
    else:
        else_end()


def smelly_tunnel():
    print("""
    Following the stench, Kolb found a flithy orc!
    The orc snarled and charged Kolb with his spiked club.
    """)

    choice = input("Raise shield or swing axe > ")

    if "raise" in choice:
        shield()
    elif "swing" in choice:
        axe()
    else:
        else_end()


def shield():
    print("""
    The orc cackled as his club splintered Kolb's shield and smashed
    into his face. There Kolb died, and the orc had soup from his bones.
    """)
    the_end()


def axe():
    print("""
    Before the orc could strike, Kolb swung his mighty axe.
    The orc's head and club fell uselessly to the floor.
    """)
    hills()

def hills():
    print("""
    Kolb stepped onto a rocky hill. He could see the dragon sleeping below,
    and a tavern off a road nearby.
    """)

    choice = input("Climb down or visit tavern > ")

    if "climb" in choice:
        climb()
    elif "tavern" in choice:
        tavern()
    else:
        else_end()


def climb():
    print("""
    Kolb found the lair where the dragon slept, tendrils of smoke
    wafting from its nostrils. The air made Kolb's eyes sting,
    and he nearly slipped on the bones of men, picked clean.
    The beast lay on its side, the throat and belly both waiting
    targets.
    """)

    choice = input("Strike the neck or belly > ")

    if "neck" in choice:
        neck()
    elif "belly" in choice:
        belly()
    else:
        else_end()


def neck():
    print("""
    The head of the axe lodged itself in the tough, scaly neck
    of the beast. It wailed and thrashed, but Kolb held on and
    eventually sawed through the neck, killing the beast.
    Kolb returned home victorious, and his village was never
    bothered by the dragon again.
    """)
    the_end()


def belly():
    print("""
    Kolb crept towards the belly of the beast, but no sooner
    had he taken his eyes off the head of the beast than it
    snapped him up and ate him whole, axe and all.
    """)
    the_end()


def tavern():
    print("""
    Kolb stopped at the tavern to rest before fighting the dragon.
    High elves ran the tavern, however, and poisoned his meal
    so they could steal his gold.
    """)
    the_end()


def windy_cave():
    print("""
    A strong gust of wind blew Kolb's torch out and knocked him into a pit
    where he split his head and died.
    """)
    the_end()


def ladder():
    print("""
    Climbing up, Kolb found a camp. He met a wise man who shared bread and
    showed two paths to the dragon's lair. One went through the hills, the other
    through a marsh.
    """)

    choice = input("Take the hills or marsh > ")

    if choice == "hills":
        hills()
    elif choice == "marsh":
        marsh()
    else:
        else_end()


def marsh():
    choice = input("Dare to attack or bribe with a gold > ")

    if "attack" in choice:
        print("""
        Kolb swung his axe as hard as he could, but the ghost hardly seemed
        to notice. The ghost drifted into Kolb, and a deep sleep took him
        over, from which he never awoke.
        """)
        the_end()
    elif "gold" in choice:
        gold()
    else:
        else_end()


def gold():
    print("""
    Kolb remembered a story his Gran told him and tossed two gold
    chits for the ghost, and it faded away, allowing him to pass.

    Leaving the marsh behind him, Kolb could see the dragon's lair
    nearby, as well as a small, welcoming tavern.
    """)

    choice = input("Go to Lair or Tavern > ")

    if choice == "lair":
        climb()
    elif choice == "tavern":
        tavern()
    else:
        else_end()


start()
