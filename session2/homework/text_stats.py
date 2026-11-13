# Homework session 2 (easy): text statistics module


def word_count(text):
    return len(text.split())


def longest_word(text):
    return max(text.split(), key=len)


def char_frequency(text):
    freq = {}
    for char in text.lower():
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
    return freq


if __name__ == "__main__":
    s = "Python ist toll"
    print(word_count(s))
    print(longest_word(s))
    print(char_frequency("Abba"))
