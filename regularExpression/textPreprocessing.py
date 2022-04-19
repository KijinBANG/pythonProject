'''
다음 texts 변수의 텍스트를 <출력 결과>와 같이 전처리하시오.

<입력 예시>
    texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']

<출력 결과>
    ['afabasabag', 'abttaa', 'uysfsfaa']
'''

from re import findall


def textPreprocessing(list) -> list:
    result = []
    for temp in list:
        result.append(''.join(findall('[a-zA-Z]+', temp)).lower())
    return result


texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']
print(textPreprocessing(texts))
