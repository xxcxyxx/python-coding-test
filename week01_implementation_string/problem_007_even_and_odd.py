"""
문제명: 짝수와 홀수
출처: Programmers
유형: Implementation / Math / Conditional
난이도: Level 1
상태: Solved
날짜: 2026-06-12

문제 요약:
- 정수 num이 짝수이면 "Even"을 반환한다.
- 정수 num이 홀수이면 "Odd"를 반환한다.

풀이 접근:
1. num을 2로 나눈 나머지를 확인한다.
2. 나머지가 0이면 짝수이므로 "Even"을 반환한다.
3. 나머지가 0이 아니면 홀수이므로 "Odd"를 반환한다.

시간복잡도:
- O(1)

배운 점:
- 짝수와 홀수는 num % 2 결과로 판별할 수 있다.
- 0 % 2 == 0이므로 0은 짝수로 처리된다.
"""

def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
