
def swapcase_decorator(gen):
    def inner_gen(*args, **kwargs):
        value = gen(*args)
        value = str(value)
        value = value.swapcase()
        yield value


    return inner_gen


def check_duplicate(word):
    digit_list = []
    word = str(word)
    for i in word:
        if i not in digit_list:
            digit_list.append(i)
        else:
            return False
    return True


@swapcase_decorator
def duplicate_words_gen(file_path):
    file = open(file_path)
    content = file.read()
    words_list = content.split()
    for word in words_list:
        if check_duplicate(word):
            yield word


if __name__ == '__main__':
    for i in duplicate_words_gen("hello.txt"):
        print(i)

