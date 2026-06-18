# 문제: 프로세스
# 유형: 큐 / 시뮬레이션
# 핵심:
# 1. enumerate()를 사용해 각 프로세스의 원래 위치와 우선순위를 함께 저장한다.
# 2. 큐의 가장 앞 프로세스를 꺼낸다.
# 3. 남은 큐에 더 높은 우선순위가 있으면 현재 프로세스를 뒤로 보낸다.
# 4. 더 높은 우선순위가 없으면 프로세스를 실행하고 실행 순서를 증가시킨다.
# 5. 실행한 프로세스의 원래 위치가 location과 같으면 실행 순서를 반환한다.
# 시간복잡도: O(N²)
# 공간복잡도: O(N)

from collections import deque


def solution(priorities, location):
    # (원래 위치, 우선순위) 형태로 큐에 저장
    queue = deque(enumerate(priorities))

    # 실제로 실행된 프로세스의 순서
    order = 0

    while queue:
        # 큐의 가장 앞 프로세스 꺼내기
        current_location, current_priority = queue.popleft()

        # 남은 프로세스 중 더 높은 우선순위가 있는지 확인
        if any(
            current_priority < priority
            for _, priority in queue
        ):
            # 더 높은 우선순위가 있으면 현재 프로세스를 뒤로 이동
            queue.append((current_location, current_priority))

        else:
            # 더 높은 우선순위가 없으면 현재 프로세스 실행
            order += 1

            # 실행한 프로세스가 찾고 있던 프로세스라면 순서 반환
            if current_location == location:
                return order


# 테스트
print(solution([2, 1, 3, 2], 2))        # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
