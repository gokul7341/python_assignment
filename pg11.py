#Create a tuple of 3 elements and try to change one element. Observe and explain the error.
thistuple = ("red","blue","green")
f = list(thistuple)
f.remove("red")
thistuple = tuple(f)
print(f)


 