def find_sequence(matrix, m, n):
    sequences = set()

    
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    for i in range(m):
        for j in range(n):
            num = matrix[i][j]
            for dx, dy in directions:
                count = 1
                x, y = i + dx, j + dy
                while 0 <= x < m and 0 <= y < n and matrix[x][y] == num:
                    count += 1
                    if count >= 4:
                        sequences.add(num)
                        break
                    x += dx
                    y += dy

    return min(sequences) if sequences else -1

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

print(find_sequence(matrix, m, n))
