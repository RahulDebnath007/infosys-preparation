# 📚 Book Fair Problem

## 🧩 Problem Overview

A school has `N` books and `N` shelves.

Each book has a thickness, and each shelf has a capacity.

The librarian follows a fixed placement strategy:

1. Process books from left to right.
2. For each book, check shelves from left to right.
3. Place the book on the **first unused shelf** whose capacity is greater than or equal to the book's thickness.
4. Once a shelf is used, it cannot be used again.
5. If no suitable shelf is available, the book remains unplaced.

The task is to find the total number of **unplaced books**.

---

## 📥 Input Format

The input consists of:

- The first line containing an integer `N`.
- The next `N` lines containing the `Books` array.
- The next `N` lines containing the `Shelves` array.

### Example

```text
3
2
5
7
6
3
8