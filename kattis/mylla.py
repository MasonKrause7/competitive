m = []
won = False
for i in range(3):
    row = input()
    if row == 'OOO':
        won = True
        break
    m_row = []
    for j in row:
        if j == 'O':
            m_row.append(1)
        else:
            m_row.append(0)
    m.append(m_row)

if not won:
    if (m[0][0]==1 and m[1][0]==1 and m[2][0]==1) or (m[0][1]==1 and m[1][1]==1 and m[2][1]==1) or (m[0][2]==1 and m[1][2]==1 and m[2][2]==1):
        
        won = True
    if (m[0][0]==1 and m[1][1]==1 and m[2][2]==1) or (m[0][2]==1 and m[1][1]==1 and m[2][0]==1):
        
        won = True

if won:
    print('Jebb')
else:
    print('Neibb')
