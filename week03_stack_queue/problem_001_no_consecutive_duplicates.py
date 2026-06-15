"""
문제명: 같은 숫자는 싫어

출처: Programmers

유형: Stack / Array
난이도: Level 1

상태: Solved
날짜: 2026-06-15

문제 요약:

- 숫자로 이루어진 배열 arr가 주어진다.
- 연속해서 나타나는 같은 숫자는 하나만 남긴다.
- 기존 숫자의 순서를 유지한 결과를 반환한다.

풀이 접근:

1. 결과를 저장할 answer 리스트를 만든다.
2. arr의 숫자를 앞에서부터 하나씩 확인한다.
3. answer가 비어 있으면 현재 숫자를 추가한다.
4. answer의 마지막 숫자와 현재 숫자가 다르면 추가한다.
5. 마지막 숫자와 같으면 연속된 중복이므로 추가하지 않는다.

시간복잡도:

- O(N)
- arr를 한 번 순회한다.

공간복잡도:

- O(N)
- 최악의 경우 모든 숫자가 달라 answer에 모두 저장된다.

배운 점:

- 리스트의 마지막 원소는 answer[-1]로 확인할 수 있다.
- answer가 비어 있을 때 answer[-1]을 사용하면 오류가 발생한다.
- 따라서 not answer 조건을 먼저 확인해야 한다.
- 연속된 중복만 제거하므로 set을 사용하면 안 된다.
- 리스트의 마지막 원소와 비교하는 방식으로 스택처럼 활용할 수 있다.
"""


def solution(arr):
    answer = []

    for number in arr:
        if not answer or answer[-1] != number:
            answer.append(number)

    return answer


if __name__ == "__main__":
    print(solution([1, 1, 3, 3, 0, 1, 1]))  # [1, 3, 0, 1]
    print(solution([4, 4, 4, 3, 3]))        # [4, 3]
