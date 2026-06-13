```python
"""
문제명: 이진 변환 반복하기
출처: Programmers
유형: Implementation / String / While / Binary Conversion
난이도: Level 2
상태: Solved
날짜: 2026-06-13

문제 요약:
- 0과 1로 이루어진 문자열 s가 주어진다.
- s에서 모든 0을 제거한 뒤, 남은 문자열의 길이를 2진법으로 변환한다.
- 이 과정을 s가 "1"이 될 때까지 반복한다.
- 총 변환 횟수와 제거한 0의 누적 개수를 반환한다.

풀이 접근:
1. 변환 횟수와 제거한 0의 누적 개수를 0으로 초기화한다.
2. s가 "1"이 아닌 동안 while문을 반복한다.
3. 현재 문자열에 포함된 0의 개수를 센다.
4. 제거한 0의 개수를 누적한다.
5. 전체 길이에서 0의 개수를 빼 남아 있는 1의 개수를 구한다.
6. 1의 개수를 2진법 문자열로 변환해 새로운 s로 저장한다.
7. 변환 횟수를 1 증가시킨다.
8. 반복이 끝나면 변환 횟수와 제거한 0의 개수를 반환한다.

시간복잡도:
- O(N)
- 첫 번째 반복에서 문자열 전체를 확인하며,
  이후 문자열의 길이는 빠르게 감소한다.

공간복잡도:
- O(N)
- 변환 과정에서 새로운 문자열을 생성한다.

배운 점:
- 반복 횟수는 모르지만 종료 조건이 명확할 때 while문을 사용할 수 있다.
- s.count("0")으로 문자열 내부의 0 개수를 셀 수 있다.
- bin(number)는 2진법 문자열을 반환한다.
- bin() 결과의 앞에는 "0b"가 붙으므로 [2:]로 제거할 수 있다.
- while문에서는 반복할 때마다 종료 조건에 사용되는 값이 변경되어야 한다.
"""

def solution(s):
    transform_count = 0
    removed_zero_count = 0

    while s != "1":
        zero_count = s.count("0")
        removed_zero_count += zero_count

        one_count = len(s) - zero_count
        s = bin(one_count)[2:]

        transform_count += 1

    return [transform_count, removed_zero_count]
```
