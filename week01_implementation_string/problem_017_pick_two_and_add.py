```python
"""
문제명: 두 개 뽑아서 더하기
출처: Programmers
유형: Implementation / Array / Brute Force / Set
난이도: Level 1
상태: Solved
날짜: 2026-06-13

문제 요약:
- 정수 배열 numbers에서 서로 다른 인덱스의 숫자 두 개를 선택한다.
- 두 숫자를 더해서 만들 수 있는 모든 값을 구한다.
- 중복을 제거한 뒤 오름차순으로 정렬해 반환한다.

풀이 접근:
1. 중복된 합을 제거하기 위해 answer를 set으로 생성한다.
2. 첫 번째 인덱스 i를 배열의 처음부터 순회한다.
3. 두 번째 인덱스 j는 i + 1부터 시작한다.
4. numbers[i]와 numbers[j]의 합을 answer에 추가한다.
5. 모든 조합을 확인한 뒤 sorted()로 오름차순 정렬해 반환한다.

시간복잡도:
- O(N² log N)
- 두 숫자의 조합을 확인하는 데 O(N²),
  결과를 정렬하는 데 추가 시간이 필요하다.

공간복잡도:
- O(N²)
- 서로 다른 합을 set에 저장한다.

배운 점:
- 중복을 제거하면서 값을 저장할 때 set을 사용할 수 있다.
- 두 번째 반복문의 시작점을 i + 1로 설정하면
  같은 인덱스를 선택하거나 같은 조합을 반복하는 것을 방지할 수 있다.
- sorted(set)은 중복이 제거된 값을 오름차순 리스트로 반환한다.
"""

def solution(numbers):
    answer = set()

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])

    return sorted(answer)
```
