import random
jackpot = random.randint(1,100)
guess = int(input('Guess kro:'))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("galat!,guess higher")
    
    elif guess > jackpot:
        print("galat!,guess lower")
    guess = int(input('Guess kro:'))
    counter += 1
else:
        print("Sabsh beta")
        print("attempts", counter)
    
        