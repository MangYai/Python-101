def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    merged = []
    for word_list in words:
        for word in word_list:
            merged.append(word)

    best_len = 0
    best_seqs = []
    left = 0
    seen = []

    for right in range(len(merged)):
        while merged[right] in seen:
            seen.remove(merged[left])
            left = left + 1
        seen.append(merged[right])

        current_len = right - left +1
        if current_len > best_len:
            best_len = current_len
            current_seq = []
            for k in range(left, right + 1):
                current_seq.append(merged[k])
            best_seqs = [current_seq]
        elif current_len == best_len:
            current_seq = []
            for k in range(left, right + 1):
                current_seq.append(merged[k])
            best_seqs.append(current_seq)

    return best_len, best_seqs

words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
# ผลลัพธ์: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])

words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2))
# ผลลัพธ์: (4, [['mouse', 'cat', 'bird', 'dog']])
