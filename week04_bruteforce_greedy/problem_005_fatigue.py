"""
문제명: 피로도
출처: Programmers
유형: Brute Force / DFS / Backtracking
난이도: Level 2
상태: Solved
날짜: 2026-06-25

문제 요약:
- 현재 피로도 k와 던전 정보 dungeons가 주어진다.
- 각 던전은 [최소 필요 피로도, 소모 피로도]로 구성된다.
- 현재 피로도가 최소 필요 피로도 이상일 때만 해당 던전을 탐험할 수 있다.
- 던전을 탐험하면 소모 피로도만큼 현재 피로도가 감소한다.
- 탐험할 수 있는 던전의 최대 개수를 구해야 한다.

풀이 접근:
1. 각 던전을 방문했는지 visited 리스트로 관리한다.
2. DFS를 사용해 현재 피로도에서 갈 수 있는 던전을 하나씩 선택한다.
3. 던전을 방문하면 방문 처리 후 피로도를 소모하고 탐험 개수를 1 증가시킨다.
4. DFS가 끝나면 방문 처리를 되돌려 다른 순서도 탐색한다.
5. 모든 가능한 방문 순서를 확인하면서 최대 탐험 개수를 갱신한다.

시간복잡도:
- O(N!): 가능한 던전 방문 순서를 모두 탐색할 수 있기 때문이다.

공간복잡도:
- O(N): visited 리스트와 DFS 호출 스택을 사용하기 때문이다.

배운 점:
- DFS를 사용하면 가능한 선택지를 깊게 탐색할 수 있다.
- visited 리스트를 사용하면 같은 던전을 중복 방문하지 않도록 관리할 수 있다.
- visited[i] = False로 되돌리는 과정이 있어야 다른 방문 순서도 탐색할 수 있다.
- 백트래킹은 선택, 탐색, 되돌리기의 흐름으로 이해하면 된다.
"""

def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(current_fatigue, count):
        nonlocal answer
        answer = max(answer, count)

        for i in range(len(dungeons)):
            required, cost = dungeons[i]

            if not visited[i] and current_fatigue >= required:
                visited[i] = True
                dfs(current_fatigue - cost, count + 1)
                visited[i] = False

    dfs(k, 0)

    return answer
