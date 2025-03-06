import sys

x = [1, 2, 3]
y = x  # Another reference to x
z = x  # Another reference to x

m = z

# declaring an int
a = 12

print(sys.getrefcount(x))  # Should be at least 4 (x, y, z, and function argument)
print(sys.getrefcount(a))

j = a
k = a
print(sys.getrefcount(a))

