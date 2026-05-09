from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count_word = {}
    for ch in word:
        if ch in count_word:
            count_word[ch] = count_word[ch]+1
            continue
        count_word[ch] = 1
    return count_word




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
