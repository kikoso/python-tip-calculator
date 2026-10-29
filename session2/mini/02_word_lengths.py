# Mini exercise 2: word lengths with a dictionary comprehension


def word_lengths(sentence: str) -> dict:
    """Map each word to its length."""
    return {w: len(w) for w in sentence.split()}


lengths = word_lengths("Python ist toll")
print(lengths)

longest = max(lengths, key=lengths.get)
print(longest)
