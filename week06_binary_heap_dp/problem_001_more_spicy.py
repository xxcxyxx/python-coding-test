# 문제: 더 맵게
# 출처: 프로그래머스
# 유형: Heap / Priority Queue
# 난이도: Level 2
#
# 문제 설명:
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해
# 가장 맵지 않은 음식 2개를 계속 섞는다.
#
# 섞은 음식의 스코빌 지수 =
# 가장 맵지 않은 음식 + 두 번째로 맵지 않은 음식 * 2
#
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 있으면 섞은 횟수를 반환하고,
# 불가능하면 -1을 반환한다.
#
# 풀이 접근:
# 1. 매번 가장 작은 값 2개가 필요하므로 최소 힙을 사용한다.
# 2. scoville 리스트를 heapq.heapify()로 힙 구조로 바꾼다.
# 3. 가장 작은 값 scoville[0]이 K보다 작으면 계속 섞는다.
# 4. 음식이 2개 미만이면 더 이상 섞을 수 없으므로 -1을 반환한다.
# 5. 가장 작은 값 2개를 꺼내 새 스코빌 지수를 만든다.
# 6. 새 값을 다시 힙에 넣고 횟수를 증가시킨다.

import heapq


def solution(scoville, K):
    answer = 0

    # 리스트를 최소 힙 구조로 변환
    heapq.heapify(scoville)

    # 가장 작은 값이 K 이상이면 모든 음식이 K 이상이라는 뜻
    while scoville[0] < K:
        # 음식이 1개만 남으면 더 이상 섞을 수 없음
        if len(scoville) < 2:
            return -1

        # 가장 맵지 않은 음식 2개 꺼내기
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        # 문제에서 주어진 공식대로 새 음식 만들기
        mixed = first + second * 2

        # 새 음식을 다시 힙에 넣기
        heapq.heappush(scoville, mixed)

        # 섞은 횟수 증가
        answer += 1

    return answer
