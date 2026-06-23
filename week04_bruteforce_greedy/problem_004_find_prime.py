# 문제: 소수 찾기
# 출처: 프로그래머스 알고리즘 고득점 Kit
# 유형: 완전탐색 / 순열 / 소수 판별
# 난이도: Level 2
#
# 핵심:
# 1. numbers의 숫자 조각으로 만들 수 있는 모든 숫자를 만든다.
# 2. 숫자는 1자리부터 numbers의 전체 길이까지 만들 수 있다.
# 3. 숫자의 순서에 따라 다른 숫자가 되므로 permutations를 사용한다.
# 4. 같은 숫자가 여러 번 만들어질 수 있으므로 set으로 중복을 제거한다.
# 5. 만들어진 숫자 후보들을 하나씩 확인하며 소수인지 판별한다.
#
# 주의:
# 1. 0과 1은 소수가 아니다.
# 2. "011"과 "11"은 같은 숫자 11로 취급해야 한다.
# 3. 따라서 후보 숫자는 리스트가 아니라 set에 저장해야 한다.
# 4. 소수 판별 시 자기 자신으로 나누는 경우는 제외해야 한다.
#    그래서 range(2, number)를 사용한다.
#
# 예시:
# numbers = "17"
# 만들 수 있는 숫자 후보: 1, 7, 17, 71
# 이 중 소수는 7, 17, 71이므로 정답은 3이다.
#
# numbers = "011"
# 만들 수 있는 숫자 중 011은 int로 바꾸면 11이다.
# 11과 011은 같은 숫자로 취급하므로 중복 제거가 필요하다.
# 이 중 소수는 11, 101이므로 정답은 2이다.


from itertools import permutations


def is_prime(number):
    """
    기본 소수 판별 함수

    2부터 number - 1까지 모두 나누어본다.
    나누어떨어지는 수가 하나라도 있으면 소수가 아니다.
    """

    # 0과 1은 소수가 아니다.
    if number < 2:
        return False

    # 2부터 number - 1까지 확인한다.
    # 자기 자신은 제외해야 하므로 range(2, number)를 사용한다.
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def solution(numbers):
    # 만들 수 있는 숫자 후보를 중복 없이 저장한다.
    candidates = set()

    # 1자리 숫자부터 len(numbers)자리 숫자까지 모두 만든다.
    for length in range(1, len(numbers) + 1):
        # numbers에서 length개를 뽑아 순서를 고려해 나열한다.
        for case in permutations(numbers, length):
            # 예: ('1', '7') -> "17" -> 17
            number = int(''.join(case))
            candidates.add(number)

    answer = 0

    # 만들어진 후보 숫자 중 소수의 개수를 센다.
    for number in candidates:
        if is_prime(number):
            answer += 1

    return answer


# 테스트
if __name__ == "__main__":
    print(solution("17"))   # 3
    print(solution("011"))  # 2
