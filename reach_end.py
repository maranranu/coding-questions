def reachTheEnd(grid, maxTime):
    # Write your code here
    if grid[0][0] == '#':
        return 'No'
    neigh = [[0, 1], [0, -1], [1,0], [-1, 0]]
    q = []
    q.append([0, 0])
    col = len(grid)
    row = len(grid[0])
    pcount = 0
    
    while len(q):
        p = q.pop()
        grid[p[0]] = grid[p[0]][:p[1]] + '#' + grid[p[0]][p[1] + 1: ]
        print(grid[p[0])
        #grid[p[0]][p[1]] = '#'
        if p == (row-1, col-1):
            print(pcount)
            return 'Yes'
        for i in range(4):
            p1 = p[0] + neigh[i][0]
            p2 = p[1] + neigh[i][1]
            if p1 >= 0 and p2 >= 0 and p1 < row and p2 < col and grid[p1][p2] == '.':
                pcount += 1
                print(pcount)
                q.append((p1, p2))
    return 'No'

print(reachTheEnd(['..##', '#.##', '#...'], 5))
