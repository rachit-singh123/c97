import random
print("number guessing game")
number=random.randint(1,9)
chances=0


while chances< 5:

    guess=int(input("enter ur guess:"))
    if guess == number:


        print("congrats")
        break
    elif guess<number:
        print("ur guess is too low!",guess)
    else:
        print("ur guess is too high",guess)
    chances+=1

if not chances<5:
    print("u loose",number)
