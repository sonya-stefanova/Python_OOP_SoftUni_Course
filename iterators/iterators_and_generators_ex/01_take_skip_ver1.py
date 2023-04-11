class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.counter = 0
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.count:
            temp = self.current
            self.counter += 1
            self.current+=self.step
            return temp
        raise StopIteration

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
