# define a tuple
one_marx = "Groucho", 

print(type(one_marx))

print(type("Groucho", ))

print(type(("Groucho", )))

# assigning multiple variables at once
# technically it is called tuple unpacking
marx_tuple = ('Groucho', 'Chico', 'Harpo')

# assign variables at once, using the tuple
a, b, c = marx_tuple

# print the vars
print(a, b, c)

# we can also use '+' to combine tuples
print(('a', 'b') + ('c',) + (3, 6, 'r') )

# let's check if we can combine the tuple variables
t1 = ('a', 'r')
t2 = ('z', 'y', 'e')

# print id of t1 before concatenation
print(f"Id of t1 before: {id(t1)}")

# print the combination of both
print(t1 + t2)

# let's now check if we can use tuple + the other
t1 += t2

print(t1)       # we can see that we do not have any error
                # this is no longer the same t1 ====> tuples are immutable

# print id of t1 after concatenation
print(f"Id of t1 after: {id(t1)}")


##### ========== Lists 
##### ========== Some common list functions are: split(), append(), insert(), list()
##### ========== To combine lists, we either use '+' or extend() method
##### using offset is similar to offset is string
##### Taking slice of a list also uses same offset as of string
##### we can use del statement to delete an element at a specific offset
##### we can use remove() to delete an element, if we don't care about the location
##### we use clear() to clear all elements of a list
##### 


### We can not use comprehension for immutable types
### The following code still does not give us exception
### surprisingly, that is not a tuple but a generator
number_thing = (num for num in range(1, 6))

# print it and check the type
print(type(number_thing))




