import random 

highest_val = 1000
lowest_val = 1
answer = random.randint(lowest_val, highest_val) 
print(answer)#TODO remove this after we finish the code 

max_guesses = 20
guess_count = 0

print("Please enter a number from {} to {}: ".format(lowest_val, highest_val)) 

while guess_count < max_guesses:
    guess = int(input()) 
    guess_count += 1

    if guess == 0: 
        break 
    if guess == answer: 
        print("Well done, you found the number") 
        break 
    else: 
        if guess<answer: 
            print("Please guess higher, or type 0 to quit") 
        else: 
            print("Please guess lower, or type 0 to quit") 

if guess_count == max_guesses:
    print("Sorry, you have exceeded the maximum number of guesses.")
