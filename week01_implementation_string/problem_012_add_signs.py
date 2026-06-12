"""
문제명: 음양 더하기
출처: Programmers
유형: Implementation / Array / Conditional
난이도: Level 1
상태: Solved
날짜: 2026-06-12

문제 요약:
- 정수의 절댓값 배열 absolutes와 부호 배열 signs가 주어진다.
- signs[i]가 True이면 absolutes[i]는 양수,
  False이면 음수로 계산한다.
- 실제 정수들의 합을 반환한다.

풀이 접근:
1. absolutes와 signs는 같은 인덱스끼리 대응된다.
2. zip()을 사용해 절댓값과 부호 정보를 함께 순회한다.
3. sign이 True이면 값을 더하고, False이면 값을 뺀다.
4. 최종 합계를 반환한다.

시간복잡도:
- O(N), N은 absolutes의 길이

배운 점:
- 두 배열을 같은 인덱스 기준으로 순회할 때 zip()을 사용할 수 있다.
- Boolean 값은 조건문에서 바로 사용할 수 있다.
"""

def solution(absolutes, signs):
    answer = 0
    
    for num, sign in zip(absolutes, signs):
        if sign:
            answer += num
        else:
            answer -= num
    
    return answer
