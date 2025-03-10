# defining a two value sequences into a dictionary
lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]

# create a dictionary from above list
lol_dict = dict(lol)

# print the dictionary
print(lol_dict)

# showcasing the usage of zip()
a = ['a', 'b', 'c', 'd']
b = [1, 2, 3, 4]

# let's create a dictionary from the above lists
a_b_dict = dict(zip(a, b))

print(a_b_dict)


# define a new dictionary
some_pythons = {
'Graham': 'Chapman',
'John': 'Cleese',
'Eric': 'Idle',
'Terry': 'Gilliam',
'Michael': 'Palin',
'Terry': 'Jones',
}

# use get()
print(some_pythons.get('Terry'))
print(some_pythons.get('Zabi', 'Not available!'))

# use key to get a value from dict
print(some_pythons['Eric'])

# this will raise an exception if the key is not available
# print(some_pythons['Zabi'])

# get all the keys
keys_list = list(some_pythons.keys())

print(keys_list)

# get all the values
values_list = list(some_pythons.values())

print(values_list)


# merging two dictionaries
first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}

# using {**a, **b} syntax
print({**first, **second})



# define a dictionary
pythons = {
'Chapman': 'Graham',
'Cleese': 'John',
'Gilliam': 'Terry',
'Idle': 'Eric',
'Jones': 'Terry',
'Palin': 'Michael',
}

# define another dictionary
others = { 'Marx': 'Groucho', 'Howard': 'Moe' }

# using update() function to combine dictioinaries
pythons.update(others)

# print the updated dictionary
print(pythons)

# del satement can be also used for dictionaries
del pythons['Marx']

print(pythons)

# using pop() in dictionary
popped_element = pythons.pop('Howard')

print(f"Popped value is {popped_element}")

# print again and confirm that value for the key 'Howard' is no longer existing
print(pythons)


# but if you are so fed up with your dictionary, use clear() === :)
pythons.clear()

# print again
print(pythons)


#### copying the dictionary / making a shallow copy of a dictionary
signals = {'green': 'go',
'yellow': 'go faster',
'red': ['stop', 'smile']}

# make a shallow copu using copy() 
# because the values of 'red' is mutable, the changes will be reflected to both the variables
signals_copy = signals.copy()


# to avoid that, let's use deepcopy()
import copy

# look at the syntax of deepcopy
signals_deep_copy = copy.deepcopy(signals)

print("="*20)
print("=== Before the changes ===")
print(f"Signals: {signals}")
print(f"signals_deep_copy: {signals_deep_copy}")

# let's change a value
signals_deep_copy['red'][1] = "sneak"

print("="*20)
print("=== After the changes ===")
print(f"Signals: {signals}")
print(f"signals_deep_copy: {signals_deep_copy}")

# iterating through a dictionary
# 1. The first option is to use for _ in dict
# it will give us the keys of the dictionary
for key in signals:
    print(key, end=" ")

# 2. getting only the values using values()
for value in signals.values():
    print(value)

# 3. getting the key and value at the same time, use items()
for key, value in signals.items():
    print(f"{key} --> {value}")

# similar to list comprehension, we also have dictionary comprehension
vocabulary = "intercontinental"

# using dictionary comprension to create a dict, key should be a character in dict and value, number of occurances of it
letter_count_dict = {character: vocabulary.count(character) for character in vocabulary}

# print the newly created dict
print(letter_count_dict)


# construct a dictionary from the following strings
# count the number of vowel characters iin the word string
vowels = 'aeiou'
word = 'onomatopoeia'

# dictionary comprehension with a condition test
vowel_count = {char: word.count(char) for char in word if char in vowels}

print(vowel_count)





