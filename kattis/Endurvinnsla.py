city = input()
percent_nonplastic_allowed = float(input())
num_items = int(input())
num_non_plastics = 0
num_plastics = 0
for i in range(num_items):
    if input() == "plast":
        num_plastics = num_plastics + 1
    else:
        num_non_plastics = num_non_plastics + 1

if(num_non_plastics / num_items) <= percent_nonplastic_allowed:
    print("Jebb")
else:
    print("Neibb")
