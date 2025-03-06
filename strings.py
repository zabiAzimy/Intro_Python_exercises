# We can combine two string literals without using a + sgin
greeting_message = "Hello " 'I hope you ' "have a great day"

# print the greeting message
print(greeting_message)

# we can also put those string literals inside a parentheses
vowels = (
    "a" '''e'''
    'i'
    "o"
    'u'
)

print(vowels)

# defining another string containing all the letters
letters = 'abcdefghijklmnopqrstuvwxyz'

print(letters[-50:])

# define another string
tasks = 'get gloves,get mask,give cat vitamins,call ambulance'

# make use of the split() function
print(tasks.split(','))

# we can also call split() without any argument
print(tasks.split())

# define a list
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']

# make use of join() function
print(', '.join(crypto_list))

# another string
setup = "a duck goes into a bar..."

# use the function replace to replace 'duck' with 'marmoset'
print(setup.replace('duck', 'marmoset'))

print(f"The original setup string is still the same: {setup}")


# import string
import string

print(string.punctuation)


# define a string that contains punctuations 
blurt = "What the...!!?"

# conveniently removing the punctuation marks from a string
print(blurt.strip(string.punctuation))


# defining a multiline string
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

# check out for differences in the  outputs of index() and find()
##
##





