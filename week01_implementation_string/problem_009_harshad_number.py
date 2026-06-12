"""
문제명: 하샤드 수
출처: Programmers
유형: Implementation / String / Math
난이도: Level 1
상태: Solved
날짜: 2026-06-12

문제 요약:
- 양의 정수 x가 하샤드 수인지 판별한다.
- 하샤드 수는 x가 자신의 자릿수 합으로 나누어떨어지는 수이다.

풀이 접근:
1. x를 문자열로 변환한다.
2. 각 자릿수를 정수로 변환해 모두 더한다.
3. x가 자릿수 합으로 나누어떨어지는지 확인한다.
4. 나누어떨어지면 True, 아니면 False를 반환한다.

시간복잡도:
- O(K), K는 x의 자릿수

배운 점:
- 자릿수 합은 sum(int(num) for num in str(x))로 구할 수 있다.
- 조건식 자체가 True/False를 반환하므로 if문 없이 바로 return할 수 있다.
"""

def solution(x):
    digit_sum = sum(int(num) for num in str(x))
    return x % digit_sum == 0
