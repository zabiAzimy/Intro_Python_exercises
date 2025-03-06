# write a simple program which will asks a number from user and prints the square of it if it is odd
# if the entered number is even, it skips, if 'q' is entered the loop terminates.

# look at the following code and point out the possible error that we might face
# while True:
#     num = int(input('Enter a number: \nYou can always quit by entering [q]'))
#     if num == 'q':
#         break
#     elif num % 2 == 0:
#         print(f"{num} squared is {num * num}")
#     else:
#         continue



## now we are using else along with while loop
## in case the while loop ends without encountering 'beak' then else block will be executed 
numbers = [1, 3, 5, 2]
position = 0

# we are now writing a loop that ends normally
while position < len(numbers):
    if numbers[position] % 2 == 0:
        print("Even number is found!")
        break
    position += 1
else: # in case the break is not called, this block of code will be executed
    print("No even number is found")

## we come across 'iterators', 'iterables' ... 
## using iterators we can traverse through elements of an iterable
## touch upon using zip() ======> combines the given iterables



