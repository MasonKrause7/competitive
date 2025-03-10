T = int(input())

for t in range(T):
    seq = [int(x) for x in input().split()]
    total_imported = 0 
    for i in range(1, len(seq)):
        imported_this_year = 0
        if seq[i] > 2*seq[i-1]:
            imported_this_year = seq[i] - 2*seq[i-1]
        total_imported += imported_this_year


    print(total_imported)
