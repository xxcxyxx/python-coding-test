# 문제: K번째수
# 출처: 프로그래머스 알고리즘 고득점 Kit
# 유형: 정렬 / 리스트 슬라이싱
# 난이도: Level 1
#
# 핵심:
# 1. commands에서 i, j, k를 하나씩 꺼낸다.
# 2. array의 i번째부터 j번째까지 자른다.
# 3. 잘라낸 배열을 오름차순으로 정렬한다.
# 4. 정렬된 배열의 k번째 값을 answer에 추가한다.
#
# 주의:
# 문제의 순서는 1부터 시작하지만,
# 파이썬 리스트의 인덱스는 0부터 시작한다.
# 따라서 시작 위치와 k번째 위치에 각각 -1을 적용한다.


def solution(array, commands):
    answer = []

    for i, j, k in commands:
        sorted_array = sorted(array[i - 1:j])
        answer.append(sorted_array[k - 1])

    return answer


# 테스트
if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    print(solution(array, commands))  # [5, 6, 3]
