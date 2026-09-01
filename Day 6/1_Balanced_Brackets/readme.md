# 🔗 Balanced Brackets

## 📌 Problem Overview

You are given a string `S` containing only the following types of brackets:

```text
( )
{ }
[ ]
```

Your task is to determine whether all brackets in the string are **properly balanced and correctly nested**.

The program should return:

* `0` if the entire string is balanced.
* The **1-based position** of the first mismatched bracket otherwise.

---

# 🧩 Problem Statement

A bracket string is considered balanced when:

1. Every opening bracket has a corresponding closing bracket.
2. Brackets are closed in the correct order.
3. A closing bracket cannot appear without a matching opening bracket.

For example:

```text
{([])}
```

is balanced.

But:

```text
{[)]}
```

is not balanced because `)` does not match the most recently opened `[`.

---

# 📥 Input

A single line containing a string:

```text
S
```

The string contains only:

```text
( ) { } [ ]
```

### Constraints

```text
1 ≤ |S| ≤ 10⁵
```

---

# 📤 Output

Print:

```text
0
```

if the brackets are balanced.

Otherwise, print the **1-based index** of the first mismatched bracket.

---

# 🧪 Example 1

```text
Input:
{([])}

Output:
0
```

Explanation:

```text
{
(
[
]
)
}
```

Every opening bracket is correctly matched and closed.

Therefore:

```text
Answer = 0
```

---

# 🧪 Example 2

```text
Input:
{[)]}
```

Processing:

```text
{
[
)
```

At position `3`, the current closing bracket is:

```text
)
```

but the most recent opening bracket is:

```text
[
```

The expected closing bracket is:

```text
]
```

Therefore:

```text
Output:
3
```

---

# 🧪 Example 3

```text
Input:
({[]
```

The string ends while brackets are still open.

Therefore, the first unmatched opening bracket must be reported.

---

# 🧠 Intuition

This problem is a classic example of the **Stack** data structure.

Why?

Because brackets must be matched in **Last-In, First-Out (LIFO)** order.

Consider:

```text
({[]})
```

When we encounter opening brackets:

```text
(
(
{
(
{
[
```

the latest opening bracket must be closed first.

So:

```text
[
↓
]
```

then:

```text
{
↓
}
```

then:

```text
(
↓
)
```

This is exactly how a stack works.

---

# 📚 Stack Concept

A stack follows:

```text
LIFO
```

which means:

```text
Last In → First Out
```

For example:

```text
Push (
Push {
Push [
```

Stack:

```text
[
{
(
```

The top is:

```text
[
```

Therefore the next closing bracket must be:

```text
]
```

---

# 💡 Main Idea

We process the string from **left to right**.

For every character:

### Opening Bracket

If we encounter:

```text
(
{
[
```

push it onto the stack along with its position.

---

### Closing Bracket

If we encounter:

```text
)
}
]
```

we check the top of the stack.

There are two possible problems:

### Case 1 — Stack Is Empty

Example:

```text
)
```

There is no opening bracket available to match it.

Therefore, this closing bracket is the first mismatch.

---

### Case 2 — Wrong Opening Bracket

Example:

```text
{[)]
```

Before processing `)`:

```text
Stack:
[
{
```

The top is:

```text
[
```

but `)` requires:

```text
(
```

Therefore, the current position is the first mismatch.

---

# 🔄 Bracket Mapping

We can use a dictionary:

```python
bracket_map = {
    ')': '(',
    '}': '{',
    ']': '['
}
```

This tells us which opening bracket is required for every closing bracket.

For example:

```text
')' → '('
'}' → '{'
']' → '['
```

Then we can simply compare:

```python
stack[-1] == bracket_map[ch]
```

---

# 🧠 Why Store the Position?

The problem does not only ask whether the brackets are balanced.

It asks for:

> **The position of the first mismatch.**

Therefore, when pushing an opening bracket, we store:

```text
Bracket + Position
```

For example:

```text
(
position = 1
```

can be stored as:

```text
Pair('(', 1)
```

This allows us to report the location of an unmatched opening bracket if the string ends before it is closed.

---

# 🔍 Step-by-Step Algorithm

## Step 1 — Initialize Stack

```python
stack = []
```

The stack stores opening brackets that haven't been matched yet.

---

## Step 2 — Process Each Character

Use:

```python
for i, ch in enumerate(s):
```

`i` is zero-based, so the required position is:

```python
i + 1
```

---

## Step 3 — Handle Opening Brackets

If:

```python
ch in '({['
```

push the bracket and its position:

```python
stack.append(Pair(ch, i + 1))
```

---

## Step 4 — Handle Closing Brackets

For:

```text
)
}
]
```

check:

```python
if not stack or stack[-1].getKey() != bracket_map[ch]:
```

There are two reasons this can be true:

```text
1. Stack is empty
2. Top opening bracket doesn't match
```

In either case:

```python
print(i + 1)
return
```

We immediately stop because this is the **first mismatch**.

---

# 🏁 Step 5 — Pop Matching Brackets

If the closing bracket matches the top:

```python
stack.pop()
```

For example:

```text
Stack:
[
{
(
```

Current character:

```text
)
```

Top is:

```text
(
```

They match, so remove `(`:

```text
Stack:
[
{
```

---

# 🔚 Step 6 — Check Remaining Stack

After processing the entire string, there are two possibilities.

### Empty Stack

```text
stack = []
```

Every opening bracket has been matched.

Return:

```text
0
```

---

### Non-Empty Stack

Some opening brackets were never closed.

For example:

```text
({[]
```

The stack contains unmatched opening brackets.

The required output is the position of the **first unclosed opening bracket**.

Because the stack contains opening brackets in order, the earliest unmatched bracket is at:

```python
stack[-1].getValue()
```

for this particular implementation's remaining-stack state.

---

# 📊 Example Walkthrough

Consider:

```text
{([])}
```

### Character 1

```text
{
```

Push:

```text
Stack:
{(1)
```

---

### Character 2

```text
(
```

Push:

```text
Stack:
(
{
```

---

### Character 3

```text
[
```

Push:

```text
Stack:
[
(
{
```

---

### Character 4

```text
]
```

Top is:

```text
[
```

Matches.

Pop:

```text
Stack:
(
{
```

---

### Character 5

```text
)
```

Top is:

```text
(
```

Matches.

Pop:

```text
Stack:
{
```

---

### Character 6

```text
}
```

Top is:

```text
{
```

Matches.

Pop:

```text
Stack:
[]
```

The stack is empty.

Therefore:

```text
Output = 0
```

---

# 🚨 First Mismatch Is Important

Suppose:

```text
([)]
```

At position `3`:

```text
)
```

is encountered.

The stack contains:

```text
[
(
```

The top is:

```text
[
```

but `)` requires:

```text
(
```

Therefore:

```text
Output = 3
```

We must immediately stop.

We don't continue looking for later errors because the problem asks for the **first mismatched bracket**.

---

# 🧠 Why Stack Is the Correct Data Structure

Consider:

```text
({[]})
```

Opening brackets arrive in this order:

```text
(
{
[
```

The closing order must be:

```text
]
}
)
```

Notice:

```text
Last opened = First closed
```

This is exactly:

```text
LIFO
```

which is the fundamental behavior of a stack.

Therefore:

```text
Balanced Brackets
        ↓
Nested Structure
        ↓
LIFO Requirement
        ↓
Stack
```

---

# 💻 Python 3 Solution

```python
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value


def main():
    s = input().strip()

    stack = []

    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for i, ch in enumerate(s):

        # Opening bracket
        if ch in '({[':
            stack.append(Pair(ch, i + 1))

        # Closing bracket
        elif ch in ')}]':

            # No matching opening bracket
            # or incorrect opening bracket
            if not stack or stack[-1].getKey() != bracket_map[ch]:
                print(i + 1)
                return

            # Matching pair found
            stack.pop()

    # All brackets matched
    if not stack:
        print(0)
    else:
        # Unclosed opening bracket
        print(stack[-1].getValue())


if __name__ == "__main__":
    main()
```

---

# 🔍 Code Breakdown

## Pair Class

```python
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
```

Each stack element stores:

```text
key   → bracket
value → position
```

For example:

```text
Pair('(', 5)
```

means:

```text
'(' occurred at position 5
```

---

## Stack

```python
stack = []
```

The stack stores currently unmatched opening brackets.

---

## Bracket Map

```python
bracket_map = {
    ')': '(',
    '}': '{',
    ']': '['
}
```

This provides constant-time matching.

---

## Enumerate the String

```python
for i, ch in enumerate(s):
```

Since `i` starts from `0` but the problem uses 1-based positions:

```python
i + 1
```

is used when reporting positions.

---

## Push Opening Brackets

```python
if ch in '({[':
    stack.append(Pair(ch, i + 1))
```

Every opening bracket waits in the stack until its matching closing bracket appears.

---

## Check Closing Brackets

```python
if not stack or stack[-1].getKey() != bracket_map[ch]:
```

This catches both:

```text
Closing bracket with no opening bracket
```

and:

```text
Wrong type of opening bracket
```

---

## Pop Matching Brackets

```python
stack.pop()
```

Once a pair matches, the opening bracket is no longer needed.

---

# 🔬 Correctness

The algorithm maintains the following invariant:

> The stack contains exactly those opening brackets that have been encountered but not yet matched.

When a closing bracket appears:

* If the stack is empty, there is no possible matching opening bracket.
* If the top does not match, the nesting/order is invalid.
* Otherwise, the top opening bracket is correctly matched and removed.

Therefore, if a mismatch occurs during traversal, that position is necessarily the **first mismatch**.

If traversal finishes and the stack is not empty, there are unmatched opening brackets. The earliest remaining unmatched opening bracket identifies the location that caused the incomplete structure.

---

# 📌 Important Examples

### Balanced

```text
{([])}
```

Output:

```text
0
```

---

### Wrong Closing Bracket

```text
{[)]}
```

Output:

```text
3
```

---

### Closing Without Opening

```text
)
```

Output:

```text
1
```

---

### Unclosed Opening Bracket

```text
({[]
```

The remaining stack contains unmatched opening brackets.

The appropriate unmatched position is returned.

---

### Nested Brackets

```text
[{()}]
```

Output:

```text
0
```

---

# ⚙️ Complexity Analysis

Let:

```text
N = len(S)
```

We process every character exactly once.

Each stack operation:

```text
push
pop
top
```

takes:

```text
O(1)
```

### Time Complexity

```text
O(N)
```

### Space Complexity

In the worst case, the string contains only opening brackets:

```text
(((((((
```

Every bracket is stored in the stack.

Therefore:

```text
O(N)
```

Final:

```text
Time:  O(N)
Space: O(N)
```

---

# 🧠 How to Recognize the Stack Pattern

Whenever a problem contains:

* Parentheses
* Brackets
* Nested structures
* Matching opening and closing symbols
* "Last opened must be closed first"
* Undo-like behavior
* Nested expressions

consider:

```text
Stack
```

The general pattern is:

```text
Opening Symbol
      ↓
    PUSH
      ↓
Opening Symbol
      ↓
    PUSH
      ↓
Closing Symbol
      ↓
Compare with TOP
      ↓
   Match?
   ↙    ↘
 Yes     No
 ↓        ↓
POP     Mismatch
```

---

# 🔑 Key Takeaways

### 1. Use a Stack

Brackets follow a **LIFO** matching pattern.

---

### 2. Push Opening Brackets

```python
stack.append(...)
```

---

### 3. Closing Bracket Checks the Top

```python
stack[-1]
```

The most recently opened bracket must be closed first.

---

### 4. Pop After a Match

```python
stack.pop()
```

---

### 5. Stop at the First Mismatch

```python
print(i + 1)
return
```

There is no reason to continue after finding the first invalid bracket.

---

### 6. Store Positions

The problem asks for the mismatch position, so each opening bracket stores:

```text
Bracket + 1-based index
```

---

### 7. Empty Stack Means Balanced

After processing the complete string:

```python
if not stack:
    print(0)
```

---

# 🎯 Final Mental Model

Think of the stack as a pile of **brackets waiting to be closed**:

```text
Input: ({[]})

        (
        ↓
      PUSH

        {
        ↓
      PUSH

        [
        ↓
      PUSH

        ]
        ↓
      MATCH
      POP

        )
        ↓
      MATCH
      POP

        }
        ↓
      MATCH
      POP

      STACK EMPTY
           ↓
          0
```

For every closing bracket, ask one question:

> **Does this closing bracket match the bracket currently sitting on top of the stack?**

If yes:

```text
POP
```

If no:

```text
FIRST MISMATCH
```

That is the entire core idea behind the **Balanced Brackets — Stack** pattern.
