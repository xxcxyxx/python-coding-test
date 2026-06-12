"""
문제명: x만큼 간격이 있는 n개의 숫자
출처: Programmers
유형: Implementation / Array / Math
난이도: Level 1
상태: Solved
날짜: 2026-06-12

문제 요약:
- 정수 x와 자연수 n이 주어진다.
- x부터 시작해 x씩 증가하는 숫자를 n개 담은 리스트를 반환한다.

풀이 접근:
1. 1부터 n까지 반복한다.
2. 각 반복값 i에 x를 곱한다.
3. x * i 값을 리스트에 담아 반환한다.

시간복잡도:
- O(N), N은 입력값 n

배운 점:
- 등차수열 형태의 리스트는 range()와 리스트 컴프리헨션으로 간단하게 만들 수 있다.
"""

def solution(x, n):
    return [x * i for i in range(1, n + 1)]
