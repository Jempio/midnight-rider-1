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

LOSE_THIRST = """
YOU DECIDED NOT TO DRINK A CHUG JUG AND COULD NO LONG FOCUS ON DRIVING.
~CRASH~
YOU HIT A LAMP POST.
EVERYTHING AROUND YOU SLOWLY DARKENS.
YOU BEGIN TO FEEL COLD.
THIS IS THE END.
THERE'S A FAINT WHISPERING.
YOU SLOWLY FADE AWAY AS YOU HEAR NINJA WHISPER TO YOU.
"GET GOOD KID."
"""

LOSE_AGENTS = """
THE AGENTS HAVE CLOSED IN ON YOU.
THERE ARE AT LEAST 20 CARS SURROUNDING YOU.
THE LEAD CAR BUMPS YOUR PASSENGER SIDE
YOU MANAGE TO CORRECT YOUR STEERING
TO KEEP YOU FROM CRASHING

YOU DIDN'T SEE THE AGENTS CAR BESIDE YOU.
THE DRIVER BUMPS YOUR CAR.
AND THAT'S IT.

YOU SPIN UNCONTROLLABLY
THE CAR FLIPS OVER AT LEAST TWO TIMES.
OR MORE.... YOU SEEM TO HAVE LOST COUNT.

SIRENS.

"ARE THEY ALIVE?" THEY SAY AS YOU HEAR
FOOTSTEPS GETTING CLOSER.
"DOESN'T MATTER, ALL WE WANTED WAS THE CAR.

YOU SEE NINJA SLOWLY STEP OUT OF THE OVERTURNED CAR.

"YOU SHOULD'VE PLAYED QUEUED UP WITH A SQUAD"

HE WAS IN THE CAR THE WHOLE TIME

YOU DRIFT OFF INTO UNCONSCIOUSNESS."""

LOSE_FUEL = """
YOUR CAR SPUTTERS AND SEEMS TO LET OUT
A BIG SIGH. THERE'S NO MORE FUEL LEFT.

THE COPS SURROUND YOU AND THEY STEP 
OUT OF THEIR CARS. NINJA RIPS THE 
DOOR OPEN AND THROWS YOU OUT
OF THE CAR.

"MY CAR NOW"

YOU FAILED...
"""

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
    MAX_THIRST = 50
    STARTING_AGENTS_DISTANCE = -20

    # Variables
    done = False

    kms_traveled = 0
    agent_distance = STARTING_AGENTS_DISTANCE
    turns = 0
    chug_jug = MAX_CHUG_JUG
    fuel = MAX_FUEL_LEVEL
    thirst = 0

    # MAIN LOOP
    while not done:
        # NINJA - refills your food (5%)
        if chug_jug < 3 and random.random() < 0.05:
            # Refill chug_jugs
            chug_jug = MAX_CHUG_JUG
            # Player feedback
            print("******** You look at your Chug Jug container.")
            print("******** It is filled magically")
            print("******** \"You're welcome kid.\"")
            print("******** You look around. Ninja?")

        # WIN - Traveled the distance required
        if kms_traveled > MAX_DISTANCE_TRAVELED:
            # Print win scenario
            time.sleep(1.5)
            type_text_output(WIN)
            # Break
            break

        # LOSE - by thirst
        elif thirst > MAX_THIRST:
            time.sleep(1.5)
            type_text_output(LOSE_THIRST)
            break

        # LOSE - agents reached you
        elif agent_distance >= 0:
            time.sleep(1.5)
            type_text_output(LOSE_AGENTS)
            break

        # LOSE - fuel ran out
        elif fuel <= 0:
            time.sleep(1.5)
            type_text_output(LOSE_FUEL)
            break

        # Display Thirst
        if thirst > 40:
            print("******** Your throat is as dry as your texting ability. Drink a chug jug man.")
            time.sleep(1)
        elif thirst > 25:
            print("******** You're getting a little thirsty might wanna get a little something to sip on.")
            time.sleep(1)

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
            player_distance_now = random.randrange(4, 12)
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

        else:
            print("\tPLease choose a valid choice")

        # UPKEEP
        if user_choice in ["b", "c", "d"]:
            thirst += random.randrange(8, 18)
            turns += 1

        time.sleep(1.5)

    # Outro
    print()
    print("\nThanks for playing. Play again soon!")
    print(f"You finished the game in {turns} turns.")


if __name__ == "__main__":
    main()

