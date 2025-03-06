from datetime import datetime


# get the name from the user
name = input("Please enter your name: ")

# get the birht year of the user
birth_year = int(input("Please enter your birth year: "))

# get the current year using the datetime library
current_year = datetime.now().year

# calculate the age of the user
user_age = current_year - birth_year

# years until 100 
years_until_100 = 100 - user_age


# print the message back to user
print(f"Hey {name}, you will be hundred years old in the year {current_year + years_until_100}")

# ask the user about a number
count = int(input("How many times to display the message? "))

for _ in range(count):
    print(f"Hey {name}, you will be hundred years old in the year {current_year + years_until_100}")