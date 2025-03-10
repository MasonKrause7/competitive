import re

word = input()

regex = "ss"

pattern = re.compile(regex)
if re.search(pattern, word):
    print("hiss")
else:
    print("no hiss")
