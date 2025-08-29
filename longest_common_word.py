from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Вставляє слово в трі."""
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end_of_word = True

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings: list[str]) -> str:
        """
        Знаходить найдовший спільний префікс для всіх слів.
        """
        if not strings:
            return ""

        # Вставляємо всі слова в трі
        for word in strings:
            self.insert(word)

        prefix = ""
        node = self.root
        
        # Проходимо по трі, поки вузол має лише одного нащадка
        while len(node.children) == 1 and not node.is_end_of_word:
            # Отримуємо єдиний символ-нащадок
            char = list(node.children.keys())[0]
            prefix += char
            node = node.children[char]
        
        return prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings1 = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings1) == "fl", f"Test 1 Failed: {trie.find_longest_common_word(strings1)}"
    
    trie2 = LongestCommonWord()
    strings2 = ["interspecies", "interstellar", "interstate"]
    assert trie2.find_longest_common_word(strings2) == "inters", f"Test 2 Failed: {trie2.find_longest_common_word(strings2)}"

    trie3 = LongestCommonWord()
    strings3 = ["dog", "racecar", "car"]
    assert trie3.find_longest_common_word(strings3) == "", f"Test 3 Failed: {trie3.find_longest_common_word(strings3)}"
    
    trie4 = LongestCommonWord()
    strings4 = []
    assert trie4.find_longest_common_word(strings4) == "", f"Test 4 Failed: {trie4.find_longest_common_word(strings4)}"
    
    trie5 = LongestCommonWord()
    strings5 = ["a"]
    assert trie5.find_longest_common_word(strings5) == "a", f"Test 5 Failed: {trie5.find_longest_common_word(strings5)}"

    trie6 = LongestCommonWord()
    strings6 = ["", "b", "c"]
    assert trie6.find_longest_common_word(strings6) == "", f"Test 6 Failed: {trie6.find_longest_common_word(strings6)}"
    
    print("Усі тести пройшли успішно! 🎉")