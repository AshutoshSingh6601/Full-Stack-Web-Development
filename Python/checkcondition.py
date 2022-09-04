guess_number=5
initial_number=0
total_number=3

while initial_number < total_number:
        guess = int(input("Enter the guess:"))
        if guess == guess_number:
            print("Right Guess")
            break
        initial_number = initial_number+1
else:
    print("Wrong Guess")