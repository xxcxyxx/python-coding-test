```python
"""
문제명: 서울에서 김서방 찾기
출처: Programmers
유형: Implementation / Array / String Search
난이도: Level 1
상태: Solved
날짜: 2026-06-14

문제 요약:
- 문자열 배열 seoul에서 "Kim"의 인덱스를 찾는다.
- "김서방은 x에 있다" 형식의 문자열을 반환한다.

풀이 접근:
1. seoul의 인덱스를 처음부터 순회한다.
2. seoul[i]가 "Kim"인지 확인한다.
3. "Kim"을 찾으면 해당 인덱스를 문자열에 넣어 반환한다.

시간복잡도:
- O(N), N은 seoul의 길이

공간복잡도:
- O(1)

배운 점:
- 리스트의 특정 원소를 찾을 때 인덱스를 이용해 순회할 수 있다.
- seoul.index("Kim")은 리스트에서 원소의 위치를 찾는다.
- seoul[i].index("Kim")은 개별 문자열 안에서 부분 문자열의 위치를 찾는 표현이다.
- 원하는 원소를 찾은 즉시 return하면 이후 탐색을 생략할 수 있다.
"""

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return f"김서방은 {i}에 있다"
```
