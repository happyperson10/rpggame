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
Human1 = Human(Playername,100,20,10)
Human2 = Human('thomas',200,10,5)
GenericMonster = Monster('monster', 50, 20,random.randint(0,40))

print('?:hello my name is ...\nIS THAT A MONSTER')
print('you are in the battle mode as',Playername)
def battlemode():
    while True:

        """Trying to create the entire battle system of the game in one function"""
        battlemode1 = input('choose quickattack or heal or see stats:')
        if battlemode1 == 'quickattack':
            print( 'you chose quickattack')
            GenericMonster.hitpoints -= Human1.quickattack
            print(f' the monster has been damaged by {GenericMonster.hitpoints}')
        elif battlemode1 == 'heal':
            Human1.hitpoints += Human1.heal
            print(f'{Playername} has been healed by {Human1.heal}')

        elif battlemode1 == 'stats':
                print(f'{Playername} hitpoints are {Human1.hitpoints}his quickattack is \
{Human1.quickattack} and his is his heal is {Human1.heal}')
        if GenericMonster.hitpoints == 0:
            break
        elif GenericMonster.hitpoints <= 0:
            break
# Now for the enemy
# this doesn't seem to work
        if battlemode1 == 'heal' or 'quickattack':
            enemy = random.choices([20,60,0])
            if enemy == 20:
                Human1.hitpoints -= 20
                print('your hitpoints now are',Human1.hitpoints)
            elif enemy == 60:
                Human1.hitpoints -= 60
                print('you have been hit by quickattack',Human1.hitpoints)
            elif enemy == 0:
                print('you have been hit by magic but failed')

        if Human1.hitpoints== 0:
            print('you died')
            continue
        elif Human1.hitpoints <= 0:
            print('you died')
            continue
battlemode()
print('?:That was so cool my name is thomas welcome to the city')
if input('choose: what happened? /.: ') == 'what happened?':
    print('thomas:seems like you were unconsious and lost memory')
elif input('choose: what happened? /.: ') == '.':
    print('thomas:i see your the quite type anyway seems like you were unconsious and lost memory')

print(Playername,'ok i understand i only remember my name which is',Playername,'\nthomas: anyway\
 can go to to the stadium to fight monsters\n')

