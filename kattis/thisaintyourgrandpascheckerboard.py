def solve(n):
    board = []

    for i in range(n):
        row = input()
        occs = {'B': [], 'W': []}
        in_a_row = 0
        for j in range(n):
            occs[row[j]].append(j)
            
            if i >=2 and j in board[i-1][row[j]] and j in board[i-2][row[j]]:
                return 0#3 in a row vertically

            if j == 0:
                in_a_row += 1
                continue
            else:
                if j > 0 and  row[j] == row[j-1]:
                    in_a_row += 1
                    if in_a_row == 3:#3 in a row horiz
                        return 0
                else:
                    in_a_row = 1

        if len(occs['B']) != len(occs['W']):#diff # B to W in horiz row
            return 0

        board.append(occs)

    for j in range(n):
        num_b = 0
        num_w = 0
        for i in range(n):
            if j in board[i]['B']:
                num_b += 1
            else:
                num_w += 1
        if num_b != num_w:
            return 0

    return 1

n = int(input())

print(solve(n))
