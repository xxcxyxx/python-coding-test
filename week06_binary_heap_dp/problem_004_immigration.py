# 문제: 입국심사
# 출처: 프로그래머스
# 유형: Binary Search
# 난이도: Level 3
#
# 문제 설명:
# n명이 입국심사를 기다리고 있고,
# 각 심사관마다 한 명을 심사하는 데 걸리는 시간이 다르다.
#
# 모든 사람이 심사를 받는 데 걸리는 최소 시간을 구해야 한다.
#
# 풀이 접근:
# 1. 사람을 직접 배정하는 것이 아니라 시간을 기준으로 이분 탐색한다.
# 2. 가능한 최소 시간 left를 1로 둔다.
# 3. 가능한 최대 시간 right를 가장 느린 심사관이 모든 사람을 처리하는 시간으로 둔다.
# 4. mid분 동안 모든 심사관이 총 몇 명을 심사할 수 있는지 계산한다.
# 5. mid분 안에 n명 이상 심사할 수 있으면 가능한 시간이므로 answer에 저장한다.
# 6. 최소 시간을 찾아야 하므로 가능한 경우에는 right를 줄인다.
# 7. n명보다 적게 심사할 수 있으면 시간이 부족하므로 left를 늘린다.
# 8. 가능한 시간 중 최솟값을 반환한다.


def solution(n, times):
    # 가능한 최소 시간
    left = 1

    # 가능한 최대 시간
    # 가장 느린 심사관이 모든 사람을 심사하는 경우
    right = max(times) * n

    # 정답 후보
    answer = right

    # 이분 탐색
    while left <= right:
        # 현재 확인할 시간
        mid = (left + right) // 2

        # mid분 동안 심사할 수 있는 총 인원 수
        people = 0
        for time in times:
            people += mid // time

        # n명 이상 심사할 수 있으면 가능한 시간
        if people >= n:
            answer = mid

            # 더 짧은 시간도 가능한지 확인
            right = mid - 1

        # n명보다 적게 심사할 수 있으면 시간이 부족함
        else:
            left = mid + 1

    return answer
