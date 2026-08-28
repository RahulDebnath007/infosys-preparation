# 📚 Book Fair Problem

A greedy simulation solution to solve the **Book Fair Problem**, where a librarian places books onto shelves following a strict left-to-right priority rule.

---

## 🧩 Problem Overview

A school has **$N$ books** and **$N$ shelves**.
- Each book has a specific thickness.
- Each shelf has a specific capacity.

### Placement Rules
1. Process books from **left to right**.
2. For each book, scan shelves from **left to right**.
3. Place the book on the **first unused shelf** whose capacity is greater than or equal to ($\ge$) the book's thickness.
4. Once a shelf is used, it **cannot be reused**.
5. If no suitable shelf is found, the book remains **unplaced**.

**Goal:** Find the total number of unplaced books.

---

## 📥 Input & Output Format

### Input Format
* **Line 1:** Integer $N$ (number of books and shelves)
* **Next $N$ lines:** Book thicknesses (`Books` array)
* **Following $N$ lines:** Shelf capacities (`Shelves` array)

### Output Format
* Print a single integer representing the number of unplaced books.

### Constraints
* $1 \le N \le 10^3$
* $1 \le \text{Books}[i], \text{Shelves}[i] \le 10^5$

---

## 🧪 Example & Dry Run

### Input
```text
3
2
5
7
6
3
8