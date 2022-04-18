'''
앞뒤가 똑같은 단어나 문장으로 뒤집어도 같은 말이 되는 단어 또는 문장을 팰린드롬(Palindrome) 이라고 한다.
우리말로는 회문(回文) 이라 부르며 문장 중에서는 대표적으로 소주 만 병만 주소 같은 문장이 이에 해당한다.
이 문장은 뒤집어도 소주 만 병만 주소 가 된다.

대소문자 여부를 구분하지 않으며 영문자, 숫자 만을 대상으로 함

예1)
입력: A man, a plan, a canal: Panama
출력: true

예2)
입력: race a car
출력: false
'''
# list 를 이용한 해결
# class Solution:
#     def isPalindrome(self, s) -> bool:
#         strs = []
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False
#         return True


# Deque 를 이용한 해결
# import collections
# from typing import Deque
# class Solution:
#     def isPalindrome(self, s) -> bool:
#         # 자료형 데크로 선언
#         strs: Deque = collections.deque()
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False
#         return True


# 정규식과 슬라이싱을 이용한 해결
import re
class Solution:
    def isPalindrome(self, s) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


solution = Solution()
print(solution.isPalindrome('A man, a plan, a canal: Panama'))
print(solution.isPalindrome('race a car'))
