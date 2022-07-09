import math
import string
from typing import List


def get_candidates(word):
    result = []

    for i in range(len(word)):
        for letter in string.ascii_lowercase:
            prev = word[:i]
            post = word[i + 1:]
            next_word = prev + letter + post
            result.append(next_word)
    return result


class Solution:
    def findLadders(self, start: str, end: str, word_list: List[str]) -> List[List[str]]:

        words = set(word_list + [start])
        paths = []
        shortest_path_length = math.inf
        visited = set()
        accum = []

        def backtrack(word):
            nonlocal shortest_path_length, paths, words, visited, accum
            if word == end:
                path = accum[:] + [word]
                if len(path) == shortest_path_length:
                    paths.append(path)
                elif len(path) < shortest_path_length:
                    paths = [path]
                    shortest_path_length = len(path)
                return

            if word not in words or word in visited or (paths and len(paths[0]) < len(accum)):
                return

            visited.add(word)
            accum.append(word)

            for next_word in get_candidates(word):
                backtrack(next_word)

            accum.pop()
            visited.discard(word)

        backtrack(start)

        return paths

s = Solution()

print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))