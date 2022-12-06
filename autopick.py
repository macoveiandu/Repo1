import random
dice_roll = random.randint(1,6)
x = int(input('Alege un nr de zar: '))
if x<dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {dice_roll}')
elif x>dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {dice_roll}')
elif x==dice_roll:
    print(f'Ai ghicit. Felicitari! Ai ales {x} si zarul a fost {dice_roll}')