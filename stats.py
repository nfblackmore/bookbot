def get_num_words(book_text) -> int:
    return len(book_text.split())

def count_characters(book_text):
    counter = {}
    for char in book_text:
        if char.lower() in counter:
            counter[char.lower()] += 1
        else:
            counter[char.lower()] = 1
    return counter

def sort_counts(counts):
    counts_sorted = [{"char": i, "count": j} for i, j in counts.items()]
    counts_sorted.sort(reverse=True, key = lambda x: x["count"])
    return counts_sorted