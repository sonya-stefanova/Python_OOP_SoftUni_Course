class vowels:
    VOWELS = "AEIUYOaeiuyo"


    def __init__(self, text: str):
        self.text = text
        self.vowels_in_text = [el for el in self.text if el in self.VOWELS]


    def __iter__(self):
        return self


    def __next__(self):
        if not self.vowels_in_text:
            raise StopIteration

        return self.vowels_in_text.pop(0)

#
# # another decision:
#
# class vowels:
#     def __init__(self, string):
#         self.string = string
#         self.start = 0
#         self.end = len(string) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.start <= self.end:
#             curr_char = self.string[self.start]
#             self.start += 1
#
#             if curr_char in 'AEIOUYaeiouy':
#                 return curr_char
#         else:
#             raise StopIteration()
#

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)