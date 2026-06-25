"""
문제명: 주식가격
출처: Programmers 
유형: Stack / Queue / Implementation
난이도: Level 2
상태: Solved
날짜: 2026-06-25

문제 요약:
- 초 단위로 기록된 주식 가격이 담긴 배열 prices가 주어진다.
- 각 시점의 가격이 몇 초 동안 떨어지지 않았는지 구해야 한다.
- 현재 가격보다 낮은 가격이 처음 등장하면 가격이 떨어진 것으로 본다.
- 같은 가격이거나 더 높은 가격은 떨어진 것이 아니다.

풀이 접근:
1. 각 시점의 가격을 현재 가격으로 설정한다.
2. 현재 가격의 뒤쪽 가격들을 하나씩 확인한다.
3. 뒤쪽 가격을 하나 확인할 때마다 seconds를 1 증가시킨다.
4. 현재 가격보다 낮은 가격을 만나면 가격이 떨어진 것이므로 반복을 멈춘다.
5. 계산된 seconds를 answer에 저장한다.
6. 모든 가격에 대해 반복한 뒤 answer를 반환한다.

시간복잡도:
- O(N^2)
- 각 가격마다 뒤쪽 가격들을 다시 확인할 수 있기 때문이다.

공간복잡도:
- O(N)
- 각 가격의 결과를 answer 리스트에 저장한다.

배운 점:
- 이중 반복문을 사용하면 현재 위치 이후의 값들을 순서대로 확인할 수 있다.
- range(i + 1, len(prices))를 사용하면 현재 위치 뒤쪽만 확인할 수 있다.
- 가격이 떨어지는 순간도 1초가 지난 것으로 계산해야 하므로 seconds를 먼저 증가시킨다.
- break를 사용하면 가격이 처음 떨어진 순간 이후의 비교를 생략할 수 있다.

"""


def solution(prices):
    answer = []

    for i in range(len(prices)):
        seconds = 0

        for j in range(i + 1, len(prices)):
            seconds += 1

            if prices[i] > prices[j]:
                break

        answer.append(seconds)

    return answer
