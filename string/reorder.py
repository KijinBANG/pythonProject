'''
제약조건
    데이터는 공백으로 구분되어 있다.
    로그의 가장 앞 부분은 식별자다.
    식별자는 순서에 영향을 끼치지 않지만 문자가 동일할 경우 식별자 순으로 한다.
    문자로 구성된 로그가 숫자 로그보다 앞에 온다.
    숫자 로그는 입력 순서대로

입력: ["dig1 8 1 5 l","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

출력: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 l","dig2 3 6"]
'''


class Solution:
    def reorderLogFiles(self, logs) -> [str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1], x.split()[0]))
        return letters + digits


solution = Solution()
logs = ["dig1 8 1 5 l", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(solution.reorderLogFiles(logs))