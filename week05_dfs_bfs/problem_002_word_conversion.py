"""
문제명: 단어 변환
출처: Programmers
유형: DFS/BFS
난이도: Level 3

문제 설명:
- begin 단어를 target 단어로 변환해야 한다.
- 한 번에 한 개의 알파벳만 바꿀 수 있다.
- words에 있는 단어로만 변환할 수 있다.
- 최소 몇 단계의 과정을 거쳐 변환할 수 있는지 구한다.
- 변환할 수 없는 경우 0을 반환한다.

풀이 접근:
1. target이 words 안에 없으면 변환할 수 없으므로 0을 반환한다.
2. begin 단어와 변환 횟수 0을 큐에 넣는다.
3. 큐에서 현재 단어와 변환 횟수를 꺼낸다.
4. 현재 단어가 target이면 변환 횟수를 반환한다.
5. words 안에서 아직 방문하지 않았고, 한 글자만 다른 단어를 찾는다.
6. 찾은 단어를 방문 처리하고, 변환 횟수 +1과 함께 큐에 넣는다.
7. 큐가 빌 때까지 target을 찾지 못하면 0을 반환한다.
"""

# BFS에서 큐를 사용하기 위해 deque를 불러온다.
from collections import deque


# 프로그래머스에서 실행되는 solution 함수
def solution(begin, target, words):
    # target이 words 안에 없으면 절대 변환할 수 없다.
    if target not in words:
        return 0

    # 두 단어가 한 글자만 다른지 확인하는 함수
    def can_change(word1, word2):
        # 서로 다른 글자의 개수를 저장한다.
        diff_count = 0

        # 두 단어의 같은 위치에 있는 글자를 하나씩 비교한다.
        for i in range(len(word1)):
            # 같은 위치의 글자가 서로 다르면
            if word1[i] != word2[i]:
                # 다른 글자의 개수를 1 증가시킨다.
                diff_count += 1

        # 다른 글자의 개수가 정확히 1개일 때만 변환 가능하다.
        return diff_count == 1

    # words 안에 있는 각 단어의 방문 여부를 저장한다.
    visited = [False] * len(words)

    # BFS 탐색을 위한 큐를 만든다.
    queue = deque()

    # 시작 단어와 현재 변환 횟수 0을 큐에 넣는다.
    queue.append((begin, 0))

    # 큐가 빌 때까지 반복한다.
    while queue:
        # 큐에서 가장 먼저 들어온 단어와 변환 횟수를 꺼낸다.
        current_word, count = queue.popleft()

        # 현재 단어가 target이면 현재 변환 횟수가 최소 횟수이다.
        if current_word == target:
            return count

        # words 안의 모든 단어를 하나씩 확인한다.
        for i in range(len(words)):
            # 아직 방문하지 않았고, 현재 단어에서 한 글자만 바꿔 갈 수 있다면
            if not visited[i] and can_change(current_word, words[i]):
                # 해당 단어를 방문 처리한다.
                visited[i] = True

                # 다음 단어와 변환 횟수 +1을 큐에 넣는다.
                queue.append((words[i], count + 1))

    # 가능한 모든 변환을 확인해도 target에 도달하지 못한 경우
    return 0
