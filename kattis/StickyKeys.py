S = input()
if len(S) == 1:
    print(S)

else:
    print(S[0], end="")
    for i in range(1,len(S)):
        if S[i] == S[i-1]:
            pass
        else:
            print(S[i], end="")
    
