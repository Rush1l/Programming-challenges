print('For what six-digit number SLAYER is the following equation true, where each letter stands for the digit in the position shown: SLAYER + SLAYER + SLAYER = LAYERS')
slayer = str(input('Enter your guess for SLAYER: '))

layers = slayer[1]+slayer[2]+slayer[3]+slayer[4]+slayer[5]+slayer[0]
layers = int(layers)

LAYERS = int(slayer)*3

if LAYERS == layers:
    print('Your guess is correct:')
else:
    print('Your guess is incorrect:')


print(f'SLAYER + SLAYER + SLAYER = {LAYERS}')
print(f'LAYERS = {layers}')
print('Thanks for playing.')

    
