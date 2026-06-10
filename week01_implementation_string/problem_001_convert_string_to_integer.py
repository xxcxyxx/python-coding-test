"""
문제명: 문자열을 정수로 바꾸기
출처: Programmers
유형: Implementation / String / Type Conversion
난이도: Level 1
상태: Solved
날짜: 2026-06-10

문제 요약:
- 문자열 s를 정수로 변환하여 반환한다.
- s의 맨 앞에는 + 또는 - 부호가 올 수 있다.

풀이 접근:
1. Python의 int() 함수는 문자열 형태의 숫자를 정수로 변환한다.
2. +, - 부호도 자동으로 처리되므로 별도 조건문이 필요 없다.

시간복잡도:
- O(N), N은 문자열 s의 길이

배운 점:
- Python의 int()는 부호가 포함된 문자열도 바로 정수로 변환할 수 있다.
"""

def solution(s):
    return int(s)
