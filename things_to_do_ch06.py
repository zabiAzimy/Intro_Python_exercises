# ======== 1. use a for loop to print the elements of the following list
# magic_numbers = [3, 2, 1, 0]

# for n in magic_numbers:
#     print(n, end=" ")

## ======== 2. Assign the value 7 to variable guess_me
guess_me = 7
number = 1

# write a while loop
while True:
    if number < guess_me:       # check if number is less than guess_me
        print("Too low!")
    elif number == guess_me:    # check the equality
        print("Found it! ")
        break
    elif number > guess_me:     # check if the number is greater than guess_me
        print("Oops!")
        break
    number += 1                 # increment the number at the end of each iteration


## ======= 3. Assign the value 5 to the variable guess_me and follow the instructions in the book

print("\n======== Using for loop ========\n")
guess_me = 5

# use a for loop to iterate over a range of 10
for number in range(10):
    if number < guess_me:       # check if number is less than guess_me
        print("Too low!")
    elif number == guess_me:
        print("Found it!")      # check equality
        break
    elif number > guess_me:     # check if number is greater than guess_me
        print("Oops!")
        break