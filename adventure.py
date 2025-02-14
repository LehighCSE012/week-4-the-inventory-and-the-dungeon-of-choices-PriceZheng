"""Week 4 coding assignment: Price Zheng's Adventure(continue^3).
by implementing an inventory system using lists and incorporating
tuples to represent fixed game elements, Copying code from Week
3 into adventure.py as a starting point.
"""
import random

def acquire_item(inventory, item):
    """Acquire an item and print the message, update to the inventory list"""
    inventory.append(item) # Using append() to add an item to the list
    print(f"You acquired a {item}!")
    return inventory

def display_inventory(inventory):
    """Display the player's current inventory"""
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for i, item in enumerate(inventory,1):
            print(f"{i}. {item}")

def display_player_status(player_health):
    """Prints the player's current health."""
    print(f"Your current health: {player_health}")

def handle_path_choice(player_health):
    """Randomly chooses a path for the player, either "left" or "right"."""
    path = random.choice(["left","right"])
    if path == "left":
        print("You encounter a friendly gnome who heals you for 10 health points.")
        player_health = min(player_health + 10, 100) #Health should not over than 100
    else:
        print("You fall into a pit and lose 15 health points.")
        player_health = max(player_health - 15, 0)
        if player_health == 0:
            print("You are barely alive!")
    return player_health

def player_attack(monster_health):
    """The player inflicts 15 damage to the monster."""
    print("You strike the monster for 15 damage!")
    monster_health = max(monster_health - 15, 0)
    return monster_health

def monster_attack(player_health):
    """Simulates the monster's attack with a chance of critical hit."""
    chance = random.random() #get a random number form 0 to 1
    if chance > 0.5:
        print("The monster hits you for 10 damage!")
        player_health = max(player_health - 10, 0)
    else:
        print( "The monster lands a critical hit for 20 damage!")
        player_health = max(player_health - 20, 0)
    return player_health

def combat_encounter(player_health, monster_health, has_treasure):
    """Manages the combat encounter using a while loop."""
    while player_health > 0 and monster_health > 0:
        monster_health = player_attack(monster_health) #Player attack first
        if monster_health == 0:
            print("You defeated the monster!")
            return has_treasure
        player_health = monster_attack(player_health) #Monster attack
        display_player_status(player_health)
        if player_health == 0:
            print("Game Over!")
            return False
    return False #Make sure all path return the bool

def check_for_treasure(has_treasure):
    """"Check the status of treasure"""
    if has_treasure:
        print("You found the hidden treasure! You win!")
    else:
        print("The monster did not have the treasure. You continue your journey.")

def handle_puzzle(player_health, challenge_outcome):
    """Handles puzzle challenges"""
    print("You encounter a puzzle!")
    choice = input("Do you want to 'solve' or 'skip' the puzzle? ").strip().lower()
    if choice == "solve":
        success = random.choice([True, False])
        if success:
            print(challenge_outcome[0])
            player_health += challenge_outcome[2]
        else:
            print(challenge_outcome[1])
            player_health += challenge_outcome[2]
    
def enter_dungeon(player_health, inventory, dungeon_rooms):
    """Iterates through each room in dungeon_rooms."""
    for room in dungeon_rooms:
        #Tuple unpacking
        room_description, item, challenge_type, challenge_outcome = room
        print(f"{room_description}")

        #Demonstrating tuple is immutability
        try:
            raise TypeError("Tuples are immutable and cannot be modified!")
        except TypeError as e:
            print(f"Error: {e}")

        if item: #acquire update
            print(f"You found a {item} in the room.")
            acquire_item(inventory, item)
            if len(inventory) > 10: #aviod oveflow
                inventory.pop(0) # Using remove() to remove item at the end
            inventory.insert(0, inventory.pop())  # Using insert() to add item at the beginning

        if challenge_type == "puzzle":
            player_health = handle_puzzle(player_health, challenge_outcome)

        elif challenge_type == "trap":
            print("You see a potential trap!")
            choice = input("Do you want to 'disarm' or 'bypass' the puzzle? ").strip().lower()
            if choice == "disarm":
                success = random.choice([True, False])
                if success:
                    print(challenge_outcome[0])
                else:
                    print(challenge_outcome[1])
                    player_health += challenge_outcome[2]
        elif challenge_type == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")

        #Health check
        if player_health < 0:
            player_health = 0
            print("You are barely alive!")

        display_inventory(inventory)

    display_player_status(player_health)
    return player_health, inventory

def main():
    """Initializes game variables and runs the adventure game."""
    player_health = 100
    inventory = [] #String list

    dungeon_rooms = [
        ("A dusty old library", "key", "puzzle", 
         ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
        ("A narrow passage with a creaky floor", None, "trap", 
         ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
        ("A grand hall with a shimmering pool", "healing potion", "none", None),
        ("A small room with a locked chest", "treasure", "puzzle", 
         ("You cracked the code!", "The chest remains stubbornly locked.", -5))
    ]
    monster_health = 55 # Initialize to a hardcoded value
    has_treasure = False #Initialize to False

    has_treasure = random.choice([True, False]) # Randomly assign treasure

    player_health = handle_path_choice(player_health = player_health)

    treasure_obtained_in_combat = combat_encounter(player_health, monster_health, has_treasure)

    check_for_treasure(treasure_obtained_in_combat) # Or has_treasure, depending on logic

    player_health, inventory = enter_dungeon(player_health, inventory, dungeon_rooms)

    print("Game Over.")

if __name__ == "__main__":
    main()
