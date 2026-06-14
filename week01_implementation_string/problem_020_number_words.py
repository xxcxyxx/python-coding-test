```python
"""
문제명: 숫자 문자열과 영단어
출처: Programmers
유형: Implementation / String / Replace
난이도: Level 1
상태: Solved
날짜: 2026-06-14

문제 요약:
- 숫자의 일부가 영단어로 바뀐 문자열 s가 주어진다.
- 영단어를 대응하는 숫자로 변환한 뒤 원래 정수를 반환한다.

풀이 접근:
1. 0부터 9까지의 영단어를 순서대로 리스트에 저장한다.
2. enumerate()를 사용해 숫자와 영단어를 함께 순회한다.
3. replace()를 사용해 문자열 속 영단어를 숫자 문자열로 치환한다.
4. 모든 변환이 끝난 문자열을 int로 변환해 반환한다.

시간복잡도:
- O(10 × N)
- 숫자 영단어 10개에 대해 문자열을 탐색한다.
- N은 문자열 s의 길이이다.

공간복잡도:
- O(N)
- replace() 과정에서 새로운 문자열이 생성된다.

배운 점:
- enumerate()를 사용하면 리스트의 인덱스와 값을 함께 가져올 수 있다.
- replace()의 두 번째 인자는 문자열이어야 하므로 str(num)을 사용한다.
- 반복문 안에서 return하면 첫 번째 반복 후 함수가 종료되므로,
  모든 치환이 끝난 뒤 return해야 한다.
"""

def solution(s):
    words = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    ]

    for num, word in enumerate(words):
        s = s.replace(word, str(num))

    return int(s)
```
