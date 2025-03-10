opening = ['(','{','[']
closing = [')','}',']']
parens = ['(', ')']
squares = ['[',']']
curlys = ['{','}']

def isBalanced(seq)->bool:
    stack = []
    for c in range(len(seq)):
        if seq[c] in opening:
            stack.append(seq[c])
        else:
            
            if stack and (seq[c] in parens and stack[-1] == parens[0]) or (seq[c] in squares and stack[-1] == squares[0]) or (seq[c] in curlys and stack[-1] == curlys[0]):
                stack.pop()
            else:
                return False

    if stack:
        return False
    else:
        return True

def dfs(root, longer_path, shorter_path, num_paths, edges):
    if root not in edges:
        #check if were balanced and add to num_paths if so
    else:
        for edge in edges:
            dfs(edge, longer_path+chars[edge], shorter_path)

n = int(input())

chars = input()

edges = {}
for _ in range(n-1):
    parent, child = [(int(x)-1) for x in input().split()]
    if parent in edges:
        edges[parent].append(child)
    else:
        edges.update({parent: [child]})



num_paths = 1 #empty string
print(dfs()




