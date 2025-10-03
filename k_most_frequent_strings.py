# Find the k most frequently occurring strings in an array, and return them sorted by frequency in descending order. If two strings have the same frequency, sort them in lexicographical order.
from typing import List
from collections import Counter

def k_most_frequent_strings(strs: List[str], k: int) -> List[str]:
    freq = Counter(strs)
    # Sort: first by (-count), then lexicographically
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return [word for word, _ in sorted_items[:k]]
