# Week 02 - Hash & Sort

## 학습 목표

* `dict`, `set`, `Counter`를 활용해 탐색 시간을 줄인다.
* 중복 여부, 등장 횟수, 종류 개수를 빠르게 판단하는 방법을 익힌다.
* `sorted()`, `sort()`, `key`, `lambda`, `reverse=True`를 활용해 원하는 기준으로 정렬한다.
* 문제 조건을 정렬 기준으로 바꾸는 연습을 한다.
* 해시로 데이터를 모으고, 정렬로 순서를 정하는 문제 흐름을 이해한다.

## 핵심 개념

* Hash
* `dict`
* `set`
* `collections.Counter`
* `get()`
* `items()`
* `sorted()`
* `list.sort()`
* `key`
* `lambda`
* `reverse=True`
* 튜플 정렬
* 문자열 정렬
* 등장 횟수 세기
* 중복 제거
* 정렬 기준 직접 설정

## 문제 목록

| 번호  | 문제명        | 유형                 | 난이도     | 상태     | 파일                                                                     |
| --- | ---------- | ------------------ | ------- | ------ | ---------------------------------------------------------------------- |
| 001 | 완주하지 못한 선수 | Hash               | Level 1 | Solved | [problem_001_unfinished_runner.py](./problem_001_unfinished_runner.py) |
| 002 | 전화번호 목록    | Hash / String      | Level 2 | Solved | [problem_002_phone_book.py](./problem_002_phone_book.py)               |
| 003 | 폰켓몬        | Hash / Set         | Level 1 | Solved | [problem_003_pokemon.py](./problem_003_pokemon.py)                     |
| 004 | 의상         | Hash / Combination | Level 2 | Solved | [problem_004_clothes.py](./problem_004_clothes.py)                     |
| 005 | K번째수       | Sort / Slicing     | Level 1 | Solved | [problem_005_kth_number.py](./problem_005_kth_number.py)               |
| 006 | 가장 큰 수     | Sort / Lambda      | Level 2 | Solved | [problem_006_largest_number.py](./problem_006_largest_number.py)       |
| 007 | H-Index    | Sort               | Level 2 | Solved | [problem_007_h_index.py](./problem_007_h_index.py)                     |
| 008 | 베스트앨범      | Hash / Sort        | Level 3 | Solved | [problem_008_best_album.py](./problem_008_best_album.py)               |

## 문제별 핵심 정리

### 001. 완주하지 못한 선수

* 참가자 명단과 완주자 명단을 비교해 완주하지 못한 한 명을 찾는 문제다.
* 동명이인이 있을 수 있기 때문에 이름의 등장 횟수를 세어야 한다.
* `dict.get(key, 0)`을 사용하면 처음 등장하는 이름도 안전하게 개수를 누적할 수 있다.
* 참가자는 `+1`, 완주자는 `-1` 처리한 뒤 값이 남아 있는 이름을 찾는다.

### 002. 전화번호 목록

* 어떤 전화번호가 다른 전화번호의 접두어인지 확인하는 문제다.
* 전화번호를 정렬하면 접두어 관계가 있는 번호들이 서로 이웃하게 된다.
* 정렬 후 현재 번호와 다음 번호만 비교하면 된다.
* `startswith()`를 사용해 접두어 여부를 확인한다.

### 003. 폰켓몬

* 선택할 수 있는 폰켓몬 수와 실제 종류 수를 비교하는 문제다.
* 중복을 제거하기 위해 `set`을 사용한다.
* 선택 가능한 최대 수는 `len(nums) // 2`이다.
* 정답은 `폰켓몬 종류 수`와 `선택 가능한 수` 중 더 작은 값이다.

### 004. 의상

* 의상 종류별 개수를 세고, 조합의 수를 계산하는 문제다.
* 각 종류마다 입지 않는 경우까지 포함해 `(개수 + 1)`을 곱한다.
* 모든 종류를 선택하지 않는 경우는 제외해야 하므로 마지막에 `-1`을 한다.
* `dict`를 사용해 의상 종류별 개수를 관리한다.

### 005. K번째수

* 배열의 특정 구간을 자르고 정렬한 뒤 k번째 값을 찾는 문제다.
* Python 슬라이싱을 활용해 `array[i-1:j]` 형태로 구간을 자른다.
* 자른 배열을 정렬한 뒤 `k-1`번째 인덱스 값을 answer에 추가한다.
* 인덱스가 0부터 시작한다는 점을 주의해야 한다.

### 006. 가장 큰 수

* 숫자들을 이어 붙였을 때 가장 큰 수를 만드는 문제다.
* 숫자를 문자열로 바꾼 뒤 정렬 기준을 직접 설정해야 한다.
* `key=lambda x: x * 4`를 사용해 문자열 비교 기준을 맞춘다.
* 모든 숫자가 0인 경우 `"000"`이 아니라 `"0"`을 반환해야 한다.

### 007. H-Index

* 논문 인용 횟수를 기준으로 H-Index를 구하는 문제다.
* 인용 횟수를 내림차순 정렬한 뒤, 현재 순위와 인용 횟수를 비교한다.
* `citation >= index` 조건을 만족하는 최대 값을 찾는다.
* 정렬 후 순서대로 확인하면 H-Index 후보를 쉽게 판단할 수 있다.

### 008. 베스트앨범

* 장르별 총 재생 수와 장르별 노래 목록을 함께 관리하는 문제다.
* 먼저 장르별 총 재생 수를 기준으로 장르 순서를 정한다.
* 각 장르 안에서는 재생 수가 높은 노래를 먼저 선택한다.
* 재생 수가 같으면 고유 번호가 낮은 노래를 먼저 선택한다.
* 해시로 데이터를 묶고, 정렬로 선택 순서를 정하는 대표 문제다.

## 사용한 주요 Python 문법

```python
count = {}

count[name] = count.get(name, 0) + 1
```

```python
from collections import Counter

counter = Counter(participant)
```

```python
unique_nums = set(nums)
```

```python
sorted_arr = sorted(arr)
```

```python
arr.sort(reverse=True)
```

```python
arr.sort(key=lambda x: x[1])
```

```python
songs.sort(key=lambda x: (-x[1], x[0]))
```

```python
phone_book[i + 1].startswith(phone_book[i])
```

```python
sliced = array[i - 1:j]
```

```python
answer.append(value)
```

## 복습 포인트

* Hash는 값을 빠르게 찾거나, 개수를 세거나, 중복을 관리할 때 사용한다.
* `dict.get(key, default)`는 key가 없을 때 기본값을 반환한다.
* `set`은 중복 제거가 필요할 때 사용한다.
* `Counter`는 등장 횟수를 간단하게 세고 싶을 때 사용할 수 있다.
* 정렬 문제에서는 먼저 “무엇을 기준으로 정렬할지”를 찾아야 한다.
* `lambda`는 정렬 기준을 짧게 정의할 때 자주 사용한다.
* 튜플을 정렬 기준으로 주면 첫 번째 기준부터 차례대로 비교한다.
* 내림차순이 필요하면 `reverse=True`를 쓰거나, 숫자에 `-`를 붙여 정렬 기준을 만든다.
* 문자열 숫자 정렬 문제에서는 일반 숫자 정렬과 다른 기준이 필요할 수 있다.
* 해시와 정렬이 함께 나오는 문제는 먼저 데이터를 묶고, 이후 조건에 맞게 정렬하는 흐름으로 접근한다.

## 학습 회고

해시/정렬 유형에서는 자료구조와 정렬 기준을 문제 조건에 맞게 바꾸는 연습이 중요했다.

* 완주하지 못한 선수: 이름별 등장 횟수 관리
* 전화번호 목록: 정렬 후 인접한 번호끼리 접두어 확인
* 폰켓몬: 중복 제거 후 선택 가능한 수와 비교
* 의상: 종류별 개수를 세고 조합 계산
* K번째수: 구간 자르기와 정렬
* 가장 큰 수: 문자열 변환 후 lambda 정렬 기준 설정
* H-Index: 정렬 후 순위와 인용 횟수 비교
* 베스트앨범: 장르별 데이터 묶기와 다중 정렬 기준 적용

이번 유형을 통해 `dict`, `get()`, `set`, `Counter`, `sorted()`, `sort()`, `lambda`, `reverse=True`, 슬라이싱, 튜플 정렬에 익숙해졌다.

해시는 “어떤 값을 기준으로 모을 것인가”가 중요했고, 정렬은 “어떤 기준으로 순서를 정할 것인가”가 중요했다.
