def solution(commands):
    merged = [[(0, 0) for _ in range(51)] for _ in range(51)]
    for i in range(1, 51):
        for j in range(1, 51):
            merged[i][j] = (i, j)
    content = [["EMPTY"]*51 for _ in range(51)]
    
    answer = []
    for command in commands:
        part = command.split()
        if part[0] == "UPDATE" and len(part) == 4:
            r, c = map(int, part[1:3])
            value = part[3]
            x, y = merged[r][c]
            content[x][y] = value
        elif part[0] == "UPDATE" and len(part) == 3:
            value1, value2 = part[1:]
            for i in range(1, 51):
                for j in range(1, 51):
                    if content[i][j] == value1:
                        content[i][j] = value2
        elif part[0] == "MERGE":
            r1, c1, r2, c2 = map(int, part[1:])
            x1, y1 = merged[r1][c1]
            x2, y2 = merged[r2][c2]
            for i in range(1, 51):
                for j in range(1, 51):
                    if merged[i][j][0] == x2 and merged[i][j][1] == y2:
                        merged[i][j] = (x1, y1)
                        
            if content[x1][y1] != "EMPTY" and content[x2][y2] != "EMPTY":
                content[x2][y2] = content[x1][y1]
            elif content[x1][y1] == "EMPTY":
                content[x1][y1] = content[x2][y2]
            elif content[x2][y2] == "EMPTY":
                content[x2][y2] = content[x1][y1]
                
        elif part[0] == "UNMERGE":
            r, c = map(int, part[1:])
            x, y = merged[r][c]
            tmp = content[x][y]
            for i in range(1, 51):
                for j in range(1, 51):
                    if merged[i][j][0] == x and merged[i][j][1] == y:
                        merged[i][j] = (i,j)
                        content[i][j] = "EMPTY"
            content[r][c] = tmp
        
        elif part[0] == "PRINT":
            r, c = map(int, part[1:])
            x, y = merged[r][c]
            answer.append(content[x][y])
            
    return answer