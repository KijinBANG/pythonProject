'''
아래의 조건에 맞는 코드를 작성하시오.

<email 양식 처리조건>
    1. 아이디: 첫자는 영문 소문자 (단어 길이 4자 이상)
    2. 호스트 이름: 영문 소문자 시작 (단어 길이 3자 이상)
    3. 최상위 도메인: 영문 조문자 3자리 이하
    4. 정규표현식 기본 패턴: '메타문자@메타문자.메타문자'
    
<입력>
    email = """hong@12.com
        you2@naver.com
        12kang@hanmail.net
        kimjs@gmail.com"""

<출력>
    you2@naver.com
    kimjs@gmail.com
'''

from re import findall, match

email = """hong@12.com
        you2@naver.com
        12kang@hanmail.net
        kimjs@gmail.com"""

emails = email.split(sep='\n')

for e in emails:
    temp = e.strip()
    result = match('^[a-z][0-9a-zA-Z]{3,}@[a-z][0-9a-zA-Z]{2,}.[0-9a-zA-Z]{,3}', temp)
    if result:
        print(temp)
