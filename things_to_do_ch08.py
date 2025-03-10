# 1. Make and english to French dictioinary
e2f = {
'dog': 'chien',
'cat': 'chat',
'walrus': 'morse'
}

print(f"=== E2F dictionary: {e2f}\n")

# 2. Print the French word for Walrus
print(f"French word for walrus is: {e2f['walrus']}\n")

# define an empty dictionary f2e
f2e = dict()

# 3. Make a French to English dictionary
for key, value in e2f.items():
    f2e[value] = key

# print the f2e dictionary
print(f"=== F2E dictionary: {f2e}")


# 4. print the English equivalent of the word 'chien'
print(f"English word for chien is {f2e['chien']}\n")


# 5. print the set of words from e2f
print(f"Set of English words: {e2f.keys()}\n")

# 6. Make a multilevel dictionary
life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}

# 7. print the top level keys of life dictionary
print(f"Top level keys of life dictionary: {life.keys()}\n")

# 8. Print the keys for life['animals']
for key in life['animals'].keys():
    print(key)

print("==========")

# 9. Print the values for life['animals']['cats]
for value in life['animals']['cats']:
    print(value)


# 10. Use a dictionary comprehension 
squares = {number : number * number for number in range(10)}

print(squares)

# 11. Use a set comprehension to create odd numbers from the range(10)
odd_set = {number for number in range(10) if number % 2 != 0}

print(f"Odd set of numbers in range of 10: {odd_set}\n")

# 12. Use a generator comprehension to return the string 'got' and a number from range(10)
generator_object = (f"Got {number}" for number in range(10))

# print the type of it 
print(type(generator_object))

# Use a for loop to iterate over this generator
for i in generator_object:
    print(i)

# 13. Use zip for this question
key_tuple = ('optimist', 'pessimist','troll')

value_tuple = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')

# define an empty dict
new_dict = dict()

# use a for loop along with zip() function
for key, value in zip(key_tuple, value_tuple):
    new_dict[key] = value

print(f"New dictionary: {new_dict}")

# 14. Use zip to pair the following lists to make a dictionary
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']

plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']

titles_plot_dict = dict()

for title, plot in zip(titles, plots):
    titles_plot_dict[title] = plot


# print the dictionary
print(f"Titles_plots dictionary: {titles_plot_dict}\n")