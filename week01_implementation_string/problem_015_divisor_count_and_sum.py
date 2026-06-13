```python
"""
문제명: 약수의 개수와 덧셈
출처: Programmers
유형: Implementation / Math / Brute Force
난이도: Level 1
상태: Solved
날짜: 2026-06-13

문제 요약:
- left부터 right까지의 모든 정수를 확인한다.
- 약수의 개수가 짝수인 수는 더하고,
  약수의 개수가 홀수인 수는 뺀 결과를 반환한다.

풀이 접근:
1. left부터 right까지 숫자 i를 하나씩 확인한다.
2. 1부터 i까지 순회하며 i의 약수 개수를 센다.
3. 약수 개수가 짝수이면 i를 answer에 더한다.
4. 약수 개수가 홀수이면 i를 answer에서 뺀다.
5. 모든 숫자의 처리가 끝나면 answer를 반환한다.

시간복잡도:
- O((right - left + 1) × right)
- 최악의 경우 O(right²)

공간복잡도:
- O(1)

배운 점:
- i % j == 0이면 j는 i의 약수이다.
- 각 숫자의 약수 개수를 따로 세기 위해 count는
  바깥 반복문이 시작될 때마다 0으로 초기화해야 한다.
- 약수 개수의 짝수·홀수 판단은 안쪽 반복문이 끝난 뒤 해야 한다.
"""

def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer
```
