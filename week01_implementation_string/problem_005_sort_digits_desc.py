"""
문제명: 정수 내림차순으로 배치하기
출처: Programmers
유형: Implementation / String / Sort
난이도: Level 1
상태: Solved
날짜: 2026-06-11

문제 요약:
- 정수 n의 각 자릿수를 큰 수부터 작은 수 순서로 정렬한 뒤,
  새로운 정수로 반환한다.

풀이 접근:
1. 정수 n을 문자열로 변환한다.
2. sorted()와 reverse=True를 사용해 각 자릿수를 내림차순 정렬한다.
3. 정렬된 문자들을 join()으로 하나의 문자열로 합친다.
4. int()로 변환해 정수 형태로 반환한다.

시간복잡도:
- O(K log K), K는 n의 자릿수

배운 점:
- 숫자의 각 자릿수를 정렬할 때는 문자열로 변환하면 쉽게 처리할 수 있다.
- sorted()는 리스트를 반환하므로 join()을 사용해 다시 문자열로 합쳐야 한다.
"""

def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))
