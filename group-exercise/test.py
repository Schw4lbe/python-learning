uppercase_letters: list = ["A", "B", "C", "D"]
letters_count: list = []
new_letters_count: list = []
test_shift: int = 4
test_string: str = "A"


def get_letters_count(list):
    for letter in enumerate(list):
        letters_count.append(letter)
    # print(letters_count)


def get_new_index():
    for tuple in letters_count:
        new_index = tuple[0] + test_shift
        if new_index >= len(uppercase_letters):
            new_index -= len(uppercase_letters)

        print(uppercase_letters[new_index])


get_letters_count(uppercase_letters)
get_new_index()


# myTuple = ("John", "Peter", "Vicky")

# x = "#".join(myTuple)

# print(x)
