"""
문제명: 3진법 뒤집기
출처: Programmers
유형: Implementation / Math / Base Conversion
난이도: Level 1
상태: Solved
날짜: 2026-06-13

문제 요약:
- 자연수 n을 3진법으로 변환한다.
- 3진법 숫자의 앞뒤를 뒤집는다.
- 뒤집은 값을 다시 10진법으로 변환해 반환한다.

풀이 접근:
1. n을 3으로 계속 나누면서 나머지를 문자열에 추가한다.
2. 나머지는 낮은 자릿수부터 나오기 때문에,
   저장된 문자열은 이미 뒤집힌 3진법이 된다.
3. int(문자열, 3)을 사용해 뒤집힌 3진법을 10진수로 변환한다.

시간복잡도:
- O(log₃N)

공간복잡도:
- O(log₃N)

배운 점:
- n % 3으로 3진법의 각 자릿수를 구할 수 있다.
- n //= 3으로 다음 몫을 갱신한다.
- int(문자열, 진법)을 사용하면 해당 진법의 문자열을 10진수로 변환할 수 있다.
"""

def solution(n):
    reversed_ternary = ""

    while n > 0:
        reversed_ternary += str(n % 3)
        n //= 3

    return int(reversed_ternary, 3)
