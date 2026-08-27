def is_palindrome(num):
    return str(num) == str(num)[::-1]

def reverse_number(num):
    return int(str(num)[::-1])

def find_palindrome(num):
    iterations = 0
    while not is_palindrome(num) and iterations < 1000:
        num+= reverse_number(num)
        iterations +=1
    return num

num = int(input().strip())
print(find_palindrome(num))    