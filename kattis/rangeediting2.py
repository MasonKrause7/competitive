def getIndeces(x,i,j):
    global a
    indeces = [index+i+1 for index, elem in enumerate(a[i+1:j]) if elem == x]
    return indeces



def minCost(i,j):
    

    return 1


n = int(input())
a  = []
for _ in range(n):
    a.append(int(input()))

total_edits = 0
indeces_of_zero = getIndeces(0, -1, n)
print(indeces_of_zero)
if not indeces_of_zero:
    total_edits = minCost(-1,n)
elif len(indeces_of_zero) <= 2:
    if indeces_of_zero[0] == 0 and indeces_of_zero[-1]==0:
        total_edits = minCost(0,n-1)
    elif indeces_of_zero[0]==0 and indeces_of_zero[-1] != 0:
        total_edits = minCost(-1,n)
    elif indeces_of_zero[0]!=0 and indeces_of_zero[-1] == 0:
        total_edits = minCost(0,n)
else:
    total_edits += minCost(-1, indeces_of_zero[0])
    for i in range(1, len(indeces_of_zero)):
        total_edits+=minCost(indeces_of_zero[i-1], indeces_of_zero[i])
    total_edits += minCost(indeces_of_zero[i], n)



print(total_edits)
    
        
