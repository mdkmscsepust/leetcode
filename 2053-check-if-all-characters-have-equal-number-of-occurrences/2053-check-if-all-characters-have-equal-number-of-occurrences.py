class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_count =Counter(s)
        c = char_count[s[0]]
        return all(c == value for value in char_count.values())