user = {
    'name': "john doe",
    'avatar': 'cloudinary.com/image-1.jpg',
    'email':'test@test.com',
    'password':'easy-one'
}

print(user)
print(user['name']) # only bracket notation is allowed, no dot notation

# Delete prop
del user['password']

# Loop Over dict props

for prop in user.items():
    # prop is a tuple(key , value)
    print(prop)

# Check existence of a prop
if('password' in user):
    print("Warning: unsafe strip the password")


