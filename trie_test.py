# trie.py
# Клас Node для представлення вузла в префіксному дереві.
# Кожен вузол містить словник дочірніх вузлів та прапорець,
# що вказує, чи є він кінцем слова.
class _Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.count = 0  # Додатковий лічильник для ефективного підрахунку

# Базовий клас Trie
class Trie:
    def __init__(self):
        # Кореневий вузол дерева
        self._root = _Node()

    def put(self, word: str, value):
        """
        Вставляє слово в префіксне дерево.
        """
        if not isinstance(word, str):
            raise TypeError("Слово для вставки має бути рядком.")
        
        current_node = self._root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = _Node()
            current_node = current_node.children[char]
            current_node.count += 1
        current_node.is_end_of_word = True

    def _get_node(self, sequence: str) -> _Node | None:
        """
        Допоміжний метод для отримання вузла, що відповідає кінцю заданої послідовності.
        """
        current_node = self._root
        for char in sequence:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node

# Клас Homework, що успадковує клас Trie та розширює його функціонал
class Homework(Trie):
    def __init__(self):
        # Ініціалізація основного префіксного дерева
        super().__init__()
        # Ініціалізація допоміжного зворотного префіксного дерева для суфіксів
        self._reverse_trie = Trie()

    def put(self, word: str, value):
        """
        Перевизначений метод put, який вставляє слово
        як в основне, так і в зворотне префіксне дерево.
        """
        super().put(word, value)
        self._reverse_trie.put(word[::-1], value)

    def count_words_with_suffix(self, pattern: str) -> int:
        """
        Підраховує кількість слів, що закінчуються на заданий суфікс.
        Використовує зворотне префіксне дерево для ефективності.
        """
        if not isinstance(pattern, str):
            raise TypeError("Параметр 'pattern' має бути рядком.")

        # Обертаємо шаблон, щоб знайти його як префікс у зворотному дереві
        reversed_pattern = pattern[::-1]
        
        # Отримуємо вузол, що відповідає оберненому шаблону
        node = self._reverse_trie._get_node(reversed_pattern)
        
        # Якщо вузол існує, повертаємо його лічильник, інакше - 0
        return node.count if node else 0

    def has_prefix(self, prefix: str) -> bool:
        """
        Перевіряє наявність хоча б одного слова із заданим префіксом.
        """
        if not isinstance(prefix, str):
            raise TypeError("Параметр 'prefix' має бути рядком.")
            
        # Отримуємо вузол, що відповідає префіксу
        node = self._get_node(prefix)

        # Повертаємо True, якщо вузол існує, інакше - False
        return node is not None


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    print("--- Перевірка суфіксів ---")
    assert trie.count_words_with_suffix("e") == 1  # apple
    print("Суфікс 'e': Passed")
    assert trie.count_words_with_suffix("ion") == 1  # application
    print("Суфікс 'ion': Passed")
    assert trie.count_words_with_suffix("a") == 1  # banana
    print("Суфікс 'a': Passed")
    assert trie.count_words_with_suffix("at") == 1  # cat
    print("Суфікс 'at': Passed")
    assert trie.count_words_with_suffix("nothing") == 0
    print("Суфікс 'nothing': Passed")

    # Перевірка наявності префікса
    print("\n--- Перевірка префіксів ---")
    assert trie.has_prefix("app") == True  # apple, application
    print("Префікс 'app': Passed")
    assert trie.has_prefix("bat") == False
    print("Префікс 'bat': Passed")
    assert trie.has_prefix("ban") == True  # banana
    print("Префікс 'ban': Passed")
    assert trie.has_prefix("ca") == True  # cat
    print("Префікс 'ca': Passed")
    assert trie.has_prefix("something") == False
    print("Префікс 'something': Passed")
    
    # Перевірка обробки некоректних даних
    print("\n--- Перевірка обробки помилок ---")
    try:
        trie.count_words_with_suffix(123)
    except TypeError as e:
        print(f"Очікувана помилка: {e}")
    
    try:
        trie.has_prefix(["list"])
    except TypeError as e:
        print(f"Очікувана помилка: {e}")

    print("\nУсі тести пройдено!")
