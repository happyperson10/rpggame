import random
# This is to be shared with every character in the game
class Livingthing:
    def __init__(self, first, hitpoints, quickattack):
        self.first = first
        self.hitpoints = hitpoints
        self.quickattack = quickattack

class Human(Livingthing):
    def __init__(self, first, hitpoints,quickattack,heal):
        super().__init__(first, hitpoints,quickattack)
        self.quickattack = quickattack
        self.heal = heal
        self.gender = "evil"

class Monster(Livingthing):
    def __init__(self, first, hitpoints, longattack,magic):
        super().__init__(first, hitpoints,longattack)
        self.magic = magic

# Global Variables
player = Human("Placeholder",100,20,10)
npc1 = Human('Thomas',200,10,5)
monster1 = Monster('monster', 50, 20,random.randint(0,40))

# Name here
def create_character():
    while True:
        playerName = input('\nEnter your name here : ')
        name_confirm = input(random.choice([f"So, is your name {playerName}?", f"{playerName}, is it?",f"Are you sure you want to be called {playerName}?"]) + " [y | N] : ")
        if "y" in name_confirm.lower():
            player.first = playerName
            break
    # Gender here
    while True:
        gender = input('\nChoose your gender : [M | F] : ')
        
        if gender == '':
            continue
        elif 'm' == gender[0].lower():
            player.gender = "Male"
            break
        else:
            player.gender = "Female"
            break

def skilltree(somethinghere):
     if somethinghere == 'skill_tree' or '':
        choice = input('Choose what you want quickattack or heal')
        print('This will lower other stats')
        if "q" in choice.lower():
            confirmation = input("Are you sure you want to increase your Quick Attack by 20 and decrease your heal move by 5? [y|N]")
            if confirmation == '' or "n" in confirmation.lower():
                return
            player.quickattack += 20
            player.heal -= 5
        elif 'h' in choice:
            confirmation = input("Are you sure you want to increase your Heal move by 10 and decrease your Quick Attack by 5? [y|N]")
            if confirmation == '' or "y" in confirmation.lower():
                return
            player.heal += 10
            player.quickattack -=5
        else:
            print("Invalid input!")

def battlemode(player_combatant,enemy_combatant):
    while True:
        """Trying to create the entire battle system of the game in one function"""
        battlemode1 = input('Choose quickattack or heal or stats : [Q | H | S] : ')

        if battlemode1 == '':
            print("\nInvald choice. Please choose a valid option.\n")
            continue
        elif battlemode1 == 'quickattack' or "q" in battlemode1.lower():
            input('\nYou chose quickattack')
            
            enemy_combatant.hitpoints -= player_combatant.quickattack
            if enemy_combatant.hitpoints <= 0:
                input("The monster died".upper()+"\n")
                return "Victory"
            else:
                input(f'You hit the monster! It has {enemy_combatant.hitpoints} HP left!')
        elif battlemode1 == 'heal' or "h" in battlemode1.lower():
            player_combatant.hitpoints += player_combatant.heal
            input(f'{player.name} has been healed by {player.heal}')
        elif battlemode1 == 'stats' or "s" in battlemode1.lower():
                input(f'\n          {player.first}\n\nHealth Points : {player.hitpoints}\nQuick Attack : {player.quickattack} \nHeal : {player.heal}\n')
        
        
        if battlemode1 == 'quickattack' or "q" in battlemode1.lower():
            attacks = [20,60,0]
            enemy = random.choice(attacks)
            if enemy == 20:
                player.hitpoints -= 20
                input(f'The monster hit you back with a light attack! You have {player.hitpoints} left!\n')
            elif enemy == 60:
                player.hitpoints -= 60
                input(f'The monster hit you back with a Heavy attack! You have {player.hitpoints} left!\n')
            elif enemy == 0:
                input('The monster missed the attack! You remain untouched')
        if player.hitpoints <= 0:
            print('You died!')
            return "Death"

if __name__ == "__main__":
    while True:
        create_character()

        print('\nQuick tip: You can open skill tree by saying skill_tree unless you are in battle mode\n')

        input('??? : Hello my nam- LOOK BEHIND YOU! A MONSTER!\n')
        input(f'You are in the battle mode as {player.first.upper()}'.upper()+'\n')

        result_battle = battlemode(player,monster1)

        if result_battle == "Death":
            continue

        input(f'\n??? : That was so cool! you single handedly slayed the monster. My name is {npc1.first}. What\'s your name?')
        input(f'{player.first} : Hello. My name is {player.first}. Nice to meet you.')
        input(f'{npc1.first} : Hi {player.first}. Nice to mee you too! Where are you from?')
        
        choice1 = input('Choose your response : "I don\'t remember" / Leave empty for no reaction : ')
        if choice1 == 'I don\'t remember' or 'what' in choice1.lower():
            print(f'{npc1.first} : Seems like you were unconsious and have lost your memory.')
        elif choice1 == '':
            print(f'{npc1.first} : I see. You\'re the quite type. Anyways, seems like you were unconscious and lost memory')
        skilltree(choice1)
        break
        # Anyway i'm finished it would be mostly reusing stuff here for code
