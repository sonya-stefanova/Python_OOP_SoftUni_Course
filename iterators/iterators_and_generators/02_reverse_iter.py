class reverse_iter:

    def __init__(self, elements):
        self.elements = elements


    def __iter__(self):
        return self

    def __next__(self):
        if not self.elements:
            raise StopIteration

        return self.elements.pop()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)