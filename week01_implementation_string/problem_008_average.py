"""
문제명: 평균 구하기
출처: Programmers
유형: Implementation / Array / Math
난이도: Level 1
상태: Solved
날짜: 2026-06-12

문제 요약:
- 정수를 담고 있는 배열 arr의 평균값을 반환한다.

풀이 접근:
1. sum(arr)를 사용해 배열 원소의 합을 구한다.
2. len(arr)를 사용해 배열의 길이를 구한다.
3. 합계를 길이로 나누어 평균값을 반환한다.

시간복잡도:
- O(N), N은 배열 arr의 길이

배운 점:
- 배열의 평균은 sum(arr) / len(arr)로 간단하게 구할 수 있다.
"""

def solution(arr):
    return sum(arr) / len(arr)
