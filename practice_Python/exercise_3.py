# write a program that prints all the elements that are smaller than five from the following list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# running a loop that performs a comparison
for element in a:
    if element < 5:
        print(element)


# storing all the elements that are smaller than 5 in a separate list
less_than_five_list = []
for element in a:
    if element < 5:
        less_than_five_list.append(element)

# print the above list
print(f"List of elements less than 5: {less_than_five_list}")


# writing this in one line code
less_than_five_list_01 = [element for element in a if element < 5]


# print the list constructed with list comprehension
print(f"{less_than_five_list_01}")


# take a number from user
user_input = int(input("Enter a number: "))


for element in a:
    if element <= user_input:
        print(element)


