import random
import Villains
common = random.randint(1,3)
normal = random.randint(1,3)
rare = random.randint(1,3)
ultra_rare = random.randint(1,3)
items = ['']

if Villains.rarity == 1:
    if common == 1:
        item = 'bronze sword'
        items.append('bronze sword')
        hp = 0
        atk = 3
        dfn = 0
        spd = 0
        mgc = 0
        kg = 1
    elif common == 2:
        item = 'bronze helmet'
        items.append('bronze helmet')
        hp = 0
        atk = 0
        dfn = 1
        spd = 0
        mgc = 0
        kg = 1
    elif common == 3:
        item = 'bronze knife'
        items.append('bronze knife')
        hp = 0
        atk = 2
        dfn = 0
        spd = 0
        mgc = 0
        kg = 1

if Villains.rarity == 2:
    if normal == 1:
        item = 'leopard sword'
        items.append('leopard sword')
        hp = 0
        atk = 3
        dfn = 0
        spd = 1
        mgc = 0
        kg = 1
    elif normal == 2:
        item = 'jungle axe'
        items.append('jungle axe')
        hp = 0
        atk = 4
        dfn = 0
        spd = 0
        mgc = 0
        kg = 3
    elif normal == 3:
        item = 'bronze shield'
        items.append('bronze shield')
        hp = 0
        atk = 0
        dfn = 2
        spd = 0
        mgc = 0
        kg = 2

if Villains.rarity == 3:
    if rare == 1:
        item = 'mystical ice sword'
        items.append('mystical ice sword')
        hp = 3
        atk = 7
        dfn = 0
        spd = 0
        mgc = 0
        kg = 2
    elif rare == 2:
        item = 'inferno armour'
        items.append('inferno armour')
        hp = 4
        atk = 2
        dfn = 3
        spd = 0
        mgc = 0
        kg = 2
    elif rare == 3:
        item = 'ancient lightning rod'
        items.append('ancient lightning rod')
        hp = 2
        atk = 11
        dfn = 0
        spd = 8
        mgc = 0
        kg = 1

if Villains.rarity == 4:
    if ultra_rare == 1:
        item = 'divine God-sword'
        items.append('divine God-sword')
        hp = 100
        atk = 50
        dfn = 5
        spd = 10
        mgc = 50
        kg = 5
    elif ultra_rare == 2:
        item = 'bizarre mystical eye'
        items.append('bizarre mystical eye')
        hp = 20
        atk = 45
        dfn = 0
        spd = 8
        mgc = 45
        kg = 0
    elif ultra_rare == 3:
        item = 'aether giga-axe'
        items.append('aether giga-axe')
        hp = 0
        atk = 200
        dfn = 9
        spd = 0
        mgc = 5
        kg = 20