# 문제: 징검다리
# 출처: 프로그래머스
# 유형: Binary Search
# 난이도: Level 4
#
# 문제 설명:
# 출발점은 0, 도착점은 distance 위치에 있다.
# 그 사이에 바위들이 있고, 바위 중 n개를 제거할 수 있다.
#
# 바위를 n개 제거했을 때,
# 각 지점 사이 거리의 최솟값 중 가능한 최댓값을 구해야 한다.
#
# 풀이 접근:
# 1. 바위 위치를 오름차순으로 정렬한다.
# 2. 도착점 distance도 마지막 지점으로 추가한다.
# 3. 이분 탐색으로 가능한 최소 거리 후보 mid를 정한다.
# 4. 앞에서부터 바위를 확인하며, 이전에 남긴 지점과의 거리가 mid보다 작으면 제거한다.
# 5. 제거한 바위 수가 n개 이하이면 mid는 가능한 최소 거리이다.
# 6. 가능한 경우 더 큰 최소 거리를 찾기 위해 left를 늘린다.
# 7. 제거한 바위 수가 n개보다 많으면 mid가 너무 크므로 right를 줄인다.


def solution(distance, rocks, n):
    # 바위를 위치 순서대로 확인하기 위해 정렬
    rocks.sort()

    # 도착점도 마지막 지점처럼 확인하기 위해 추가
    rocks.append(distance)

    # 가능한 최소 거리의 범위
    left = 1
    right = distance

    answer = 0

    while left <= right:
        # 현재 확인할 최소 거리 후보
        mid = (left + right) // 2

        # 마지막으로 남긴 지점
        prev = 0

        # 제거한 바위 개수
        removed = 0

        # 각 바위와 도착점을 차례대로 확인
        for rock in rocks:
            # 이전에 남긴 지점과의 거리가 mid보다 작으면 제거
            if rock - prev < mid:
                removed += 1

            # 거리가 mid 이상이면 현재 지점을 남김
            else:
                prev = rock

        # n개 이하로 제거해서 mid 이상 간격을 만들 수 있으면 가능
        if removed <= n:
            answer = mid

            # 더 큰 최소 거리도 가능한지 확인
            left = mid + 1

        # 제거해야 하는 바위가 n개보다 많으면 불가능
        else:
            right = mid - 1

    return answer
