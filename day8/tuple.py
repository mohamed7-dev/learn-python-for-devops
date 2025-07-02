admins = ("admin_1","admin_2","admin_3")

# Note: in Tuples we can't mutate data

# admins.append("admin_4") # throws an error

print(len(admins))
print(admins[1])

# in python we must include a trailing comma
# to differentiate between a string in parenthesis and the tuple
print(admins + ("admin_4",))
print('admin_1' in admins)


# Tuple Packing / UnPacking (similar to destructuring in js)
# but in python variables on the left-side need to match the tuple elements
a, b, c = admins
print(a,b,c)

# when returning multiple output values from a function a tuple is usually used
def get_coordinates():
    return (3, 4)
x, y = get_coordinates()
print(x,y)