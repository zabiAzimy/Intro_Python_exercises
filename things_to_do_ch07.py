# 1. create a list called years_list 
years_list = [1994, 1995, 1996, 1997, 1998, 1999]

# 2. print a message
print(f"My third birthday was in year {years_list[3]}.")

# 3. print the year from the list where I am the oldest
print(f"In year {years_list[-1]} I am the oldest.")

# 4.define another list
things = ["mozzarella", "cinderella", "salmonella"]

# 5. Capitialize the element that refers to a person
things[1] = things[1].capitalize()

# print and check of the element is really capitalized
print(f"Elements of the things list: {things}")


# 6. Make the cheesy elements of the things list uppercase 
for index, thing in enumerate(things):
    if thing in ["mozzarella", "salmonella"]:
        things[index] = thing.upper()

# print the list
print(things)

# 7. Delete the disease element === What is disease element here?
# How to delete a specific element of a list? ------ using del statement?
del things[-1]

# print the list after deleting one element
print(things)



# 8. Create another list called surprise
surprise = ["Groucho", "Chico", "Harpo"]

# 9. lowercase the last element, reverse it and then capitalize it

# lowercase the last element
surprise[-1] = surprise[-1].lower()

# reverse the last element
surprise[-1] = surprise[-1][::-1]

# capitalize the last element
surprise[-1] = surprise[-1].capitalize()

# print the list after the changes
print(f"\nElement of surprise list: {surprise}")

# 10. create a list using list comprehension to take only even numbers in range(10)
even = [number for number in range(10) if number % 2 == 0]

print(f"\nEven numbers: {even}\n\n")
print("=" * 30)
# 11. Jump rope rhyme maker

start1 = ["fee", "fie", "foe"]
rhymes = [
("flop", "get a mop"),
("fope", "turn the rope"),
("fa", "get your ma"),
("fudge", "call the judge"),
("fat", "pet the cat"),
("fog", "walk the dog"),
("fun", "say we're done"),
]
start2 = "Someone better"

for s1, rhyme in zip(start1, rhymes):
    print(f"{s1.capitalize()}! {rhyme[0].capitalize()}!")
    print(f"{start2} {rhyme[1]}.")

print("\n\n")
