class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.data:
            return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        result = ', '.join(x for x in reversed(self.data))
        return f'[{result}]'

s = Stack()
print(s.push("lemonada"))
s.push("bottle of water")
s.push("bottle of wine")
s.push("juice")
print(str(s))