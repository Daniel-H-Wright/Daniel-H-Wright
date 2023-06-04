import random
import time
import Villains
import math
import Areas
import colorama
from colorama import Fore
import Text
import Items

t = 0.5 # time taken for text to move
name = (input("Name: "))
print(Fore.LIGHTYELLOW_EX + "Welcome " + name.title() + ", you find yourself in a great jungle, the trees are higher than the "
                                                      "eye can see.")
time.sleep(t)
print(Fore.LIGHTYELLOW_EX + 'The jungle is humid, but with a pleasant breeze. You can hear low ominous sounds around this bizarre'
                          ' area.')
time.sleep(t)
print(Fore.LIGHTYELLOW_EX + 'It may be a good idea to move.')
time.sleep(t)
print(Fore.LIGHTBLACK_EX + '#If you wish for a hint, enter "hint"')
x = 0
y = 0
Stats_hp = random.randint(1, 15) * 1000
Stats_atk = random.randint(1, 10) * 1000
Stats_dfn = random.randint(1, 10)
Stats_spd = (random.randint(1, 1000)) / 1000
Stats_mgc = random.randint(1, 10)
Stats_kg = random.randint(50, 85)

data_logic = False
import lazy_import
t_hp = Stats_hp

lck = 0

damage = 0
distance = 0
direction = 0
t = 0.5 #time for running through text
while abs(float(x)) < 100 and abs(float(y)) < 100:
    while data_logic is not True:
        action = (input(Fore.RED + "Action: "))
        if action.lower() == "move":
            data_logic = True
        elif action.lower() == 'hint':
            print(Fore.LIGHTBLACK_EX + 'enter "move"')
            data_logic = False
        else:
            print(Fore.RED + 'Invalid Action')
    data_logic = False

    while data_logic is not True:
        distance = (input(Fore.RED + "Distance: "))
        if float(distance) >= 101 or float(distance) <= 0:
            print(Fore.RED + 'Invalid Distance')
        elif float(distance) > 0:
            data_logic = True
        else:
            data_logic = False
    data_logic = False

    while data_logic is not True:
        direction = input(Fore.RED + 'N, E, S, W: ')
        if direction.lower() == "n":
            y = y + float(distance)
            data_logic = True
        elif direction.lower() == "e":
            x = x + float(distance)
            data_logic = True
        elif direction.lower() == "s":
            y = y + float(distance) * -1
            data_logic = True
        elif direction.lower() == "w":
            x = x + float(distance) * -1
            data_logic = True
        else:
            print(Fore.RED + "Invalid")
            action = (input("Action: "))
            data_logic = False
    data_logic = False

    while data_logic is not True:
        speed = (input(Fore.RED + "Speed(km/h): "))
        if float(speed) >= 12 or float(speed) <= 0:
            print(Fore.RED + 'Invalid Speed')
        elif float(speed) > 0:
            data_logic = True
        else:
            data_logic = False
    data_logic = False

    assault = (float(distance) // 5) * float(speed)  # Moving Calculation

    if float(assault) >= 10:
        if random.randint(1, 10) > 1:

            print(Fore.LIGHTYELLOW_EX + "You have been attacked by " + Villains.enemy)  # Enemy Attacks
            while Stats_hp > 0 and Villains.hp > 0:
                action = input(Fore.RED + "Action: ")
                if action.lower() == 'fight':
                    if Stats_spd * random.randint(1, Stats_kg) > Villains.spd * random.randint(1, Villains.kg):

                        print(Fore.MAGENTA + 'They attacked first!')
                        lck = 10 / random.randint(1, 100)
                        time.sleep(1)
                        if Stats_dfn > Villains.atk * lck:
                            damage = 0
                        else:
                            damage = math.ceil(Villains.atk * lck - Stats_dfn)
                        print(Fore.LIGHTYELLOW_EX + 'Damage: ' + str(damage))
                        time.sleep(1)
                        t_hp = t_hp - abs(int(damage))
                        if t_hp <= 0:
                            t_hp = 0
                            print(Fore.LIGHTYELLOW_EX + 'Defeat!')
                            time.sleep(1)
                            exit()
                        else:
                            print(Fore.LIGHTBLUE_EX + 'HP: ' + str(int(t_hp)))
                            time.sleep(1)

                        print(Fore.LIGHTBLUE_EX + 'You now attack!')
                        lck = 10 / random.randint(1, 100)
                        time.sleep(1)
                        if Villains.dfn > Stats_atk * lck:
                            damage = 0
                        else:
                            damage = math.ceil(Stats_atk * lck - Villains.dfn)
                        print(Fore.LIGHTYELLOW_EX + 'Damage: ' + str(damage))
                        time.sleep(1)
                        Villains.hp = Villains.hp - abs(int(damage))
                        if Villains.hp <= 0:
                            Villains.hp = 0
                            print(Fore.LIGHTYELLOW_EX + 'Victory!')
                            time.sleep(1)
                            if random.randint(1, 100) > 1:
                                print(Fore.LIGHTYELLOW_EX + 'You obtained ' + Items.item)
                                Stats_hp += Items.hp
                                Stats_atk += Items.atk
                                Stats_dfn += Items.dfn
                                Stats_spd += Items.spd
                                Stats_mgc += Items.mgc
                                Stats_kg += Items.kg
                                time.sleep(2)
                                print(Fore.LIGHTBLUE_EX + 'HP: ' + str(Stats_hp) + Fore.LIGHTGREEN_EX + '  (+' + str(
                                    Items.hp) + ')')
                                time.sleep(0.2)
                                print(Fore.LIGHTBLUE_EX + 'attack: ' + str(Stats_atk) + Fore.LIGHTGREEN_EX + '  (+' + str(
                                    Items.atk) + ')')
                                time.sleep(0.2)
                                print(Fore.LIGHTBLUE_EX + 'defence: ' + str(Stats_dfn) + Fore.LIGHTGREEN_EX + '  (+' + str(
                                    Items.dfn) + ')')
                                time.sleep(0.2)
                                print(Fore.LIGHTBLUE_EX + 'speed: ' + str(Stats_spd) + Fore.LIGHTGREEN_EX + '  (+' + str(
                                    Items.spd) + ')')
                                time.sleep(0.2)
                                print(Fore.LIGHTBLUE_EX + 'magic: ' + str(Stats_mgc) + Fore.LIGHTGREEN_EX + '  (+' + str(
                                    Items.mgc) + ')')
                                time.sleep(0.2)
                                print(
                                    Fore.LIGHTBLUE_EX + 'weight: ' + str(Stats_kg) + Fore.RED + '  (+' + str(Items.kg) + ')')
                                time.sleep(1)
                        else:
                            print(Fore.MAGENTA + 'Enemy HP: ' + str(int(Villains.hp)))

                    else:
                        print(Fore.LIGHTBLUE_EX + 'You attacked first!')  # You Attack
                        lck = 10 / random.randint(1, 100)
                        time.sleep(1)
                        if Villains.dfn > Stats_atk * lck:
                            damage = 0
                        else:
                            damage = math.ceil(Stats_atk * lck - Villains.dfn)
                        print(Fore.LIGHTYELLOW_EX + 'Damage: ' + str(damage))
                        time.sleep(1)
                        Villains.hp = Villains.hp - abs(int(damage))
                        if Villains.hp <= 0:
                            Villains.hp = 0
                            print(Fore.LIGHTYELLOW_EX + 'Victory!')
                            if random.randint(1, 100) > 70:
                                print(Fore.LIGHTYELLOW_EX + 'You obtained ' + Items.item)
                                hp += Items.hp
                                atk += Items.atk
                                dfn += Items.dfn
                                spd += Items.spd
                                mgc += Items.mgc
                                kg += Items.kg
                                time.sleep(2)
                                print(Fore.LIGHTBLUE_EX + 'HP: ' + str(Stats.hp) + Fore.LIGHTGREEN_EX + '  (+' + str(
                                    Items.hp) + ')')
                                time.sleep(0.2)
                                print(Fore.LIGHTBLUE_EX + 'attack: ' + str(Stats.atk) + Fore.LIGHTGREEN_EX + '  (+' + str(
                                    Items.atk) + ')')
                                time.sleep(0.2)
                                print(Fore.LIGHTBLUE_EX + 'defence: ' + str(Stats.dfn) + Fore.LIGHTGREEN_EX + '  (+' + str(
                                    Items.dfn) + ')')
                                time.sleep(0.2)
                                print(Fore.LIGHTBLUE_EX + 'speed: ' + str(Stats.spd) + Fore.LIGHTGREEN_EX + '  (+' + str(
                                    Items.spd) + ')')
                                time.sleep(0.2)
                                print(Fore.LIGHTBLUE_EX + 'magic: ' + str(Stats.mgc) + Fore.LIGHTGREEN_EX + '  (+' + str(
                                    Items.mgc) + ')')
                                time.sleep(0.2)
                                print(
                                    Fore.LIGHTBLUE_EX + 'weight: ' + str(Stats.kg) + Fore.RED + '  (+' + str(Items.kg) + ')')
                                time.sleep(1)
                        else:
                            print(Fore.MAGENTA + 'Enemy HP: ' + str(int(Villains.hp)))
                            time.sleep(1)

                        print(Fore.MAGENTA + Villains.enemy + ' now attacks you!')
                        lck = 10 / random.randint(1, 100)
                        time.sleep(1)
                        if Stats_dfn > Villains.atk * lck:
                            damage = 0
                        else:
                            damage = math.ceil(Villains.atk * lck - Stats_dfn)
                        print(Fore.LIGHTYELLOW_EX + 'Damage: ' + str(damage))
                        time.sleep(1)
                        t_hp = t_hp - abs(int(damage))
                        if t_hp <= 0:
                            t_hp = 0
                            print(Fore.LIGHTYELLOW_EX + 'Defeat!')
                            time.sleep(1)
                            exit()
                        else:
                            print(Fore.LIGHTBLUE_EX + 'HP: ' + str(int(t_hp)))
                    time.sleep(1)

                elif action.lower() == 'override':
                    Villains.hp = -1
                    time.sleep(1)

                elif action.lower() == 'hint':
                    print(Fore.LIGHTBLACK_EX + 'enter "escape" or "fight"')

                elif action.lower() == 'escape':
                    lck = 10 / random.randint(1, 100)
                    if Stats_spd * lck > Villains.spd:
                        Villains.hp = -1
                        print(Fore.LIGHTYELLOW_EX + "You escaped!")
                        time.sleep(1)
                    else:
                        t_hp = t_hp - 5
                        print(Fore.LIGHTYELLOW_EX + "You failed to escaped!")
                        time.sleep(0.5)
                        print(Fore.LIGHTBLUE_EX + 'HP: ' + str(int(t_hp)))
                        time.sleep(1)

            else:
                print(Fore.LIGHTYELLOW_EX + "You are okay.")
                time.sleep(1)
    else:
        print(Fore.LIGHTYELLOW_EX + "You are okay.")
        time.sleep(1)
time.sleep(1)
print(
    Fore.LIGHTYELLOW_EX + 'You have reached a civilisation outside of the Jungle. Well done ' + name.title() + ', now observe: this place is called ' + Areas.name + '.')
time.sleep(1)

while data_logic is not True:
    action = (input(Fore.RED + "Action: "))
    if action.lower() == 'explore':
        print(Fore.LIGHTYELLOW_EX + 'You walk around')
        time.sleep(1)
        print(Fore.LIGHTYELLOW_EX + "Your observation is this: it's" + Areas.tag)
        time.sleep(1)
        data_logic = False
    elif action.lower() == 'talk':
        if Areas.ppl / random.randint(1, 10 ** 4) > 10:
            print(Fore.LIGHTYELLOW_EX + 'You find someone and begin talking to them.')
            time.sleep(1)
            if Areas.safety * (random.randint(1, 100) / 100) > 20:
                print(Fore.LIGHTYELLOW_EX + 'They say: ' + Text.speech)
            else:
                print(Fore.LIGHTYELLOW_EX + 'You get stabbed.')
            time.sleep(1)
            data_logic = False
        else:
            print(Fore.LIGHTYELLOW_EX + 'There is nobody near you to talk to.')
            time.sleep(1)
        data_logic = False
    elif action.lower() == 'hint':
        print(Fore.LIGHTBLACK_EX + 'enter "talk" or "explore"')
    else:
        print(Fore.RED + 'Invalid Action')
    data_logic = False

# Wednesday 24/05/2023 15:00-23:59
# Friday 26/05/2023 15:00-23:59
# Saturday 27/05/2023 7:00-23:59