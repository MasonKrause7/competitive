import re

regex = "[A-Z]"

pattern = re.compile(regex)

caps = re.findall(pattern, input())
for c in caps:
    print(c, end="")
