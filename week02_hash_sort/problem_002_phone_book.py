```python
"""
문제명: 전화번호 목록
출처: Programmers
유형: Hash / Set / String
난이도: Level 2
상태: Solved
날짜: 2026-06-14

문제 요약:
- 전화번호 배열 phone_book이 주어진다.
- 한 전화번호가 다른 전화번호의 접두사인 경우가 있으면 False,
  그렇지 않으면 True를 반환한다.

풀이 접근:
1. 전화번호의 빠른 존재 여부 확인을 위해 phone_book을 set으로 변환한다.
2. 각 전화번호를 하나씩 순회한다.
3. 첫 글자부터 마지막 글자 전까지 잘라 접두사를 만든다.
4. 만든 접두사가 phone_set에 존재하면 False를 반환한다.
5. 모든 전화번호를 확인해도 접두사가 없으면 True를 반환한다.

시간복잡도:
- O(N × L²)
- N은 전화번호의 개수, L은 전화번호의 최대 길이이다.
- 전화번호 길이가 최대 20이므로 충분히 효율적이다.

공간복잡도:
- O(N)
- 모든 전화번호를 set에 저장한다.

배운 점:
- set을 사용하면 특정 값의 존재 여부를 평균 O(1)에 확인할 수 있다.
- phone[:i]를 사용하면 문자열의 앞부분인 접두사를 만들 수 있다.
- 전화번호 전체까지 확인하면 자기 자신과 일치하므로
  range(1, len(phone))까지만 순회해야 한다.
"""

def solution(phone_book):
    phone_set = set(phone_book)

    for phone in phone_book:
        for i in range(1, len(phone)):
            prefix = phone[:i]

            if prefix in phone_set:
                return False

    return True
```
