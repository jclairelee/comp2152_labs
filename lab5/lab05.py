# Import the random library to use for the dice later
import random

# Put all the functions into another file and import them
import functions_lab05

input_invalid = True

# Loop to validate hero's name: ensures exactly two words with alphabetic characters only
while input_invalid:
    hero_name = input("Enter your Hero's name (in two words): ")
    hero_names = hero_name.split()

    if len(hero_names) != 2:
        print("Invalid input - Enter a name with two words")
    elif not hero_names[0].isalpha() or not hero_names[1].isalpha():
        print("Invalid input - Names should contain only letters")
    else:
        input_invalid = False

short_name = hero_names[0][:2] + hero_names[1][:1]
print(short_name)

# Game Setup
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]
belt = []
monster_powers = {"Fire Magic": 2, "Freeze Time": 4, "Super Hearing": 6}
num_stars = 0

# Combat Strength Input
i = 0
input_invalid = True
while input_invalid and i in range(5):
    combat_strength = input("Enter your combat Strength (1-6): ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        print("Invalid input. Enter integer numbers for Combat Strength")
        i += 1
        continue
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength) not in range(1, 7)):
        print("Enter a valid integer between 1 and 6 only")
        i += 1
        continue
    else:
        input_invalid = False
        break

if not input_invalid:
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Roll for weapon
    input("Roll the dice for your weapon (Press Enter)")  # Added prompt
    weapon_roll = random.choice(small_dice_options)
    combat_strength = min(6, (combat_strength + weapon_roll))
    print(f"The hero's weapon is {weapons[weapon_roll - 1]}")

    # Roll for player and monster health points
    health_points = random.choice(big_dice_options)
    m_health_points = random.choice(big_dice_options)
    print(f"Player rolled {health_points} health points")
    print(f"Monster rolled {m_health_points} health points")

    # Collect Loot
    functions_lab05.collect_loot(loot_options, belt)
    functions_lab05.collect_loot(loot_options, belt)

    # Organize Belt
    belt.sort()
    print("Your belt:", belt)

    # Use Loot
    belt, health_points = functions_lab05.use_loot(belt, health_points)

    # Q5: Determine First Attack
    first_attacker = functions_lab05.determine_first_attack()

    # Q6: Inception Dream
    crazy_level = functions_lab05.inception_dream(5)
    health_points -= 1
    combat_strength += crazy_level
    print(f"Your health points are now {health_points}")
    print(f"Your combat strength is now {combat_strength}")

    # Fight Sequence
    print("You meet the monster. FIGHT!!")
    while m_health_points > 0 and health_points > 0:
        if first_attacker == "hero":
            m_health_points = functions_lab05.hero_attacks(combat_strength, m_health_points)
            if m_health_points == 0:
                num_stars = 3
                break
            health_points = functions_lab05.monster_attacks(m_combat_strength, health_points)
        else:
            health_points = functions_lab05.monster_attacks(m_combat_strength, health_points)
            if health_points == 0:
                num_stars = 1
                break
            m_health_points = functions_lab05.hero_attacks(combat_strength, m_health_points)
            if m_health_points == 0:
                num_stars = 3

    if m_health_points > 0 and health_points > 0:
        num_stars = 2

    stars = "*" * num_stars
    print(f"Hero {short_name} gets <{stars}> stars")
