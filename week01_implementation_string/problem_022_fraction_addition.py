"""
문제명: 분수의 덧셈
출처: Programmers
유형: Implementation / Math / GCD
난이도: Level 0
상태: Solved
날짜: 2026-06-30

문제 요약:
- 두 분수 numer1 / denom1, numer2 / denom2가 주어진다.
- 두 분수를 더한 값을 기약분수로 만든다.
- 결과를 [분자, 분모] 형태로 반환한다.

풀이 접근:
1. 두 분수의 분모를 곱해 공통분모를 만든다.
2. 각 분자를 상대 분모와 곱해 더한 뒤 새로운 분자를 만든다.
3. 분자와 분모의 최대공약수로 나누어 기약분수로 만든다.

시간복잡도:
- O(log N)

공간복잡도:
- O(1)

배운 점:
- 분모가 다른 분수는 공통분모를 만든 뒤 더해야 한다.
- math.gcd()를 사용하면 최대공약수를 쉽게 구할 수 있다.
- 분자와 분모를 최대공약수로 나누면 기약분수를 만들 수 있다.
"""

from math import gcd


def solution(numer1, denom1, numer2, denom2):
    numerator = numer1 * denom2 + numer2 * denom1
    denominator = denom1 * denom2

    common_divisor = gcd(numerator, denominator)

    return [numerator // common_divisor, denominator // common_divisor]
