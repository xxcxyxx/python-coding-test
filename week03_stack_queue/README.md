# Week 03 - Stack & Queue

## 학습 목표

* Stack과 Queue의 차이를 이해하고 문제에 적용한다.
* LIFO와 FIFO 구조를 구분해 사용할 수 있도록 연습한다.
* `list`, `deque`, `append()`, `pop()`, `popleft()`의 사용 상황을 구분한다.
* 순서 처리, 대기열, 우선순위, 시뮬레이션 문제를 코드로 구현한다.
* 문제를 단순 구현 방식으로 먼저 이해한 뒤, 필요한 경우 효율적인 자료구조로 개선한다.

## 핵심 개념

* Stack
* Queue
* LIFO
* FIFO
* `collections.deque`
* `append()`
* `pop()`
* `popleft()`
* 반복문을 이용한 순서 처리
* 조건에 따른 대기열 관리
* 시뮬레이션 구현

## 문제 목록

| 번호  | 문제명        | 유형                             | 난이도     | 상태     | 파일                                                                                     |
| --- | ---------- | ------------------------------ | ------- | ------ | -------------------------------------------------------------------------------------- |
| 001 | 같은 숫자는 싫어  | Stack / Implementation         | Level 1 | Solved | [problem_001_no_consecutive_duplicates.py](./problem_001_no_consecutive_duplicates.py) |
| 002 | 기능개발       | Queue / Implementation         | Level 2 | Solved | [problem_002_feature_development.py](./problem_002_feature_development.py)             |
| 003 | 올바른 괄호     | Stack                          | Level 2 | Solved | [problem_003_valid_parentheses.py](./problem_003_valid_parentheses.py)                 |
| 004 | 프로세스       | Queue / Priority               | Level 2 | Solved | [problem_004_process.py](./problem_004_process.py)                                     |
| 005 | 주식가격       | Stack / Queue / Implementation | Level 2 | Solved | [problem_005_stock_price.py](./problem_005_stock_price.py)                             |
| 006 | 다리를 지나는 트럭 | Queue / Simulation             | Level 2 | Solved | [problem_006_truck_bridge.py](./problem_006_truck_bridge.py)                           |

## 문제별 핵심 정리

### 001. 같은 숫자는 싫어

* 연속으로 같은 숫자가 나오는 경우 하나만 남기는 문제다.
* 이전 값과 현재 값을 비교하면서 결과 리스트에 추가한다.
* Stack처럼 마지막에 넣은 값과 현재 값을 비교하는 방식으로 해결할 수 있다.

### 002. 기능개발

* 각 기능이 완료되는 데 필요한 날짜를 계산한다.
* 앞 기능이 배포될 때 뒤에 완료된 기능들도 함께 배포한다.
* Queue처럼 앞에서부터 순서대로 처리하는 것이 핵심이다.

### 003. 올바른 괄호

* 여는 괄호는 Stack에 넣고, 닫는 괄호가 나오면 Stack에서 제거한다.
* 닫는 괄호가 나왔을 때 Stack이 비어 있으면 올바르지 않은 괄호다.
* 모든 문자를 확인한 뒤 Stack이 비어 있어야 올바른 괄호다.

### 004. 프로세스

* 실행 대기 큐에서 프로세스를 하나씩 꺼내며 우선순위를 비교한다.
* 더 높은 우선순위가 남아 있으면 다시 큐 뒤로 보낸다.
* 내가 찾는 프로세스의 원래 위치를 함께 저장해 추적하는 것이 핵심이다.

### 005. 주식가격

* 각 시점의 가격이 몇 초 동안 떨어지지 않는지 구하는 문제다.
* 현재 가격을 기준으로 뒤쪽 가격들을 하나씩 확인한다.
* 현재 가격보다 낮은 가격을 만나면 가격이 떨어진 것이므로 반복을 멈춘다.
* 가격이 떨어지는 순간도 1초가 지난 것으로 계산해야 한다.

### 006. 다리를 지나는 트럭

* 다리를 `bridge_length` 길이의 Queue로 생각한다.
* 매초마다 다리 맨 앞 값을 제거하고, 새 트럭 또는 빈칸을 뒤에 추가한다.
* 현재 다리 위 무게를 따로 관리해 다음 트럭이 올라갈 수 있는지 판단한다.
* `deque`를 사용하면 맨 앞 값을 효율적으로 제거할 수 있다.

## 사용한 주요 Python 문법

```python
from collections import deque
```

```python
queue = deque()
queue.append(value)
queue.popleft()
```

```python
stack = []
stack.append(value)
stack.pop()
```

```python
while queue:
    ...
```

```python
for i in range(len(arr)):
    ...
```

## 복습 포인트

* Stack은 마지막에 들어온 값이 먼저 나간다.
* Queue는 먼저 들어온 값이 먼저 나간다.
* `pop(0)`은 리스트의 맨 앞 값을 제거하지만, 데이터가 많을 때 비효율적일 수 있다.
* Queue 문제에서는 `deque`의 `popleft()`를 사용하는 것이 좋다.
* 시뮬레이션 문제는 시간, 현재 상태, 대기 상태를 변수로 나누어 관리하면 이해하기 쉽다.
* 문제를 풀 때는 먼저 현재 상태가 어떻게 변하는지 손으로 따라가 본 뒤 코드로 옮긴다.

## 학습 회고

스택/큐 유형에서는 자료구조 자체보다 “순서”를 어떻게 관리하는지가 중요했다.

* 같은 숫자는 싫어: 이전 값과 현재 값 비교
* 기능개발: 앞 기능 기준으로 배포 묶음 처리
* 올바른 괄호: 괄호의 짝을 Stack으로 관리
* 프로세스: 우선순위와 원래 위치를 함께 관리
* 주식가격: 현재 위치 이후의 가격 변화 확인
* 다리를 지나는 트럭: 다리 위 상태를 Queue로 시뮬레이션

이번 유형을 통해 `deque`, `popleft()`, `append()`, `break`, 반복 조건 관리에 익숙해졌다.
