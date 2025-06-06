def longest_word_chain(words):
    word_set = set(words)
    dp = {}


    max_len = max(len(word) for word in words)

    buckets = [[] for _ in range(max_len + 1)]

    for word in words:
        buckets[len(word)].append(word)

    sorted_words = []
    for length in range(1, max_len + 1):
        sorted_words.extend(buckets[length])

    max_chain = 1
    for word in sorted_words:
        dp[word] = 1
        for i in range(len(word)):
            prev_word = word[:i] + word[i + 1:]
            if prev_word in dp:
                dp[word] = max(dp[word], dp[prev_word] + 1)
        max_chain = max(max_chain, dp[word])

    return max_chain





# def longest_word_chain(words):
#     word_set = set(words)
#     dp = {}
#
#
#     # words.sort(key=len, reverse=True)
#
#
#     max_len = max(len(word) for word in words)
#
#
#     buckets = [[] for _ in range(max_len + 1)]
#
#
#     for word in words:
#         buckets[len(word)].append(word)
#
#
#
#     max_chain = 1
#     for word in words:
#         dp[word] = max(dp.get(word, 1), 1)
#
#         for i in range(len(word)):
#             next_word = word[:i] + word[i + 1:]
#             if next_word in word_set:
#                 dp[next_word] = max(dp.get(next_word, 1), dp[word] + 1)
#                 max_chain = max(max_chain, dp[next_word])
#
#     return max_chain



# with open('wchain.in', 'r') as fin:
#     n = int(fin.readline())
#     words = [fin.readline().strip() for _ in range(n)]
#
# result = longest_word_chain(words)
#
#
# with open('wchain.out', 'w') as fout:
#     fout.write(str(result) + '\n')
