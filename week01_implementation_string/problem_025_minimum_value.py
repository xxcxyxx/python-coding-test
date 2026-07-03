"""
문제명: 최솟값 만들기
출처: Programmers
유형: Sort / Greedy
난이도: Level 2
상태: Solved
날짜: 2026-07-03

문제 요약:
- 길이가 같은 배열 A, B가 주어진다.
- A와 B에서 각각 하나씩 숫자를 뽑아 곱한 값을 누적한다.
- 한 번 뽑은 숫자는 다시 뽑을 수 없다.
- 누적합이 최소가 되도록 만든 값을 반환한다.

풀이 접근:
1. A는 오름차순으로 정렬한다.
2. B는 내림차순으로 정렬한다.
3. 작은 수와 큰 수를 서로 곱해 누적합을 최소로 만든다.

시간복잡도:
- O(N log N)

공간복잡도:
- O(N)

배운 점:
- 곱의 합을 최소로 만들려면 작은 값과 큰 값을 짝지어야 한다.
- sort()는 리스트를 직접 정렬한다.
- reverse=True를 사용하면 내림차순 정렬할 수 있다.
"""


def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    answer = 0

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer
