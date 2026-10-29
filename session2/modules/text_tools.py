# Modules: your own module
# The test at the bottom only runs when you start this file directly.


def count_words(text):
    return len(text.split())


def shout(text):
    return text.upper() + "!"


if __name__ == "__main__":
    print(count_words("a b c"))
