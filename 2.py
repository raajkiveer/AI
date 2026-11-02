from collections import deque

grid = [ [0,0,0],
              [1,1,0],
              [0,0,0] ]
start, goal = (0,0), (2,2)
q = deque([(start, [start])])
visited = {start}

while q:
    (r, c), path = q.popleft()

    if (r, c) == goal:
        print("Path:", path)
        break

    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3 and grid[nr][nc] == 0 and (nr,nc) not in visited:
            visited.add((nr,nc))
            q.append(((nr,nc), path + [(nr,nc)]))
else:
    print("No path found")
