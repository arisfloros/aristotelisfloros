import random 

RANDOM_RANGE_MIN = 0 
RANDOM_RANGE_MAX = 101

guesses = 0
isTrue = False

random_number = random.randint(RANDOM_RANGE_MIN, RANDOM_RANGE_MAX)

range_half = RANDOM_RANGE_MAX / 2


while True:

    guesses += 1
    

    user_guess = input(f"Add a number from {RANDOM_RANGE_MIN} - {RANDOM_RANGE_MAX - 1}: ")
    if user_guess.isdigit():
            user_guess = int(user_guess)

            if user_guess <= 0 :
                print('Please type a number larger than 0 next time.')
                quit()
    else:
        print('please type a number next time')
        quit()

    if user_guess > random_number:
        print("You are higher")
    elif user_guess < random_number:
        print("You are lower")
    else:
        print("You win GG. !")
        break

