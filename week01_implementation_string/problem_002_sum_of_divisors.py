"""
문제명: 약수의 합
출처: Programmers
유형: Implementation / Math
난이도: Level 1
상태: Solved
날짜: 2026-06-10

문제 요약:
- 정수 n의 약수를 모두 더한 값을 반환한다.

풀이 접근:
1. 1부터 n까지 순회한다.
2. n을 i로 나누었을 때 나머지가 0이면 약수로 판단한다.
3. 약수들을 모두 더해 반환한다.

시간복잡도:
- O(N), N은 입력값 n

배운 점:
- 약수는 n % i == 0 조건으로 판별할 수 있다.
"""

def solution(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)
