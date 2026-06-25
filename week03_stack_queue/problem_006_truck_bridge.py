"""
문제명: 다리를 지나는 트럭
출처: Programmers
유형: Stack / Queue / Simulation
난이도: Level 2
상태: Solved
날짜: 2026-06-25

문제 요약:
- 트럭 여러 대가 정해진 순서대로 다리를 건너야 한다.
- 다리에는 bridge_length만큼의 길이가 있고, 동시에 올라간 트럭들의 무게 합은 weight를 넘을 수 없다.
- 모든 트럭이 다리를 완전히 건너는 데 걸리는 시간을 구해야 한다.

풀이 접근:
1. 다리를 bridge_length 길이의 큐로 만든다.
2. 0은 트럭이 없는 빈칸을 의미한다.
3. 매초마다 다리 맨 앞 값을 제거한다.
4. 제거한 값이 트럭이면 현재 다리 무게에서 뺀다.
5. 다음 대기 트럭을 올릴 수 있으면 다리 뒤에 추가한다.
6. 올릴 수 없으면 빈칸 0을 추가한다.
7. 대기 트럭이 없고 다리 위 트럭도 없을 때까지 반복한다.

시간복잡도:
- O(N): 각 트럭이 한 번씩 다리에 올라가고 빠져나가기 때문이다.

공간복잡도:
- O(N + bridge_length): 대기 트럭 큐와 다리 상태 큐를 사용하기 때문이다.

배운 점:
- deque를 사용하면 큐의 맨 앞 값을 효율적으로 제거할 수 있다.
- popleft()는 다리 맨 앞의 트럭이 빠져나가는 상황을 표현할 수 있다.
- append()는 새 트럭 또는 빈칸이 다리 뒤에 들어오는 상황을 표현할 수 있다.
- current_weight를 따로 관리하면 매번 sum(bridge)를 계산하지 않아도 된다.
"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0

    while truck_weights or current_weight > 0:
        time += 1

        out_truck = bridge.popleft()
        current_weight -= out_truck

        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                in_truck = truck_weights.popleft()
                bridge.append(in_truck)
                current_weight += in_truck
            else:
                bridge.append(0)

    return time
