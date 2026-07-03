"""
문제명: 최댓값과 최솟값
출처: Programmers
유형: String / List / Min Max
난이도: Level 2
상태: Solved
날짜: 2026-07-03

문제 요약:
- 공백으로 구분된 숫자들이 문자열 s로 주어진다.
- 문자열에 있는 숫자 중 최솟값과 최댓값을 찾는다.
- 결과를 "최솟값 최댓값" 형태의 문자열로 반환한다.

풀이 접근:
1. 문자열 s를 공백 기준으로 나눈다.
2. 나눈 문자열들을 정수로 변환한다.
3. min(), max()를 사용해 최솟값과 최댓값을 구한다.
4. 최솟값과 최댓값을 공백으로 이어 붙여 반환한다.

시간복잡도:
- O(N)

공간복잡도:
- O(N)

배운 점:
- split()을 사용하면 공백 기준으로 문자열을 나눌 수 있다.
- map(int, 리스트)를 사용하면 문자열 숫자를 정수로 변환할 수 있다.
- min(), max()는 리스트에서 최솟값과 최댓값을 구할 때 사용할 수 있다.
- f-string을 사용하면 숫자를 문자열 형식으로 쉽게 반환할 수 있다.
"""


def solution(s):
    numbers = list(map(int, s.split()))

    min_number = min(numbers)
    max_number = max(numbers)

    return f"{min_number} {max_number}"
