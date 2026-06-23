# 문제: 카펫
# 출처: 프로그래머스 알고리즘 고득점 Kit
# 유형: 완전탐색
# 난이도: Level 2
#
# 핵심:
# 1. brown + yellow는 전체 카펫의 넓이이다.
# 2. 카펫의 가로와 세로를 곱하면 전체 넓이가 되어야 한다.
# 3. 갈색 격자는 바깥 테두리 1줄이다.
# 4. 따라서 노란색 영역은 테두리를 제외한 안쪽 영역이다.
# 5. 안쪽 영역의 크기는 (가로 - 2) * (세로 - 2)로 계산할 수 있다.
#
# 주의:
# 카펫의 가로 길이는 세로 길이보다 크거나 같아야 한다.
# 즉, width >= height 조건을 만족해야 한다.
#
# 풀이 방식:
# 1. 기본 완전탐색 방식
#    - height를 1부터 total까지 전부 확인한다.
#    - 이해하기 쉽지만 불필요한 반복이 많다.
#
# 2. 제곱근 최적화 방식
#    - 약수 쌍은 제곱근을 기준으로 반복된다.
#    - 따라서 height는 1부터 int(total ** 0.5)까지만 확인하면 된다.
#    - 더 효율적인 풀이이다.
#
# 예시:
# brown = 10, yellow = 2
# total = 12
#
# 가능한 가로, 세로 후보:
# 12 x 1
# 6 x 2
# 4 x 3
#
# [4, 3]일 때 안쪽 영역은
# (4 - 2) * (3 - 2) = 2
# yellow와 같으므로 정답은 [4, 3]이다.


def solution_basic(brown, yellow):
    """
    기본 완전탐색 풀이

    height를 1부터 total까지 전부 확인하는 방식이다.
    처음 이해할 때는 이 방식이 가장 직관적이다.
    """

    total = brown + yellow

    for height in range(1, total):
        # total이 height로 나누어떨어져야
        # width * height = total인 카펫 후보가 될 수 있다.
        if total % height == 0:
            width = total // height

            # 문제 조건상 가로는 세로보다 크거나 같아야 한다.
            if width >= height:
                # 테두리 1줄을 제외한 안쪽 영역이 yellow와 같은지 확인한다.
                if (width - 2) * (height - 2) == yellow:
                    return [width, height]


def solution_optimized(brown, yellow):
    """
    제곱근 최적화 풀이

    약수 쌍은 제곱근을 기준으로 반복된다.
    따라서 height를 전체 넓이의 제곱근까지만 확인해도 충분하다.
    """

    total = brown + yellow

    for height in range(1, int(total ** 0.5) + 1):
        # total이 height로 나누어떨어지면
        # height와 짝이 되는 width를 구할 수 있다.
        if total % height == 0:
            width = total // height

            # height를 제곱근까지만 확인하므로
            # width는 자연스럽게 height보다 크거나 같다.
            # 따라서 width >= height 조건을 따로 쓰지 않아도 된다.
            if (width - 2) * (height - 2) == yellow:
                return [width, height]


def solution(brown, yellow):
    """
    프로그래머스 제출용 함수

    최종 제출은 더 효율적인 제곱근 최적화 방식을 사용한다.
    """
    return solution_optimized(brown, yellow)


# 테스트
if __name__ == "__main__":
    print(solution_basic(10, 2))       # [4, 3]
    print(solution_basic(8, 1))        # [3, 3]
    print(solution_basic(24, 24))      # [8, 6]

    print(solution_optimized(10, 2))   # [4, 3]
    print(solution_optimized(8, 1))    # [3, 3]
    print(solution_optimized(24, 24))  # [8, 6]

    print(solution(10, 2))             # [4, 3]
    print(solution(8, 1))              # [3, 3]
    print(solution(24, 24))            # [8, 6]
