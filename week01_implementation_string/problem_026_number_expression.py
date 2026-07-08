"""
문제명: 숫자의 표현
출처: Programmers
유형: Implementation / Brute Force
난이도: Level 2

문제 설명:
- 자연수 n을 연속된 자연수들의 합으로 표현하는 방법의 수를 구한다.
- 예를 들어 15는 다음과 같이 4가지로 표현할 수 있다.
  1 + 2 + 3 + 4 + 5 = 15
  4 + 5 + 6 = 15
  7 + 8 = 15
  15 = 15

풀이 접근:
1. 시작 숫자를 1부터 n까지 하나씩 정한다.
2. 시작 숫자부터 연속된 숫자들을 차례대로 더한다.
3. 합이 n과 같아지면 표현 방법을 1개 찾은 것이므로 answer를 증가시킨다.
4. 합이 n보다 커지면 더 이상 확인할 필요가 없으므로 반복을 종료한다.
5. 모든 시작 숫자를 확인한 뒤 answer를 반환한다.
"""


def solution(n):
    # n을 연속된 자연수의 합으로 표현할 수 있는 방법의 수
    answer = 0

    # 연속된 자연수의 시작 숫자를 1부터 n까지 하나씩 확인한다.
    for start in range(1, n + 1):
        # start부터 연속해서 더한 합을 저장한다.
        total = 0

        # start부터 n까지 숫자를 하나씩 더한다.
        for number in range(start, n + 1):
            # 현재 숫자를 total에 더한다.
            total += number

            # 연속된 숫자의 합이 n과 같으면 표현 방법을 찾은 것이다.
            if total == n:
                answer += 1

                # 이미 n을 만들었으므로 현재 시작 숫자에 대한 탐색을 끝낸다.
                break

            # 연속된 숫자의 합이 n보다 커지면 더 이상 n이 될 수 없다.
            if total > n:
                break

    # 찾은 표현 방법의 수를 반환한다.
    return answer
