# 문제: 최소직사각형
# 출처: 프로그래머스 알고리즘 고득점 Kit
# 유형: 완전탐색 / 구현
# 난이도: Level 1
#
# 핵심:
# 1. 모든 명함은 회전할 수 있다.
# 2. 각 명함마다 긴 쪽은 가로 방향, 짧은 쪽은 세로 방향으로 정리한다.
# 3. 정리된 긴 쪽들 중 가장 큰 값을 지갑의 width로 사용한다.
# 4. 정리된 짧은 쪽들 중 가장 큰 값을 지갑의 height로 사용한다.
# 5. 모든 명함을 담을 수 있는 최소 지갑의 넓이는 width * height이다.
#
# 주의:
# 명함의 가로와 세로를 그대로 비교하면 안 된다.
# 명함은 회전할 수 있으므로,
# 각 명함에서 큰 값과 작은 값을 먼저 나누어 생각해야 한다.
#
# 예시:
# [30, 70] 크기의 명함은 회전하면 [70, 30]처럼 넣을 수 있다.
# 따라서 긴 쪽 70, 짧은 쪽 30으로 정리한다.


def solution(sizes):
    width = 0
    height = 0

    for w, h in sizes:
        # 명함은 회전할 수 있으므로
        # 둘 중 큰 값을 긴 쪽, 작은 값을 짧은 쪽으로 정리한다.
        long_side = max(w, h)
        short_side = min(w, h)

        # 지금까지 본 명함들 중 가장 긴 쪽을 width에 저장한다.
        width = max(width, long_side)

        # 지금까지 본 명함들 중 짧은 쪽의 최댓값을 height에 저장한다.
        height = max(height, short_side)

    return width * height


# 테스트
if __name__ == "__main__":
    sizes1 = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(sizes1))  # 4000

    sizes2 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
    print(solution(sizes2))  # 120

    sizes3 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    print(solution(sizes3))  # 133
