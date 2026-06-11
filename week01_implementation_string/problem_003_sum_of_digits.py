"""
문제명: 자릿수 더하기
출처: Programmers
유형: Implementation / String / Math
난이도: Level 1
상태: Solved
날짜: 2026-06-11

문제 요약:
- 자연수 N의 각 자릿수를 더한 값을 반환한다.

풀이 접근:
1. 숫자 N을 문자열로 변환한다.
2. 문자열을 한 글자씩 순회한다.
3. 각 문자를 정수로 변환한 뒤 모두 더한다.

시간복잡도:
- O(K), K는 N의 자릿수

배운 점:
- 숫자의 각 자릿수를 다룰 때는 문자열로 변환하면 쉽게 순회할 수 있다.
"""

def solution(N):
    return sum(int(num) for num in str(N))
