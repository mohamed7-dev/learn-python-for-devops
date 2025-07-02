# division vs floor division
a = 5
b = 3
print("division",a/b)
print("float division",a//b) 


# identity operators
x = [1, 2, 3]
y = x  # now y refers to the same location in memory
result1 = x is y
print("is x in the same mem location as y",result1)

a = "hello"
b = "world"
result2 = a is not b
print("is a in a different mem location from b", result2)

# Membership operators
fruits = ["apple", "banana", "cherry"]
result3 = "banana" in fruits
print("is banana in fruits list",result3)

colors = ["red", "green", "blue"]
result4 = "yellow" not in colors
print("is yellow not in colors list", result4)

