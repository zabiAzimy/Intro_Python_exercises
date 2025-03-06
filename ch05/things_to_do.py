# define a string containing the song
song = """When an eel grabs your arm,
 And it causes great harm,
 That's - a moray!"""

# 1. capitalize the word of the above song that starts with 'm'
# let's first split
song_words = song.split()

print(song_words)

# remember that we can also use enumerate() here to have the index and element at the same time
for index, element in enumerate(song_words):
    if element.startswith("m"):
        song_words[index] = song_words[index].capitalize()

print(song_words)

# join the above elements back
song_words_capitalized = ' '.join(song_words)
print(song_words_capitalized)


# replacing the m with capital m --- Not the solution 
capitalized_song = song.replace("moray", "Moray")
print(capitalized_song)

# Solution of question 1 is still missing
#


# 2. Print each list question with its correctly matching answer, in the form:
# Q: question
# A: answer
questions = [
"We don't serve strings around here. Are you a string?",
"What is said on Father's Day in the forest?",
"What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
"An exploding sheep.",
"No, I'm a frayed knot.",
"'Pop!' goes the weasel."
]


# we have two lists above, first one contains the questions and the second one contains the answers
# let's fist check if the length of both are equal
print(f"Lenght of both lists are equal? {len(questions) == len(answers)}")

print("==" * 40)


# after confirming their lengths are equal we run a for loop
for i in range(len(questions)):
    print(f"Q: {questions[i]}")
    print(f"A: {answers[i]}")

## 
print("=="*40)
print("Formatting the letter")
print("=="*40)

print("\n")


# 4. format the following letter
letter = """Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.
Thank you for your support.

Sincerely,
{spokesman}
{job_title}"""


# assign values to the above variables
salutation = "Mr. "
name = "Alex"
verbed = "broke down"
room = "kitchen"
animals = "dog"
amount = "$20"
product = "vacuum cleaner"
percent = 29
spokesman = "Jacob"
job_title = "Sales manager"

# now we print the above letter using the format() function
print(letter.format(salutation=salutation, name=name, product=product, verbed=verbed, 
                     room=room, animals=animals, amount=amount, percent=percent, spokesman=spokesman, job_title=job_title))
print("\n")


print("=="*40)
print("Using the old style formatting")
print("=="*40)

english_submarine = "Boaty McBoatface"
australian_racehorse = "Horsey McHorseface"
swedish_train = "Trainy McTrainface"

first_prize = "duck"
second_prize = "gourd"
third_prize = "spitz"

# print the winning names and the prizes
print("%s Has won a %s" % (english_submarine, first_prize))
print("%s Has won a %s" %(australian_racehorse, second_prize))
print("%s Has won a %s" %(swedish_train, third_prize))

print("=" * 40)

# using format to print the same message
print("{} has won the {}".format(english_submarine, first_prize))
print("{} has won the {}".format(australian_racehorse, second_prize))
print("{} has won the {}".format(swedish_train, third_prize))

print("=" * 40)

# using the f-string to print the message
print(f"{english_submarine} has won the {first_prize}")
print(f"{australian_racehorse} has won the {second_prize}")
print(f"{swedish_train} has won the {third_prize}")






