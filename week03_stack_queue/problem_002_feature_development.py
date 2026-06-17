```python
"""
문제명: 기능개발
출처: Programmers
유형: Queue / Implementation / Simulation
난이도: Level 2
상태: Solved
날짜: 2026-06-17

문제 요약:
- 각 기능의 현재 진행률과 하루 개발 속도가 주어진다.
- 기능은 앞에 있는 기능부터 순서대로 배포해야 한다.
- 뒤의 기능이 먼저 완성되어도 앞 기능이 배포될 때까지 기다린다.
- 각 배포일마다 함께 배포되는 기능의 개수를 반환한다.

풀이 접근:
1. 각 기능이 완성되기까지 필요한 날짜를 계산한다.
2. 첫 번째 기능의 완료일을 현재 배포 기준일로 설정한다.
3. 다음 기능의 완료일이 현재 배포 기준일 이하라면 함께 배포한다.
4. 현재 배포 기준일보다 늦게 완료된다면 기존 배포 묶음을 저장한다.
5. 해당 기능의 완료일을 새로운 배포 기준일로 설정한다.
6. 반복이 끝난 뒤 마지막 배포 묶음을 결과에 추가한다.

시간복잡도:
- O(N)
- 각 기능의 완료 날짜를 계산하고 한 번씩 순회한다.

공간복잡도:
- O(N)
- 각 기능의 완료 날짜를 days 리스트에 저장한다.

배운 점:
- math.ceil()을 사용하면 나눗셈 결과를 올림할 수 있다.
- zip()을 사용하면 progresses와 speeds의 같은 위치 값을 함께 순회할 수 있다.
- 완료일이 빠르더라도 앞 기능이 배포되지 않으면 함께 기다려야 한다.
- 반복문 안에서는 이전 배포 묶음만 저장되므로,
  반복문이 끝난 뒤 마지막 묶음을 한 번 더 추가해야 한다.
"""

import math


def solution(progresses, speeds):
    answer = []
    days = []

    # 각 기능이 완성되기까지 필요한 날짜 계산
    for progress, speed in zip(progresses, speeds):
        day = math.ceil((100 - progress) / speed)
        days.append(day)

    # 첫 번째 기능의 완료일을 배포 기준일로 설정
    deploy_day = days[0]
    count = 1

    # 두 번째 기능부터 완료일 비교
    for day in days[1:]:
        if day <= deploy_day:
            count += 1
        else:
            answer.append(count)
            deploy_day = day
            count = 1

    # 마지막 배포 묶음 추가
    answer.append(count)

    return answer
```
