"""
문제명: 모음사전
출처: Programmers
유형: Brute Force / itertools.product / Sort
난이도: Level 2

상태: Solved
날짜: 2026-07-22

문제 요약:
- 알파벳 모음 A, E, I, O, U만 사용하여 단어를 만든다.
- 단어의 길이는 1글자 이상 5글자 이하이다.
- 만들어진 모든 단어를 사전순으로 정렬한다.
- 주어진 word가 사전에서 몇 번째에 위치하는지 반환한다.

풀이 접근:
1. 모든 단어를 저장할 빈 리스트를 만든다.
2. 단어 길이를 1부터 5까지 반복한다.
3. product()를 사용하여 각 길이의 모든 모음 조합을 만든다.
4. product()가 만든 튜플을 join()으로 문자열로 변환한다.
5. 변환한 단어를 리스트에 저장한다.
6. 모든 단어를 사전순으로 정렬한다.
7. word가 저장된 인덱스를 찾는다.
8. 인덱스는 0부터 시작하므로 1을 더해 반환한다.

핵심 개념:
- product("AEIOU", repeat=length)는 모음을 중복해서 선택할 수 있는
  모든 순서 조합을 생성한다.
- product()의 결과는 튜플이므로 join()을 사용해 문자열로 변환한다.
- 만들 수 있는 단어는 총 3,905개이므로 완전탐색이 가능하다.

시간 복잡도:
- 전체 단어의 개수를 N이라고 할 때 정렬에 O(N log N)
- N은 최대 3,905이므로 충분히 처리할 수 있다.
"""

from itertools import product


def solution(word):
    # 만들어지는 모든 모음 단어를 저장할 리스트
    words = []

    # 단어 길이를 1글자부터 5글자까지 반복
    for length in range(1, 6):

        # 현재 길이로 만들 수 있는 모든 모음 조합 생성
        for letters in product("AEIOU", repeat=length):

            # 튜플 형태의 모음 조합을 문자열로 변환
            new_word = "".join(letters)

            # 완성된 단어를 리스트에 저장
            words.append(new_word)

    # 모든 단어를 사전순으로 정렬
    words.sort()

    # word의 인덱스에 1을 더해 실제 사전 순서 반환
    return words.index(word) + 1
