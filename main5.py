# Slicing
x = ["a", "b", "c", "d"]
print(x[:2])
print(x[2:])
print(x[:])

x[0:2] = ["1", "a"]

# Plus List
a = x + ["q", "t"]

# Delete element
del (a[1])  # Remove a

x1 = ["a", "b", "c"]
y = x
y[1] = "z"


x2 = ["a", "b", "c"]
y2 = list(x2) # Copy from x2 and change y2 cannot change x2
y = x2[:]

# round

# pow
