# 문제: 올바른 괄호
# 유형: 스택 / 문자열
# 핵심:
# 1. '('를 만나면 balance를 1 증가시킨다.
# 2. ')'를 만나면 balance를 1 감소시킨다.
# 3. balance가 음수가 되면 닫는 괄호가 먼저 나온 것이므로 False를 반환한다.
# 4. 모든 문자를 확인한 후 balance가 0인지 확인한다.
# 시간복잡도: O(N)
# 공간복잡도: O(1)


def solution(s):
    balance = 0

    for bracket in s:
        if bracket == '(':
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            return False

    return balance == 0


# 테스트
print(solution("()()"))    # True
print(solution("(())()"))  # True
print(solution(")()("))    # False
print(solution("(()("))    # False
