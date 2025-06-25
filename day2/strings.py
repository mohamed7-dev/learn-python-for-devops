
# Stripping strings
str = " hello world "
print(str.strip())

# Concat
print("python" + " " + "for dev ops")

# length
print(len(str))

# upper / lower
print(str.upper())
print(str.lower())

# replace
print(str.replace("world","python"))

# splitting
print(str.split(" "))

# sub-string
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")