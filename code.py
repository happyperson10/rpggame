import random
# This is to be shared with every character in the game
class Livingthing:
    def __init__(self, first,hitpoints,longattack):
        self.first = first
        self.hitpoints = hitpoints
        self.longattack = longattack

class Human(Livingthing):
    def __init__(self, first, hitpoints,longattack,quickattack,heal):
        super().__init__(first, hitpoints,longattack)
        self.quickattack = quickattack
        self.heal = heal

class Monster(Livingthing):
    def __init__(self, first, hitpoints, longattack,magic):
        super().__init__(first, hitpoints,longattack)
        self.magic = magic
# Name here
while True:
    Playername = input('enter your name here:')
    print(f'so is your name {Playername}?')
    if input('type yes if correct and type no if not:') == 'yes':
        break
# Gender here
while True:
    gender = input('what is your gender:\ntype male or female:')
    if gender == 'male' or 'female':
        break
# Instances of the class here
Human1 = Human(Playername,100,40,20,10)
Human2 = Human('thomas',200,20,10,5)
GenericMonster = Monster('monster', 50, 20,random.randint(0,40))

print('hello my name is thomas\nHAVE YOU SEEN THAT MONSTER')
def battlemode():
    while True:
        """Trying to create the entire battle system of the game in one function"""

        print(f'you are in the battle mode as {Playername}')
        battlemode1 = input('choose quickattack or heal or see stats:')
        if battlemode1 == 'quickattack':
            print( 'you chose quickattack')
            GenericMonster.hitpoints -= Human1.quickattack
            print(f' the monster has been damaged by {GenericMonster.hitpoints}')

        elif GenericMonster.hitpoints == 0:
            break
            return
        elif GenericMonster.hitpoints >= 0:
            break
        elif battlemode1 == 'heal':
            Human1.hitpoints += Human1.heal
            print(f'{Playername} has been healed by {Human1.heal}')

        elif battlemode1 == 'stats':
            statsinput =input(f'if you want to see your stats say me else say you:')
            if statsinput == 'me':
                print(f'{Playername} hitpoints are {Human1.hitpoints}\
 his quickattack is {Human1.quickattack} and his longattack is {Human1.longattack}\
 his heal is {Human1.heal}')
            elif statsinput == 'you':
                pass
# I need help in this i don't know how can it break when the hp gets 0
        elif GenericMonster.hitpoints == 0:
            break
        elif GenericMonster.hitpoints <= 0:
            break
battlemode()
