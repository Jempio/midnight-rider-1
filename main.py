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

CHOICES = """
    ----
    B. GO AT A MODERATE SPEED
    C. GO FULL THROTTLE
    D. GAS STATION
    E. STATUS CHECK
    Q. QUIT
    ----
"""
def intro():
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)


def main():
    # intro()

    # CONSTANTS
    MAX_FUEL_LEVEL = 50

    # Variables
    done = False

    kms_traveled = 0       # 100km is the end
    agent_distance = -20    # 0km is the end
    turns = 0
    tofu = 3                # 3 is max
    fuel = MAX_FUEL_LEVEL
    hunger = 0

    # MAIN LOOP
    while not done:
        # TODO: Check to see if reached END GAME

        # TODO: Present the users their choices
        print(CHOICES)

        user_choice = input("What do you want to do?\n").lower().strip(",.!?")
        if user_choice == "b":
            # Moderate Speed
            player_distance_now = random.randrange(8, 13)
            agent_distance_now = random.randrange(6, 11)

            # Burn fuel
            fuel -= random.randrange(3, 8)

            # Player distance traveled
            kms_traveled += player_distance_now

            # Agents distance traveled
            agent_distance -= player_distance_now - agent_distance_now

            # Player feedback
            print()
            print("Zoooooom!")
            print(f"-------- You travelled {player_distance_now} kms.")
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
            print("ZOOOOOOOM!")
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
            print(f"\tYou have {tofu} tofus left.")
            print(f"\t--------\n")

        elif user_choice == "q":
            done = True

        time.sleep(1.5)

        # TODO: Change the environment based on user choice and RNG

        # TODO: Random event generator

    # Outro
    print("Thanks for playing. Play again soon!")

if __name__ == "__main__":
    main()

