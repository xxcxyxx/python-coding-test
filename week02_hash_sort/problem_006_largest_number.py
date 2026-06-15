"""
문제명: 가장 큰 수
출처: Programmers
유형: Sort / Lambda / String
난이도: Level 2

상태: Solved
날짜: 2026-06-15

문제 요약:
- 숫자들의 순서를 재배치하여 만들 수 있는 가장 큰 수를 구한다.
- 결과가 매우 클 수 있으므로 문자열로 반환한다.

풀이 접근:
1. 모든 숫자를 문자열로 변환한다.
2. 각 문자열을 4번 반복한 값을 기준으로 내림차순 정렬한다.
3. 정렬된 문자열들을 하나로 이어 붙인다.
4. 정렬 후 첫 번째 값이 '0'이면 모든 값이 0이므로 '0'을 반환한다.

시간복잡도:
- O(N log N)

배운 점:
- 숫자를 이어 붙여 비교할 때는 문자열로 변환한다.
- 원소가 최대 1,000이므로 최대 4자리이며 x * 4를 정렬 기준으로 사용한다.
- 매우 긴 문자열은 int()로 변환하면 오류가 발생할 수 있다.
- 모든 값이 0인지 확인할 때 정렬된 첫 번째 값을 사용할 수 있다.
"""


def solution(numbers):
    numbers = list(map(str, numbers))

    sorted_numbers = sorted(
        numbers,
        key=lambda x: x * 4,
        reverse=True
    )

    if sorted_numbers[0] == '0':
        return '0'

    return ''.join(sorted_numbers)


if __name__ == "__main__":
    print(solution([6, 10, 2]))         # "6210"
    print(solution([3, 30, 34, 5, 9]))  # "9534330"
    print(solution([0, 0, 0]))           # "0"
