class GraphTrav:

    def __init__(self, adj_matrix: list[list[int]]):
        self.adj_matrix = adj_matrix
        self.graph = {}
        for i in range(len(adj_matrix)):
            for j in range(i+1, len(adj_matrix[i])):
                if adj_matrix[i][j] >= 1:
                    if i in self.graph:
                        self.graph[i].append(j)
                    else:
                        self.graph[i] = [j]
                    if j in self.graph:
                        self.graph[j].append(i)
                    else:
                        self.graph[j] = [i]

    def print_matrix(self):
        print(self.adj_matrix)

    def dfs_stack(self, node=0):
        seen = set([node])
        stack = [node]
        while stack:
            node = stack.pop()
            print(f"popped {node} from stack")
            for neighbor in self.graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

    def dfs_recursive(self, node=0):
        seen = set()
        
                    
            
        
            





matrix = [[1, 1, 0], [1, 1, 0],[0, 0, 1]]
gt = GraphTrav(matrix)
gt.print_matrix()
gt.dfs_stack()
                
    
