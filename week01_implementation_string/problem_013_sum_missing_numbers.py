"""
문제명: 없는 숫자 더하기
출처: Programmers
유형: Implementation / Array / Math
난이도: Level 1
상태: Solved
날짜: 2026-06-12

문제 요약:
- 0부터 9까지의 숫자 중 numbers에 없는 숫자들을 찾아 모두 더한다.
- numbers에는 0부터 9까지의 숫자 중 일부가 들어 있으며, 중복은 없다.

풀이 접근:
[방법 1] 완전탐색
1. 0부터 9까지 숫자를 하나씩 확인한다.
2. 해당 숫자가 numbers 안에 없으면 answer에 더한다.
3. 최종 합계를 반환한다.

[방법 2] 전체 합 활용
1. 0부터 9까지의 전체 합은 45이다.
2. numbers에 들어 있는 숫자들의 합을 구한다.
3. 45에서 sum(numbers)를 빼면 없는 숫자들의 합이 된다.

시간복잡도:
- 방법 1: O(10 * N), N은 numbers의 길이
- 방법 2: O(N)

배운 점:
- 리스트 안에 특정 값이 없는지 확인할 때는 `not in`을 사용할 수 있다.
- 범위가 고정된 숫자 집합에서는 전체 합에서 포함된 값의 합을 빼는 방식으로 더 간단하게 풀 수 있다.
"""


# 방법 1: 완전탐색
def solution_loop(numbers):
    answer = 0
    
    for i in range(10):
        if i not in numbers:
            answer += i
    
    return answer


# 방법 2: 전체 합 활용
def solution(numbers):
    return 45 - sum(numbers)
