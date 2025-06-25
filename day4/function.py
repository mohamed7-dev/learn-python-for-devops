from package1 import module1


def sayHelloUser(name):
    return f"Hello, {name}!"

message = sayHelloUser("mohamed")
print(message)

print(module1.createUser("mohamed"))