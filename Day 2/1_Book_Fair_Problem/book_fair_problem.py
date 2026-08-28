def arrange_books(n, books, shelves):
    used = [False] * n
    unplaced = 0

    for book in books:
        placed = False
        for j in range(n):
            if not used[j] and shelves[j] >= book:
                used[j] = True
                placed = True
                break
        if not placed:
            unplaced += 1
    return unplaced


if __name__ == "__main__":
    n = int(input().strip())
    books = [int(input().strip()) for _ in range(n)]
    shelves = [int(input().strip()) for _ in range(n)]
    print(arrange_books(n, books, shelves))
