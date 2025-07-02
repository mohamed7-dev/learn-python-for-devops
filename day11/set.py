# Set is a DS that stores data unordered and only unique values.
# it's useful in the context of the maths operations such as intersect, union, and difference

my_set = {0,1,1, 2, 3,3, 4, 5}
my_set.add(6)
my_set.remove(0)

# Union
print(my_set.union({6,6,7,8}))

# Intersection
print(my_set.intersection({0,8}))

# Difference
print(my_set.difference({0,1}))

# Subset
print(my_set.issubset({1,2,3,4,5})) # false

# Superset
print(my_set.issuperset({10})) # false