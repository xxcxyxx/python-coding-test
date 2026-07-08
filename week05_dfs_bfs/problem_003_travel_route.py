"""
문제명: 여행경로
출처: Programmers
유형: DFS/BFS
난이도: Level 3

문제 설명:
- 주어진 항공권을 모두 사용하여 여행 경로를 만든다.
- 항상 "ICN" 공항에서 출발한다.
- tickets의 각 원소 [a, b]는 a 공항에서 b 공항으로 가는 항공권을 의미한다.
- 가능한 경로가 여러 개라면 알파벳 순서가 앞서는 경로를 반환한다.

풀이 접근:
1. 가능한 경로가 여러 개일 경우 알파벳 순서가 앞서는 경로를 찾아야 하므로 tickets를 정렬한다.
2. 항공권 사용 여부를 저장하는 visited 리스트를 만든다.
3. DFS를 사용해 현재 공항에서 출발할 수 있는 항공권을 하나씩 선택한다.
4. 모든 항공권을 사용하면 현재까지의 경로를 정답으로 저장한다.
5. 선택한 경로로 모든 항공권을 사용할 수 없다면 방문 처리를 되돌리는 백트래킹을 한다.
"""


def solution(tickets):
    # 알파벳 순서가 앞서는 경로를 먼저 탐색하기 위해 항공권을 정렬한다.
    tickets.sort()

    # 각 항공권을 사용했는지 확인하기 위한 리스트
    visited = [False] * len(tickets)

    # 최종 정답 경로를 저장할 변수
    answer = []

    # 현재 공항과 지금까지의 경로를 기준으로 DFS 탐색을 진행한다.
    def dfs(current_airport, path):
        # 함수 내부에서 바깥쪽 answer 값을 수정하기 위해 nonlocal을 사용한다.
        nonlocal answer

        # 경로의 길이가 항공권 개수 + 1이면 모든 항공권을 사용한 것이다.
        if len(path) == len(tickets) + 1:
            # 현재까지 만든 경로를 정답으로 저장한다.
            answer = path

            # 정답을 찾았다는 의미로 True를 반환한다.
            return True

        # 모든 항공권을 하나씩 확인한다.
        for i in range(len(tickets)):
            # i번째 항공권의 출발 공항과 도착 공항을 꺼낸다.
            start, end = tickets[i]

            # 아직 사용하지 않은 항공권이고, 현재 공항에서 출발하는 항공권이라면
            if not visited[i] and start == current_airport:
                # 해당 항공권을 사용 처리한다.
                visited[i] = True

                # 도착 공항을 경로에 추가하고 다음 DFS를 진행한다.
                if dfs(end, path + [end]):
                    # 정답 경로를 찾았다면 더 탐색하지 않고 True를 반환한다.
                    return True

                # 이 항공권을 사용한 경로로 정답을 만들 수 없다면 사용 처리를 취소한다.
                visited[i] = False

        # 현재 공항에서 더 이상 갈 수 없거나 정답 경로를 찾지 못한 경우
        return False

    # 항상 ICN 공항에서 출발한다.
    dfs("ICN", ["ICN"])

    # 완성된 여행 경로를 반환한다.
    return answer
