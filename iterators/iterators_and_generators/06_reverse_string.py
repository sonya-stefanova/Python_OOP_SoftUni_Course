def reverse_text(text: str):
    #---first variant----
    # text = list(text)
    # index = len(text) - 1
    # while index >= 0:
    #     yield text[index]
    #     index -= 1

    #---second variant----

    # idx = len(text) - 1
    # while idx >= 0:
    #     yield text[idx]
    #     idx -= 1

    #---third variant---better performance----
    for letter in text[::-1]:
        yield letter

for char in reverse_text("step"):
    print(char, end='')
