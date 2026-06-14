```python
"""
문제명: 부족한 금액 계산하기
출처: Programmers
유형: Implementation / Math / Accumulation
난이도: Level 1
상태: Solved
날짜: 2026-06-14

문제 요약:
- 놀이기구를 N번째 이용할 때마다 이용료가 price의 N배로 증가한다.
- 놀이기구를 count번 이용하는 데 필요한 총금액을 계산한다.
- 현재 가진 money보다 부족한 금액을 반환한다.
- 금액이 부족하지 않으면 0을 반환한다.

풀이 접근:
1. total_price를 0으로 초기화한다.
2. 1부터 count까지 순회한다.
3. 각 이용 횟수 i에 대해 price * i를 total_price에 누적한다.
4. 총 이용료에서 가진 금액을 뺀 값을 계산한다.
5. 부족한 금액이 음수이면 0을 반환하도록 max()를 사용한다.

시간복잡도:
- O(N), N은 놀이기구 이용 횟수 count

공간복잡도:
- O(1)

배운 점:
- 반복문을 사용해 일정한 규칙으로 증가하는 값을 누적할 수 있다.
- max(0, 값)을 사용하면 계산 결과가 음수일 때 0으로 처리할 수 있다.
"""

def solution(price, money, count):
    total_price = 0

    for i in range(1, count + 1):
        total_price += price * i

    return max(0, total_price - money)
```
