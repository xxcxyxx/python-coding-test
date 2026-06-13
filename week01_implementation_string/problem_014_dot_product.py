```python
"""
문제명: 내적
출처: Programmers
유형: Implementation / Array
난이도: Level 1
상태: Solved
날짜: 2026-06-13

문제 요약:
- 길이가 같은 두 정수 배열 a와 b가 주어진다.
- 같은 인덱스에 있는 두 값을 곱한 뒤 모두 더한 내적을 반환한다.

풀이 접근:
1. 합계를 저장할 answer를 0으로 초기화한다.
2. 배열의 길이만큼 반복한다.
3. 같은 인덱스의 a[i]와 b[i]를 곱해 answer에 더한다.
4. 반복이 끝난 뒤 최종 합계를 반환한다.

시간복잡도:
- O(N), N은 배열 a와 b의 길이

배운 점:
- 길이가 같은 두 배열은 인덱스를 사용해 같은 위치의 값을 함께 처리할 수 있다.
- return이 반복문 안에 있으면 첫 번째 계산 후 함수가 종료되므로,
  모든 계산이 끝난 뒤 실행되도록 반복문 밖에 작성해야 한다.
"""

def solution(a, b):
    answer = 0

    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer
```
