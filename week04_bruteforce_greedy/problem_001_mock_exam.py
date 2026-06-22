# 문제: 모의고사
# 유형: 완전탐색
# 핵심: 각 수포자의 반복 패턴을 정답 배열과 모두 비교한다.
# 시간복잡도: O(n)

def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    scores = [0, 0, 0]

    for i, answer in enumerate(answers):
        for student in range(3):
            if patterns[student][i % len(patterns[student])] == answer:
                scores[student] += 1

    max_score = max(scores)

    result = []

    for i in range(3):
        if scores[i] == max_score:
            result.append(i + 1)

    return result
