```python
"""
문제명: 의상
출처: Programmers
유형: Hash / Dictionary / Counting / Combination
난이도: Level 2
상태: Solved
날짜: 2026-06-14

문제 요약:
- 의상 이름과 의상 종류가 담긴 2차원 배열 clothes가 주어진다.
- 같은 종류의 의상은 최대 한 개만 착용할 수 있다.
- 최소 한 개 이상의 의상을 착용할 때 가능한 조합의 수를 반환한다.

풀이 접근:
1. 의상 종류별 개수를 딕셔너리에 저장한다.
2. 각 종류에서는 해당 의상 중 하나를 선택하거나,
   아무것도 선택하지 않을 수 있다.
3. 따라서 종류별 선택지는 의상 개수 + 1개이다.
4. 모든 종류의 선택지 수를 곱한다.
5. 아무 의상도 입지 않는 경우를 제외하기 위해 1을 뺀다.

시간복잡도:
- O(N)
- clothes를 한 번 순회해 종류별 개수를 계산한다.

공간복잡도:
- O(K)
- K는 서로 다른 의상 종류의 개수이다.

배운 점:
- dict.get(key, 0)을 사용하면 종류별 개수를 쉽게 셀 수 있다.
- dict.values()를 사용하면 딕셔너리의 값만 순회할 수 있다.
- 각 종류에서 의상을 입지 않는 경우를 포함하기 위해 개수에 1을 더한다.
- 모든 종류에서 아무것도 선택하지 않는 경우가 포함되므로 마지막에 1을 뺀다.
- 경우의 수를 곱할 때는 초기값을 1로 설정해야 한다.
"""

def solution(clothes):
    clothes_count = {}

    for name, category in clothes:
        clothes_count[category] = clothes_count.get(category, 0) + 1

    answer = 1

    for count in clothes_count.values():
        answer *= count + 1

    return answer - 1
```
