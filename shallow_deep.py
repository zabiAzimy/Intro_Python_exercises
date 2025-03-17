# # let's see the copy() behavior
# a = [1, 2, 5, 6]

# b = a

# print(f"Before changing: {a}")
# print(f"Before changing: {b}")

# # make some changes to any of the list
# b[2] = 99

# # the changes will reflect in both the lists
# print(f"Before changing: {a}")
# print(f"Before changing: {b}")

# print("======================")

# # I will make another copy of list a
# c = a.copy()
# print(f"Before changing: {a}")
# print(f"Before changing: {c}")
# print("======================")

# c[-1] = 555
# print(f"After changing: {a}")
# print(f"After changing: {c}")

# move forward and make a list that contains mutable data type
# list inside this list
# new_list = [[1,2,3], [3,5,7], [1]]

# # let's make a copy of the above list
# t = new_list.copy()

# print(f"Before changing: {new_list}")
# print(f"Before changing: {t}")

# t[1][0] = 100

# print("=================")
# print(f"After changing: {new_list}")
# print(f"After changing: {t}")


# new_list = [(1,2,3), (3,5,7), (1)]

# # let's make a copy of the above list
# t = new_list.copy()

# print(f"Before changing: {new_list}")
# print(f"Before changing: {t}")

# new_list[-1] = (3,6,7)

# print("=================")
# print(f"After changing: {new_list}")
# print(f"After changing: {t}")

# accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
#     'person': 'Col. Mustard'}


# for item in accusation.items():
#     print(item)

# print("=========")

# for card, contents in accusation.items():
#     print('Card', card, 'has the contents', contents)

# dictionary comprehension
letter = 'wordingg'

simple_dict = {i:letter.count(i) for i in letter}

print(simple_dict)
