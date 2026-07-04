# 문제: 이중우선순위큐
# 출처: 프로그래머스
# 유형: Heap / Priority Queue
# 난이도: Level 3
#
# 문제 설명:
# 이중 우선순위 큐는 숫자를 삽입하고,
# 최댓값 또는 최솟값을 삭제할 수 있는 자료구조이다.
#
# 명령어:
# I 숫자  : 숫자 삽입
# D 1     : 최댓값 삭제
# D -1    : 최솟값 삭제
#
# 모든 연산을 처리한 뒤 큐가 비어 있으면 [0, 0],
# 비어 있지 않으면 [최댓값, 최솟값]을 반환한다.
#
# 풀이 접근:
# 1. heapq를 사용해 최소 힙을 관리한다.
# 2. I 명령어는 heappush()로 숫자를 삽입한다.
# 3. D -1 명령어는 heappop()으로 최솟값을 삭제한다.
# 4. D 1 명령어는 max()로 최댓값을 찾고 remove()로 삭제한다.
# 5. remove() 후에는 힙 구조가 깨질 수 있으므로 heapify()를 다시 실행한다.
# 6. 빈 큐에서 삭제 명령이 들어오면 무시한다.
# 7. 마지막에 heap이 비어 있으면 [0, 0], 아니면 [max(heap), heap[0]]을 반환한다.

import heapq


def solution(operations):
    heap = []

    for operation in operations:
        command, number = operation.split()
        number = int(number)

        # 숫자 삽입
        if command == "I":
            heapq.heappush(heap, number)

        # 숫자 삭제
        elif command == "D":
            # 빈 큐에서 삭제 명령이 들어오면 무시
            if not heap:
                continue

            # 최솟값 삭제
            if number == -1:
                heapq.heappop(heap)

            # 최댓값 삭제
            elif number == 1:
                max_value = max(heap)
                heap.remove(max_value)
                heapq.heapify(heap)

    # 모든 연산 후 큐가 비어 있으면 [0, 0]
    if not heap:
        return [0, 0]

    # heap[0]은 최소 힙의 최솟값
    return [max(heap), heap[0]]
