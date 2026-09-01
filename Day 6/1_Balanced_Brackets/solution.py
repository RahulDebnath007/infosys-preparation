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
    bracket_map = {')': '(', '}': '{', ']': '['}

    for i, ch in enumerate(s):
        if ch in '({[':
            stack.append(Pair(ch, i + 1))
        elif ch in ')}]':
            if not stack or stack[-1].getKey() != bracket_map[ch]:
                print(i + 1)
                return
            stack.pop()

    print(0 if not stack else stack[-1].getValue())


if __name__ == "__main__":
    main()
