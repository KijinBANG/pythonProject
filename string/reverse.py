'''
앞뒤가 똑같은 단어나 문장으로 뒤집어도 같은 말이 되는 단어 또는 문장을 팰린드롬(Palindrome) 이라고 한다.
우리말로는 회문(回文) 이라 부르며 문장 중에서는 대표적으로 소주 만 병만 주소 같은 문장이 이에 해당한다. 이 문장은 뒤집어도 소주 만 병만 주소 가 된다.

대소문자 여부를 구분하지 않으며 영문자, 숫자 만을 대상으로 함

예1)
입력: ["h", "e", "l", "l", "o"]
출력: ["o", "l", "l", "e", "h"]

예2)
입력: ["H", "a", "n", "n", "a", "h"]
출력: ["h", "a", "n", "n", "a", "H"]
'''


# reverse 함수를 이용한 방법
# class Solution:
#     def reverse(self, s) -> None:
#         s.reverse()
#         print(s)


# left 와 right 라는 두 인덱스를 이용하는 방법
class Solution:
    def reverse(self, s) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)


s1 = ["h", "e", "l", "l", "o"]
s2 = ["H", "a", "n", "n", "a", "h"]

solution = Solution()
solution.reverse(s1)
solution.reverse(s2)
