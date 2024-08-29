import random

health = 100

def dice_roll():
    number_rolled = random.randrange(1,7)
    print(number_rolled)

def add_health(number1):
    global health
    if (health < (100 - number1)):
        health = health + number1
        print("Your health is " + str(health) + ".")
    else: 
        print("Your health is already maxed out! Get back to it.")


player_name = input("\nHello, welcome to the Upside Down. Just kidding. What is your name?\n")

print(("\nHi " + player_name + "."))

ready_to_play_answer = (input("\nAre you ready to play?\n"))

# redo this section to using a list of valid responses and the in operator
if (ready_to_play_answer == "Yes") or (ready_to_play_answer == "yes") or (ready_to_play_answer == "ok") or (ready_to_play_answer == "Ok") or (ready_to_play_answer == "ya") or (ready_to_play_answer == "sure") or (ready_to_play_answer == "Ya") or (ready_to_play_answer == "Sure"):
    print("Let's go then!\n")
    print("You are an explorer traveling through the jungle searching for a lost city.\n\nYou are starting with 100 health, and the lost city is approximately 200 steps away according to your scout.\n\nYou might make it, but you have to dodge dangerous creatures and killer plants.\n\nGood luck!\n")
else:
    print("\nWell, come back when you are ready.\n") 
    exit()

special_weapon = "dagger"

player_has_special_weapon = False

print("Before you begin you have a chance to gain possession of a special weapon!\n")
special_weapon_int_selection = input("Pick a number between 1 and 10.\n")


if int(special_weapon_int_selection) % 2 == 0:
    player_has_special_weapon = True
    print("You have been give a dagger for your journey. This is a special weapon, keep it safe.")
else:
    print("Hmmm, that was an unlucky number. You'll have to do without any extras.")