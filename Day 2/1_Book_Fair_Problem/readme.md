📚 Book Fair Problem

🧩 Pattern: Arrays + Greedy Placement + Simulation
🎯 Goal: Place each book on the first available shelf that can hold it and count how many books remain unplaced.

📌 Problem Statement

A school is organizing a book fair with:

📚 N books
🗄️ N shelves

Each book has a thickness, and each shelf has a capacity.

The librarian follows a strict placement process:

📚 Process books from left to right.
🗄️ For each book, check shelves from left to right.
🔍 Find the first unused shelf whose capacity is at least the book's thickness.
✅ Place the book there.
🔒 Once a shelf is used, it cannot be used again.
❌ If no suitable shelf exists, leave the book unplaced.

Finally, output the total number of unplaced books.

🧪 Sample
📥 Input
3
2
5
7
6
3
8

The input represents:

N = 3

Books:
2
5
7

Shelves:
6
3
8
🔍 Understanding the Example
📚 Book 1 → Thickness 2

Shelves:

Shelf 1 → 6
Shelf 2 → 3
Shelf 3 → 8

Check from left to right:

6 >= 2 ✅

So Book 1 goes to Shelf 1.

Shelf 1 → 🔒 Used
Shelf 2 → 3
Shelf 3 → 8
📚 Book 2 → Thickness 5

Start checking from the first shelf:

Shelf 1 → 🔒 Used
Shelf 2 → 3 ❌
Shelf 3 → 8 ✅

Book 2 goes to Shelf 3.

Shelf 1 → 🔒 Used
Shelf 2 → 3
Shelf 3 → 🔒 Used
📚 Book 3 → Thickness 7

Check remaining shelves:

Shelf 1 → 🔒 Used
Shelf 2 → 3 ❌
Shelf 3 → 🔒 Used

No suitable shelf exists.

Therefore:

Book 3 → ❌ Unplaced
🎯 Final Answer
1
📥 Input Format

The first line contains an integer N.

The next N lines contain the Books array.

The following N lines contain the Shelves array.

N
Books[0]
Books[1]
...
Books[N-1]
Shelves[0]
Shelves[1]
...
Shelves[N-1]
📤 Output Format

Print a single integer representing the number of books that could not be placed.

🔢 Constraints
1 ≤ N ≤ 10³
1 ≤ Books[i], Shelves[i] ≤ 10⁵
🧠 Core Idea

This is a simulation problem.

You must follow the exact process described in the problem.

📚 Take next book
       ↓
🗄️ Check shelves left → right
       ↓
🔍 Is shelf unused AND capacity enough?
       ↓
   ┌───┴───┐
  YES      NO
   ↓        ↓
✅ Place   🔍 Check next shelf
   ↓
🔒 Mark used
   ↓
📚 Next book

If every shelf is checked and none works:

❌ Unplaced += 1
1️⃣ 🔒 Track Used Shelves

We need to remember which shelves have already been used.

Create:

used = [False] * n

For example, when:

N = 3

we start with:

used = [False, False, False]

Meaning:

Shelf 1 → Available
Shelf 2 → Available
Shelf 3 → Available

After using Shelf 1:

used = [True, False, False]

Now:

Shelf 1 → 🔒 Used
Shelf 2 → Available
Shelf 3 → Available
2️⃣ 📚 Process Books in Order

The problem explicitly says books must be processed from left to right.

So:

for book in books:

processes them in their original order.

For:

Books = [2, 5, 7]

the order is:

2 → 5 → 7

⚠️ Do not sort the books.

Sorting would change the required process.

3️⃣ 🗄️ Search Shelves from Left to Right

For every book:

for j in range(n):

checks:

Shelf 0
Shelf 1
Shelf 2
...

in order.

We need two conditions:

if not used[j] and shelves[j] >= book:
Condition 1️⃣
not used[j]

means:

Is this shelf still available?

Condition 2️⃣
shelves[j] >= book

means:

Can this shelf hold the book?

Both must be true.

4️⃣ ✅ Place the Book

When we find a suitable shelf:

used[j] = True

marks that shelf as unavailable.

Then:

placed = True

records that the book was successfully placed.

Finally:

break

stops searching shelves.

🚨 Why is break important?

The problem says:

Use the first suitable shelf.

Suppose:

Book = 5

Shelves:
6  8  10

All three can hold the book.

But the correct choice is:

6
↑
First suitable shelf

Therefore we must stop immediately after finding it.

5️⃣ ❌ Handle an Unplaced Book

Before searching, we assume:

placed = False

If no shelf works, it remains:

False

After checking all shelves:

if not placed:
    unplaced += 1

So the counter increases.

💻 Complete Python 3 Solution
def arrange_books(n, books, shelves):
    # Track which shelves have already been used
    used = [False] * n

    # Count books that cannot be placed
    unplaced = 0

    # Process books from left to right
    for book in books:
        placed = False

        # Search shelves from left to right
        for j in range(n):

            if not used[j] and shelves[j] >= book:
                used[j] = True
                placed = True
                break

        # No suitable shelf found
        if not placed:
            unplaced += 1

    return unplaced


if __name__ == "__main__":
    n = int(input().strip())

    books = [int(input().strip()) for _ in range(n)]
    shelves = [int(input().strip()) for _ in range(n)]

    print(arrange_books(n, books, shelves))
🧪 Dry Run
📥 Input
3
2
5
7
6
3
8

Arrays:

Books   = [2, 5, 7]
Shelves = [6, 3, 8]

Initial state:

used = [False, False, False]
unplaced = 0
🔄 Book 1 = 2

Check:

Shelf 1 → 6 >= 2 ✅

Place it.

used = [True, False, False]
unplaced = 0
🔄 Book 2 = 5

Check:

Shelf 1 → Used 🔒
Shelf 2 → 3 >= 5 ❌
Shelf 3 → 8 >= 5 ✅

Place it.

used = [True, False, True]
unplaced = 0
🔄 Book 3 = 7

Check:

Shelf 1 → Used 🔒
Shelf 2 → 3 >= 7 ❌
Shelf 3 → Used 🔒

No shelf available.

unplaced = 1
📤 Output
1
🧩 Why This Is a Greedy Problem

The librarian always makes the decision:

Take the first available shelf that can hold the current book.

There is no attempt to reconsider previous placements.

For example:

Books   = [2, 5]
Shelves = [6, 8]

For Book 2:

6 >= 2

so the librarian must use Shelf 1.

Even though Shelf 2 could also hold it, the rule says:

👉 First suitable shelf

This is a greedy choice because we make the required local choice immediately and move forward.

🚨 Important: Don't Sort Anything

A common mistake would be:

books.sort()
shelves.sort()

❌ Don't do this.

The problem requires:

📚 Original book order
+
🗄️ Original shelf order

The position of each shelf matters.

For example:

Books   = [5, 2]
Shelves = [2, 5]

For Book 5:

Shelf 1 → 2 ❌
Shelf 2 → 5 ✅

Shelf 2 becomes used.

Then Book 2 has only Shelf 1:

2 >= 2 ✅

Both get placed.

Changing the order could produce a different process.

🧠 Recognition Pattern

When you see:

"Process items in order and assign each item to the first available position that satisfies a condition."

Think:

🔁 Simulation
+
🟢 Used/Available tracking
+
👉 First valid choice

This is a very common coding-assessment pattern.

🧠 Exam Recognition Table
📝 Problem Clue	💡 Think
Process books in given order	🔁 for loop
Search shelves left → right	🔄 Nested loop
Shelf can be used once	🔒 used[]
Capacity must be enough	shelves[j] >= book
First suitable shelf	break
Cannot place	unplaced += 1
Follow exact process	🧩 Simulation
First valid choice	🏆 Greedy
⚠️ Common Mistakes
❌ Mistake 1 — Forgetting to mark the shelf

Wrong:

if shelves[j] >= book:
    placed = True

This allows the same shelf to be reused.

Correct:

used[j] = True
❌ Mistake 2 — Not using break

Without:

break

the program may continue searching and potentially assign the same book to multiple shelves.

Correct:

used[j] = True
placed = True
break
❌ Mistake 3 — Sorting
books.sort()
shelves.sort()

❌ Wrong because the original order is part of the problem.

❌ Mistake 4 — Using > instead of >=

A shelf with capacity exactly equal to the book thickness can hold it.

Example:

Book = 5
Shelf = 5

This is valid:

shelves[j] >= book

Not:

shelves[j] > book
⏱️ Complexity Analysis

There are N books.

For each book, we may scan all N shelves.

Therefore, worst case:

⏱️ Time Complexity: O(N²)

With:

N ≤ 1000

the worst case is roughly:

1000 × 1000 = 1,000,000

shelf checks, which is completely reasonable.

💾 Space Complexity

We maintain:

used = [False] * n

Therefore:

💾 Space Complexity: O(N)
🗺️ Complete Mental Model
                    📚 BOOKS
                       │
                       ▼
               🔁 Take next book
                       │
                       ▼
              🗄️ Check Shelf 1
                       │
              ┌────────┴────────┐
              │                 │
          Available?          Used?
              │                 │
              ▼                 └──→ Next shelf
       Capacity >= book?
          │        │
         YES       NO
          │         │
          ▼         └──→ Next shelf
       ✅ Place
          │
          ▼
       🔒 Mark used
          │
          ▼
       🛑 break
          │
          ▼
      📚 Next book
          │
          ▼
     No shelf found?
          │
          ▼
    ❌ unplaced += 1
          │
          ▼
       🔁 Repeat
          │
          ▼
      🎯 Print count
⭐ Final Takeaway

The problem is essentially:

📚 Take book
    ↓
🗄️ Scan shelves left → right
    ↓
🔍 Find first unused shelf with capacity >= book
    ↓
✅ Place + mark shelf used
    ↓
🔁 Next book

If no shelf works:

❌ unplaced += 1
🚀 One-Line Memory Trick

Book order fixed → scan shelves left-to-right → first valid shelf → mark used → repeat.

The three lines you should recognize immediately in an exam are:

for book in books:
    for j in range(n):
        if not used[j] and shelves[j] >= book:

That combination represents the core ordered greedy placement + simulation pattern.