n = int(input())

for i in range(n):
    line = input()

    if line == "P=NP":
        print("skipped")
    else:
        x,y = [int(x) for x in line.split("+")]
        print(x+y)
        
