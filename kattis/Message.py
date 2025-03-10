rowsAndCols = [int(x) for x in input().split()]
rows = rowsAndCols[0]
cols = rowsAndCols[1]

message = ""
index = 0
for i in range(rows):
    row = input()
    for j in range(index, cols):
        if row[j] == ".":
            if index > 0:
                index =- 1;
            pass
        else:
            message = message + row[j]
print(message)
    
