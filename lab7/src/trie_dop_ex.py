class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, phrase: str):
        node = self.root
        for char in phrase:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def contains_in_text(self, text: str):
        count = 0
        text_length = len(text)
        for i in range(text_length):
            node = self.root
            j = i
            while j < text_length and text[j] in node.children:
                node = node.children[text[j]]
                j += 1
                if node.is_end_of_word:
                    count += 1
        return count


def load_phrases(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip().lower() for line in file if line.strip()]


def load_posts(filename):
    users_posts = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if ':' in line:
                user, post = line.strip().split(':', 1)
                users_posts[user.strip()] = post.strip().lower()
    return users_posts


def analyze_users(trie, users_posts):
    results = {}
    for user, post in users_posts.items():
        total_words = len(post.split())
        matches = trie.contains_in_text(post)
        match_percentage = (matches / total_words) * 100 if total_words > 0 else 0
        results[user] = round(match_percentage, 2)
    return results


phrases = load_phrases('criminal_phrases.txt')
trie = Trie()
for phrase in phrases:
    trie.insert(phrase)

users_posts = load_posts('users_posts.txt')

results = analyze_users(trie, users_posts)

for user, percentage in results.items():
    print(f"{user}: Ймовірність бути злодієм — {percentage}%")
