"""
문제명: 타겟 넘버
출처: Programmers
유형: DFS / Brute Force
난이도: Level 2
상태: Solved
날짜: 2026-06-26

문제 요약:
- 정수 배열 numbers와 목표값 target이 주어진다.
- numbers의 각 숫자 앞에 + 또는 -를 붙여 계산할 수 있다.
- 모든 숫자를 사용해서 target을 만들 수 있는 경우의 수를 구해야 한다.

풀이 접근:
1. DFS를 사용해 각 숫자마다 더하는 경우와 빼는 경우를 모두 탐색한다.
2. index는 현재 확인 중인 숫자의 위치를 의미한다.
3. total은 지금까지 계산한 합계를 의미한다.
4. 현재 숫자를 더하는 경우와 빼는 경우로 재귀 호출한다.
5. 모든 숫자를 사용했을 때 total이 target과 같으면 answer를 1 증가시킨다.

시간복잡도:
- O(2^N): 각 숫자마다 + 또는 - 두 가지 선택지가 있기 때문이다.

공간복잡도:
- O(N): DFS 재귀 호출 스택이 numbers의 길이만큼 쌓일 수 있기 때문이다.

배운 점:
- DFS를 사용하면 모든 경우의 수를 깊게 탐색할 수 있다.
- 각 단계에서 선택지가 2개일 때는 재귀 호출을 2번 사용해 모든 조합을 만들 수 있다.
- 종료 조건을 먼저 작성하면 재귀 흐름을 이해하기 쉽다.
- nonlocal을 사용하면 내부 함수에서 바깥 함수의 answer 값을 수정할 수 있다.
"""

def solution(numbers, target):
    answer = 0

    def dfs(index, total):
        nonlocal answer

        if index == len(numbers):
            if total == target:
                answer += 1
            return

        dfs(index + 1, total + numbers[index])
        dfs(index + 1, total - numbers[index])

    dfs(0, 0)

    return answer
