class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.idx == self.number:
            raise StopIteration

        returning_item = self.sequence[self.idx % len(self.sequence)]
        self.idx += 1
        return returning_item

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

