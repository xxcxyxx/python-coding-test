```python
"""
문제명: H-Index
출처: Programmers
유형: Sort / Enumeration
난이도: Level 2
상태: Solved
날짜: 2026-06-15

문제 요약:
- 논문별 인용 횟수가 담긴 배열 citations가 주어진다.
- h번 이상 인용된 논문이 h편 이상일 때 가능한 h의 최댓값을 구한다.

풀이 접근:
1. 인용 횟수를 내림차순으로 정렬한다.
2. 가장 많이 인용된 논문부터 순서대로 확인한다.
3. 현재까지 확인한 논문 수와 현재 논문의 인용 횟수를 비교한다.
4. 현재 논문의 인용 횟수가 논문 수 이상이면 해당 논문 수를 H-Index 후보로 저장한다.
5. 조건을 처음 만족하지 못하면 이후 논문의 인용 횟수는 더 작으므로 반복을 종료한다.
6. 마지막으로 저장된 H-Index를 반환한다.

시간복잡도:
- O(N log N)
- 논문 인용 횟수를 정렬하는 데 O(N log N)이 필요하다.
- 정렬된 배열을 순회하는 데 O(N)이 필요하다.

공간복잡도:
- O(N)
- sorted()가 새로운 정렬 리스트를 생성한다.

배운 점:
- sorted(citations, reverse=True)를 사용하면 내림차순으로 정렬할 수 있다.
- for value in list 형태에서는 value에 인덱스가 아니라 실제 원소가 들어간다.
- enumerate(iterable, start=1)를 사용하면 순서와 값을 함께 가져올 수 있다.
- 내림차순으로 정렬한 뒤 현재 논문 수와 인용 횟수를 비교하면 H-Index를 구할 수 있다.
- 조건을 만족하지 못한 이후의 인용 횟수는 더 작으므로 바로 반복을 종료할 수 있다.
"""

def solution(citations):
    sorted_citations = sorted(citations, reverse=True)
    h_index = 0

    for paper_count, citation in enumerate(sorted_citations, start=1):
        if citation >= paper_count:
            h_index = paper_count
        else:
            break

    return h_index
```
