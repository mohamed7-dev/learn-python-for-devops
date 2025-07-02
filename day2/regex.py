import re

text = "python is awesome!"
pattern = r"is"

# matches the beginning of the string
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

# scans all the string
search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

# substitute
new_text = re.sub(pattern, "was", text)
print(new_text)

# split
print(re.split(pattern,text))