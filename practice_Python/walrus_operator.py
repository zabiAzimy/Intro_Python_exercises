
# diff = tweet_limit - len(tweet_string)

# # print the difference
# print(f"Difference in length: {diff}")

# # check if difference is not zero (i.e the length is more than limit)
# if diff >= 0:
#     print("A fitting sweet")
# else:
#     print(f"Went over by {abs(diff)}")


# using walrus operator this time
# tweet_limit = 180
# tweet_string = "Blah" * 50
# if diff := tweet_limit - len(tweet_string) >= 0:
#     print("A fitting tweet")
# else:
#     print("Went over by", abs(diff))
#     print(f"Type of diff variable: {type(diff)}")


if (n := len([1, 2, 3])) > 2:
    print(f"List has {n} elements")
    i = n * 3
    print(f"printing i from within the if block: {i}")


# checking if 'n' is accessible outside the if block 
print(f"Number of elements in the list: {n}")

# checking if 'i' is accessible outside the if block
print(f"Value stored in varibale i: {i}")