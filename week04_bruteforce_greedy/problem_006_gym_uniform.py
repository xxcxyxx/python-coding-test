"""
문제명: 체육복
출처: Programmers
유형: Greedy / Set
난이도: Level 1
상태: Solved
날짜: 2026-06-26

문제 요약:
- 전체 학생 수 n, 체육복을 도난당한 학생 lost, 여벌 체육복을 가진 학생 reserve가 주어진다.
- 체육복을 잃어버린 학생은 바로 앞번호 또는 뒷번호 학생에게만 체육복을 빌릴 수 있다.
- 여벌 체육복을 가진 학생도 도난당했을 수 있으며, 이 경우 자기 여벌을 입어야 하므로 다른 학생에게 빌려줄 수 없다.
- 체육수업을 들을 수 있는 학생의 최댓값을 구해야 한다.

풀이 접근:
1. lost와 reserve를 set으로 변환한다.
2. lost와 reserve에 동시에 있는 학생을 먼저 제거한다.
3. 체육복을 잃어버린 학생을 작은 번호부터 확인한다.
4. 앞번호 학생이 여벌 체육복을 가지고 있으면 앞번호에게 빌린다.
5. 앞번호가 불가능하면 뒷번호 학생에게 빌린다.
6. 앞번호와 뒷번호 모두 불가능하면 수업 가능 인원에서 1명을 뺀다.

시간복잡도:
- O(N log N): 체육복을 잃어버린 학생을 정렬하기 때문이다.

공간복잡도:
- O(N): lost_set과 reserve_set을 사용하기 때문이다.

배운 점:
- set을 사용하면 교집합, 차집합 연산을 쉽게 처리할 수 있다.
- lost와 reserve에 동시에 있는 학생을 먼저 제거해야 정확한 계산이 가능하다.
- sorted(lost_set)을 사용하면 작은 번호부터 순서대로 처리할 수 있다.
- 탐욕법은 현재 상황에서 가장 적절한 선택을 반복해 최적의 결과를 구하는 방식이다.
"""

def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    both = lost_set & reserve_set
    lost_set -= both
    reserve_set -= both

    for student in sorted(lost_set):
        if student - 1 in reserve_set:
            reserve_set.remove(student - 1)
        elif student + 1 in reserve_set:
            reserve_set.remove(student + 1)
        else:
            n -= 1

    return n
