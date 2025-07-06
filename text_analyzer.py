import re
from collections import Counter


class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text

    def word_count(self) -> int:
        words = re.findall(r'\w+', self.text.lower())
        return len(words)

    def unique_words(self) -> set:
        words = re.findall(r'\w+', self.text.lower())
        return set(words)

    def most_common_word(self) -> str:
        words = re.findall(r'\w+', self.text.lower())
        if not words:
            return ""
        return Counter(words).most_common(1)[0][0]

    def replace_word(self, old: str, new: str) -> str:
        return re.sub(rf'\b{old}\b', new, self.text, flags=re.IGNORECASE)