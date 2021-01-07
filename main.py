# main.py
# Midnight Rider
# A text-based adventure game
# Gamespot gives it 9/10.

import sys
import textwrap
import time
import random


INTRODUCTION = """
WELCOME TO MIDNIGHT RIDER

WE'VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.

THAT'S WHY THE GOVERNMENT WANTS IT.

WE CAN'T LET THEM HAVE IT

ONE GOAL: SURVIVAL... and THE CAR
REACH THE END BEFORE THE MAN GONNA GETCHU"""

WIN = """
YOU PRESS THE BUTTON TO OPEN THE GATE. 
THIS ISN'T THE FIRST TIME YOU'VE DONE THIS
YOU CAN TIME IT PERFECTLY SO THAT YOU CAN 
SLIDE THE CAR IN AS THE GATES CLOSE.

YOU KNOW YOU DID THE RIGHT THING.
THE GOVERNMENT WOULD HAVE TORN THE CAR APART
ANALYSING IT, TESTING IT, THEN DESTROYING IT.

THEY DON'T KNOW ITS SECRETS...
THAT IT HOLDS THE KEY TO DIFFERENT WORLDS.

AS YOU STEP OUT THE VEHICLE, FIDO RUNS 
UP TO YOU.
"THANK YOU FOR SAVING ME," HE SAYS.

AS YOU TAKE A COUPLE OF STEPS AWAY FROM THE CAR, 
IT MAKES A STRANGE NOISE

BEFORE YOUR EYES, IT SHIFTS ITS SHAPE YOU'VE SEEN IT BEFORE, BUT ONLY ON TV.

BUMBLEBEE...?"""

CHOICES = """
    ----
    A. DRINK A CHUG JUG
    B. GO AT A MODERATE SPEED
    C. GO FULL THROTTLE
    D. GAS STATION
    E. STATUS CHECK
    Q. QUIT
    ----
"""


def type_text_output(string):
    for char in textwrap.dedent(string):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)


def main():
    # CONSTANTS
    MAX_FUEL_LEVEL = 50
    MAX_DISTANCE_TRAVELED = 100
    MAX_CHUG_JUG = 3

    # Variables
    done = False

    kms_traveled = 0
    agent_distance = -20
    turns = 0
    chug_jug = MAX_CHUG_JUG
    fuel = MAX_FUEL_LEVEL
    thirst = 0

    # MAIN LOOP
    while not done:
        # TODO: RNG
        # NINJA - refills your food (5%)
        if chug_jug < 3 and random.random() < 0.05:
            # Refill chug_jugs
            chug_jug = MAX_CHUG_JUG
            # Player feedback
            print("******** You look at your Chug Jug container.")
            print("******** It is filled magically")
            print("******** \"You're welcome kid.\"")
            print("******** You look around. Ninja?")

        # TODO: Check to see if reached END GAME
        # WIN - Traveled the distance required
        if kms_traveled > MAX_DISTANCE_TRAVELED:
            # Print win scenario
            time.sleep(2)
            type_text_output(WIN)
            # Break
            break

        # TODO: Present the users their choices
        print(CHOICES)

        user_choice = input("What do you want to do?\n").lower().strip(",.!?")
        if user_choice == "a":
            # Drink/Energy
            if chug_jug > 0:
                chug_jug -= 1
                thirst = 0
                print()
                print("-------- That's refreshing.")
                print("-------- Your thirst is sated.")
                print()

            else:
                print()
                print("You're out of Chug Jugs.")
                print()

        elif user_choice == "b":
            # Moderate Speed
            player_distance_now = random.randrange(7, 13)
            agent_distance_now = random.randrange(7, 13)

            # Burn fuel
            fuel -= random.randrange(2, 7)

            # Player distance traveled
            kms_traveled += player_distance_now

            # Agents distance traveled
            agent_distance -= player_distance_now - agent_distance_now

            # Player feedback
            print()
            print("--------- Zoooooom!")
            print(f"-------- You traveled {player_distance_now} kms.")
            print()

        elif user_choice == "c":
            # Fast
            player_distance_now = random.randrange(10, 16)
            agent_distance_now = random.randrange(7, 13)

            # Burn fuel
            fuel -= random.randrange(5, 11)

            # Player distance traveled
            kms_traveled += player_distance_now

            # Agent distance traveled
            agent_distance -= player_distance_now - agent_distance_now

            # Player feedback
            print()
            print("-------- ZOOOOOOOM!")
            print(f"-------- You travelled {player_distance_now} kms.")
            print()

        elif user_choice == "d":
            # Refueling
            # Fill up the fuel tank
            fuel = MAX_FUEL_LEVEL

            # Consider the agents coming closer
            agent_distance += random.randrange(7, 15)

            # Give player feedback
            print("")
            print("----- You filled the fuel tank")
            print("----- The agents got closer...")
            print()

        elif user_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkm travelled: {kms_traveled}.")
            print(f"\tFuel remaining: {fuel} L.")
            print(f"\tAgents are now {abs(agent_distance)} kms behind.")
            print(f"\tYou have {chug_jug} Chug Jugs left.")
            print(f"\tThirst: {thirst}.")
            print(f"\t--------\n")

        elif user_choice == "q":
            done = True

        # Hunger
        if user_choice not in ["a", "e"]:
            thirst += random.randrange(5, 13)

        time.sleep(1.5)




    # Outro
    print("Thanks for playing. Play again soon!")


if __name__ == "__main__":
    main()

