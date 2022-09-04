def guess(guess_number):
    number_guess = 3
    initial_guess = 0
    
    while initial_guess < number_guess:
        guesss = int(input("Enter the guess:"))
        if guesss == guess_number:
            print("Right")
            break
        initial_guess = initial_guess+1
    else:
        print("Play agian")
guess(12)