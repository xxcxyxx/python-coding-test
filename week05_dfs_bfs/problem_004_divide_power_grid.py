"""
문제명: 전력망을 둘로 나누기
출처: Programmers
유형: 완전탐색 / BFS / 그래프
난이도: Level 2

상태: Solved
날짜: 2026-07-14

문제 요약:
- n개의 송전탑이 전선을 통해 트리 형태로 연결되어 있다.
- 전선 하나를 끊어 전력망을 두 개로 나눈다.
- 두 전력망의 송전탑 개수 차이가 가장 작아지도록 해야 한다.

풀이 접근:
1. 모든 전선을 하나씩 끊어본다.
2. 끊은 전선을 제외하고 그래프를 만든다.
3. 1번 송전탑부터 BFS를 진행한다.
4. 1번 송전탑과 연결된 송전탑의 개수를 센다.
5. 다른 전력망의 송전탑 개수는 전체 개수에서 빼서 구한다.
6. 두 전력망의 송전탑 개수 차이 중 최솟값을 반환한다.
"""

from collections import deque


def solution(n, wires):
    # 두 전력망의 송전탑 개수 차이를 저장한다.
    answer = n

    # 전선을 하나씩 끊어본다.
    for cut in range(len(wires)):

        # 송전탑의 연결 관계를 저장할 그래프를 만든다.
        graph = [[] for _ in range(n + 1)]

        # 끊기로 선택한 전선을 제외하고 그래프를 만든다.
        for index, (start, end) in enumerate(wires):

            # 현재 전선이 끊기로 한 전선이라면 건너뛴다.
            if index == cut:
                continue

            # 전선은 양방향으로 연결되어 있다.
            graph[start].append(end)
            graph[end].append(start)

        # 각 송전탑의 방문 여부를 저장한다.
        visited = [False] * (n + 1)

        # 1번 송전탑부터 BFS를 시작한다.
        queue = deque([1])
        visited[1] = True

        # 1번 송전탑을 이미 방문했으므로 1부터 시작한다.
        count = 1

        # 큐가 빌 때까지 연결된 송전탑을 탐색한다.
        while queue:

            # 큐의 가장 앞에 있는 송전탑을 꺼낸다.
            current = queue.popleft()

            # 현재 송전탑과 연결된 송전탑을 확인한다.
            for next_node in graph[current]:

                # 아직 방문하지 않은 송전탑이라면 방문한다.
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    count += 1

        # 한쪽 전력망의 송전탑 개수는 count이다.
        # 다른 쪽 전력망의 송전탑 개수는 n - count이다.
        difference = abs(count - (n - count))

        # 지금까지 계산한 차이 중 가장 작은 값을 저장한다.
        answer = min(answer, difference)

    return answer
