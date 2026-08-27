def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

def largest_palindrome_less(N):
    for i in range(N-1, -1, -1):
        if is_palindrome(i):
            return i

def smallest_palindrome_greater(N):
    i = N + 1
    while True:
        if is_palindrome(i):
            return i
        i += 1

N = int(input())
while True:
    num1 = largest_palindrome_less(N)
    num2 = smallest_palindrome_greater(N)
    final_number = num1 + num2
    if is_palindrome(final_number):
        print(final_number)
        break
    N -= 1