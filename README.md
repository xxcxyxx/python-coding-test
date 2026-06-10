# Python Coding Test

Python 기반 코딩테스트 문제 풀이를 통해 문제 이해, 알고리즘 선택, 구현력, 시간복잡도 판단 능력을 훈련하기 위한 레포지토리입니다.

단순 정답 코드 저장이 아니라, 문제를 유형별로 분류하고 풀이 접근 방식과 구현 패턴을 함께 기록합니다.

---

## What this repository proves

이 레포지토리는 다음 역량을 보여주기 위해 만들어졌습니다.

- 문제 요구사항을 코드 로직으로 변환하는 능력
- 입력 조건과 제한사항을 바탕으로 알고리즘을 선택하는 능력
- Python 자료구조를 활용한 효율적인 구현 능력
- 시간복잡도와 예외 케이스를 고려하는 문제 해결 능력
- 반복되는 풀이 패턴을 정리하고 재사용하는 능력

---

## Problem Solving Approach

모든 문제는 아래 과정으로 해결합니다.

1. 문제에서 요구하는 결과 정의
2. 입력 크기와 제한사항 확인
3. 완전탐색 가능 여부 판단
4. 필요한 자료구조 또는 알고리즘 선택
5. 예외 케이스 확인
6. 시간복잡도 정리
7. 재사용 가능한 풀이 패턴으로 일반화

정답을 맞추는 것보다, 같은 유형의 문제를 다시 만났을 때 빠르게 접근할 수 있는 풀이 패턴을 만드는 것을 목표로 합니다.

---

## Repository Structure

```text
week01_implementation_string/  : 구현, 문자열, 배열 처리
week02_hash_sort/              : 해시, 정렬
week03_stack_queue/            : 스택, 큐
week04_bruteforce_greedy/      : 완전탐색, 그리디
week05_dfs_bfs/                : DFS, BFS, 그래프 탐색
week06_binary_heap_dp/         : 이분탐색, 힙, DP 기초
review/                        : 오답 및 반복 풀이 패턴 정리
templates/                     : 문제 풀이 기록 템플릿
```

---

## Problem Classification System

문제는 난이도가 아니라 사용된 풀이 방식 기준으로 분류합니다.

| Code | Meaning |
|---|---|
| I | Implementation |
| STR | String |
| ARR | Array |
| H | Hash |
| S | Sort |
| ST | Stack |
| Q | Queue |
| HP | Heap |
| BF | Brute Force |
| G | Greedy |
| DFS | Depth First Search |
| BFS | Breadth First Search |
| BS | Binary Search |
| DP | Dynamic Programming |

---

## Review Rule

오답 또는 다시 풀 필요가 있는 문제는 `review/wrong_answers.md`에 기록합니다.

기록 기준:

- 처음 접근을 못 한 문제
- 시간 초과가 발생한 문제
- 예외 케이스를 놓친 문제
- 풀이를 보고 해결한 문제
- 같은 유형에서 반복 실수한 문제

---

## Commit Message Rule

```text
solve: 문제명 풀이 추가
review: 문제명 오답 정리
refactor: 문제명 풀이 개선
docs: README 정리
```

예시:

```text
solve: 완주하지 못한 선수 풀이 추가
review: 문자열 내 마음대로 정렬하기 오답 정리
```
