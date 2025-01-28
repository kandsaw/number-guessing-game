def game():
    import random
    import art
    print(art.logo)
    numbers = list(range(1, 101))
    random_number=random.choice(numbers)


    print("welcome to the number guessing game !")
    print(" i am thinking of a number from 1 to 100.")
    game_difficulty=input("choose a difficulty. type  'easy' or 'hard':").lower()
    if game_difficulty=='easy':
        attempt=10
    elif game_difficulty=='hard':
        attempt=5
    else:
        print("invalide choice")

    count = 0


    while count<attempt:
        guess=int(input("have a guess:"))

        if guess==random_number:
            print("congrats you win")
            break
        elif guess<random_number:
            print("too low")
        else:
            print("too high")
        count+=1
        print(f"you have used {attempt-count} attempts")
    if count==attempt:
        print("you lose")
        print(f"the correct number was {random_number}")





game()







