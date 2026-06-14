```python
"""
문제명: 완주하지 못한 선수
출처: Programmers
유형: Hash / Dictionary / Counting
난이도: Level 1
상태: Solved
날짜: 2026-06-14

문제 요약:
- 참가자 명단 participant와 완주자 명단 completion이 주어진다.
- 단 한 명의 선수를 제외하고 모든 선수가 완주했다.
- 동명이인이 있을 수 있으므로 이름별 인원수를 고려해야 한다.
- 완주하지 못한 선수의 이름을 반환한다.

풀이 접근:
1. participant를 순회하며 참가자 이름별 인원수를 딕셔너리에 저장한다.
2. completion을 순회하며 완주한 선수의 인원수를 1씩 뺀다.
3. 최종적으로 인원수가 1인 선수의 이름을 반환한다.

시간복잡도:
- O(N)
- 참가자와 완주자 명단을 각각 한 번씩 순회한다.

공간복잡도:
- O(N)
- 참가자 이름별 인원수를 딕셔너리에 저장한다.

배운 점:
- 동명이인이 있는 경우 set으로는 개수 정보를 유지할 수 없다.
- dict.get(key, 0)을 사용하면 존재하지 않는 키의 기본값을 0으로 처리할 수 있다.
- dict.items()를 사용하면 키와 값을 함께 순회할 수 있다.
"""

def solution(participant, completion):
    count = {}

    for name in participant:
        count[name] = count.get(name, 0) + 1

    for name in completion:
        count[name] -= 1

    for name, number in count.items():
        if number == 1:
            return name
```
