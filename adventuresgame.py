import time

def introduction():
    print("Welcome to the Epic Adventure Game!")
    time.sleep(1)
    print("You find yourself in a medieval kingdom filled with mysteries.")
    time.sleep(1)
    print("Your quest is to find the legendary Sword of Pythonia.")
    time.sleep(1)
    print("Embark on a journey and make wise choices to succeed!\n")

def choose_path():
    print("Choose your path:")
    print("1. Enter the dark forest")
    print("2. Cross the ancient bridge")
    print("3. Climb the misty mountains")
    return input("Enter your choice (1, 2, or 3): ")

def dark_forest():
    print("You enter the dark forest and hear mysterious sounds.")
    time.sleep(1)
    print("Suddenly, a shadowy figure appears!")
    time.sleep(1)
    
    choice = input("What will you do? (1. Fight, 2. Hide): ")
    if choice == '1':
        print("You draw your sword and engage in a fierce battle.")
        time.sleep(1)
        print("Congratulations! You defeat the shadowy figure.")
        return True
    else:
        print("You choose to hide and observe.")
        time.sleep(1)
        print("The figure passes by without noticing you.")
        return False

def ancient_bridge():
    print("You decide to cross the ancient bridge over a rushing river.")
    time.sleep(1)
    print("As you walk, the bridge begins to creak and sway.")
    time.sleep(1)

    choice = input("What will you do? (1. Continue, 2. Retreat): ")
    if choice == '1':
        print("You carefully continue and successfully cross the bridge.")
        return True
    else:
        print("You decide to retreat and find another path.")
        time.sleep(1)
        print("After some exploration, you discover a hidden cave.")
        return False

def misty_mountains():
    print("You start climbing the misty mountains, surrounded by clouds.")
    time.sleep(1)
    print("The air becomes thinner, and the path more treacherous.")
    time.sleep(1)

    choice = input("What will you do? (1. Keep climbing, 2. Rest): ")
    if choice == '1':
        print("You persevere and reach the summit of the mountains.")
        return True
    else:
        print("You decide to rest and catch your breath.")
        time.sleep(1)
        print("After a short rest, you continue your ascent.")
        return False

def conclusion(success):
    if success:
        print("Congratulations! You have found the legendary Sword of Pythonia!")
    else:
        print("Your journey comes to an end, but the Sword of Pythonia remains hidden.")

if __name__ == "__main__":
    introduction()

    path_choice = choose_path()

    if path_choice == '1':
        success = dark_forest()
    elif path_choice == '2':
        success = ancient_bridge()
    elif path_choice == '3':
        success = misty_mountains()
    else:
        print("Invalid choice. The adventure ends.")

    conclusion(success)
