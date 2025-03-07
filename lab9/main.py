import random
import function

# Define two Dice
small_dice_options = list(range(1, 7))  # Max combat strength is 6
big_dice_options = list(range(1, 21))  # Max health points is 20

# Validate input for Hero Combat Strength
input_valid = False
i = 0
while not input_valid and i in range(5):
    try:
        combat_strength = int(input("Enter your combat Strength (1-6): "))
        if combat_strength not in range(1, 7):
            raise ValueError("Enter a valid integer between 1 and 6 only")
        input_valid = True
    except ValueError:
        print("Invalid input. Player needs to enter integer numbers for Combat Strength")
        i += 1

# Validate input for Monster Combat Strength
m_input_valid = False
i = 0
while not m_input_valid and i in range(5):
    try:
        m_combat_strength = int(input("Enter the monster's combat Strength (1-6): "))
        if m_combat_strength not in range(1, 7):
            raise ValueError("Enter a valid integer between 1 and 6 only")
        m_input_valid = True
    except ValueError:
        print("Invalid input. Monster needs to enter integer numbers for Combat Strength")
        i += 1

# If both inputs are valid, continue game
if input_valid and m_input_valid:
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

 # Roll for player health points
input("Roll the dice for your health points (Press enter)")
health_points = random.choice(big_dice_options)  # ✅ Now health_points is defined
print("Player rolled " + str(health_points) + " health points")

# Roll for monster combat strength
input("Roll the dice for the monster's combat strength (Press enter)")
m_combat_strength = random.choice(small_dice_options)
print("Player rolled " + str(m_combat_strength) + " combat strength for the monster")

# Roll for monster health points
input("Roll the dice for the monster's health points (Press enter)")
m_health_points = random.choice(big_dice_options)
print("Player rolled " + str(m_health_points) + " health points for the monster")
# Lab 9: Question 2 - Handling `monster_attacks()` exception
try:
    health_points = function.monster_attacks(m_combat_strength, health_points)
except TypeError:
    print("A TypeError occurred")

# Loop while both the player and monster are alive
while m_health_points > 0 and health_points > 0:
    input("Roll to see who attacks first (Press Enter)")
    attack_roll = random.choice(small_dice_options)

    if attack_roll % 2 != 0:
        input("You strike (Press enter)")
        m_health_points = function.hero_attacks(combat_strength, m_health_points)
        if m_health_points > 0:
            input("The monster strikes (Press enter)!!!")
            health_points = function.monster_attacks(m_combat_strength, health_points)
    else:
        input("The Monster strikes (Press enter)")
        health_points = function.monster_attacks(m_combat_strength, health_points)
        if health_points > 0:
            input("The hero strikes!! (Press enter)")
            m_health_points = function.hero_attacks(combat_strength, m_health_points)
