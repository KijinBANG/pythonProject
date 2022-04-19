'''
anagram 은 문자의 순서에 상관없이 구성이 같은 경우
단어 목록에서 애너그램 단위로 별도의 list를 만들어서 출력
대소문자 구분은 하지 않음

입력:
    ["eat", "tea", "tan", "ate", "nat", "bat"]

출력:
    [ ["ate","eat","tea"], ["nat","tan"], ["bat"] ]
'''
import collections


class Solution:
    def anagram(self, words):
        dict = collections.defaultdict(list)
        for word in words:
            dict[''.join(sorted(word))].append(word)
        return list(dict.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
print(solution.anagram(words))