# Week 02 - Hash & Sort

## 학습 목표

* `dict`, `set`을 활용해 탐색 시간을 줄인다.
* 중복 여부, 등장 횟수, 종류 개수를 빠르게 판단하는 방법을 익힌다.
* `get()`, `items()`, `values()`를 사용해 딕셔너리를 다루는 방법을 익힌다.
* `sorted()`, `reverse=True`, `lambda`를 활용해 원하는 기준으로 정렬한다.
* 문자열 슬라이싱과 문자열 변환을 활용한 정렬 문제 풀이를 연습한다.
* 문제 조건을 코드의 정렬 기준이나 자료구조 선택으로 바꾸는 연습을 한다.

## 핵심 개념

* Hash
* `dict`
* `set`
* `get()`
* `items()`
* `values()`
* `min()`
* 문자열 슬라이싱
* `sorted()`
* `reverse=True`
* `map()`
* `lambda`
* `enumerate()`
* `break`
* 등장 횟수 세기
* 중복 제거
* 정렬 기준 직접 설정

## 문제 목록

| 번호  | 문제명        | 유형                                         | 난이도     | 상태     | 파일                                                                     |
| --- | ---------- | ------------------------------------------ | ------- | ------ | ---------------------------------------------------------------------- |
| 001 | 완주하지 못한 선수 | Hash / Dictionary / Counting               | Level 1 | Solved | [problem_001_unfinished_runner.py](./problem_001_unfinished_runner.py) |
| 002 | 전화번호 목록    | Hash / Set / String                        | Level 2 | Solved | [problem_002_phone_book.py](./problem_002_phone_book.py)               |
| 003 | 폰켓몬        | Hash / Set / Greedy                        | Level 1 | Solved | [problem_003_pokemon.py](./problem_003_pokemon.py)                     |
| 004 | 의상         | Hash / Dictionary / Counting / Combination | Level 2 | Solved | [problem_004_clothes.py](./problem_004_clothes.py)                     |
| 005 | K번째수       | Sort / List Slicing                        | Level 1 | Solved | [problem_005_kth_number.py](./problem_005_kth_number.py)               |
| 006 | 가장 큰 수     | Sort / Lambda / String                     | Level 2 | Solved | [problem_006_largest_number.py](./problem_006_largest_number.py)       |
| 007 | H-Index    | Sort / Enumeration                         | Level 2 | Solved | [problem_007_h_index.py](./problem_007_h_index.py)                     |

## 문제별 핵심 정리

### 001. 완주하지 못한 선수

* 참가자 명단과 완주자 명단을 비교해 완주하지 못한 한 명을 찾는 문제다.
* 동명이인이 있을 수 있으므로 이름별 등장 횟수를 세어야 한다.
* `dict`를 사용해 참가자 이름별 인원수를 저장한다.
* 참가자 명단을 순회하면서 이름이 나올 때마다 `+1` 한다.
* 완주자 명단을 순회하면서 완주한 이름은 `-1` 한다.
* 마지막에 `count.items()`를 순회하며 값이 `1`인 이름을 반환한다.

핵심 코드:

```python
count[name] = count.get(name, 0) + 1
```

```python
for name, number in count.items():
    if number == 1:
        return name
```

---

### 002. 전화번호 목록

* 한 전화번호가 다른 전화번호의 접두사인지 확인하는 문제다.
* 빠른 존재 여부 확인을 위해 `phone_book`을 `set`으로 변환한다.
* 각 전화번호를 하나씩 확인하면서 앞에서부터 잘라 접두사를 만든다.
* `phone[:i]`를 사용해 문자열의 앞부분을 만든다.
* 만든 접두사가 `phone_set` 안에 있으면 접두어 관계가 있으므로 `False`를 반환한다.
* 자기 자신과 비교하면 안 되므로 `range(1, len(phone))`까지만 확인한다.
* 모든 전화번호를 확인해도 접두사가 없으면 `True`를 반환한다.

핵심 코드:

```python
phone_set = set(phone_book)
```

```python
for i in range(1, len(phone)):
    prefix = phone[:i]

    if prefix in phone_set:
        return False
```

---

### 003. 폰켓몬

* 전체 폰켓몬 중 절반만 선택할 수 있을 때, 최대한 다양한 종류를 선택하는 문제다.
* 선택할 수 있는 폰켓몬 수는 `len(nums) // 2`이다.
* 실제 폰켓몬 종류 수는 `len(set(nums))`로 구한다.
* 선택 가능한 수보다 종류가 많아도 모두 선택할 수는 없다.
* 따라서 선택 가능한 수와 실제 종류 수 중 작은 값을 반환한다.

핵심 코드:

```python
select_count = len(nums) // 2
type_count = len(set(nums))

return min(select_count, type_count)
```

---

### 004. 의상

* 의상 종류별 개수를 세고 가능한 조합 수를 구하는 문제다.
* `dict`를 사용해 의상 종류별 개수를 저장한다.
* 각 종류마다 의상을 하나 선택하거나, 선택하지 않는 경우가 있다.
* 따라서 각 종류별 선택지는 `개수 + 1`개이다.
* 모든 종류의 선택지 수를 곱한다.
* 아무 의상도 입지 않는 경우가 포함되므로 마지막에 `-1`을 한다.

핵심 코드:

```python
clothes_count[category] = clothes_count.get(category, 0) + 1
```

```python
answer = 1

for count in clothes_count.values():
    answer *= count + 1

return answer - 1
```

---

### 005. K번째수

* 배열의 특정 구간을 자르고 정렬한 뒤 k번째 값을 찾는 문제다.
* `commands`에서 `i, j, k`를 하나씩 꺼낸다.
* 문제의 위치는 1부터 시작하지만, Python 리스트 인덱스는 0부터 시작한다.
* 따라서 배열을 자를 때 시작 위치는 `i - 1`을 사용한다.
* 정렬한 배열에서 k번째 값은 `k - 1` 인덱스에 있다.
* 결과를 `answer` 리스트에 추가한다.

핵심 코드:

```python
for i, j, k in commands:
    sorted_array = sorted(array[i - 1:j])
    answer.append(sorted_array[k - 1])
```

---

### 006. 가장 큰 수

* 숫자들의 순서를 재배치해 만들 수 있는 가장 큰 수를 구하는 문제다.
* 숫자를 이어 붙여 비교해야 하므로 먼저 문자열로 변환한다.
* `map(str, numbers)`를 사용해 숫자 리스트를 문자열 리스트로 바꾼다.
* 각 숫자는 최대 1000이므로, 문자열을 4번 반복한 값을 기준으로 정렬한다.
* `key=lambda x: x * 4`와 `reverse=True`를 사용해 큰 수가 되도록 정렬한다.
* 정렬 후 첫 번째 값이 `'0'`이면 모든 값이 0이므로 `'0'`을 반환한다.
* 그렇지 않으면 정렬된 문자열을 이어 붙여 반환한다.

핵심 코드:

```python
numbers = list(map(str, numbers))

sorted_numbers = sorted(
    numbers,
    key=lambda x: x * 4,
    reverse=True
)
```

```python
if sorted_numbers[0] == '0':
    return '0'

return ''.join(sorted_numbers)
```

---

### 007. H-Index

* 논문별 인용 횟수를 기준으로 H-Index를 구하는 문제다.
* 먼저 인용 횟수를 내림차순으로 정렬한다.
* `enumerate(sorted_citations, start=1)`을 사용해 현재까지 확인한 논문 수와 인용 횟수를 함께 본다.
* 현재 논문의 인용 횟수가 현재 논문 수 이상이면 H-Index 후보로 저장한다.
* 조건을 만족하지 못하면 이후 인용 횟수는 더 작으므로 반복을 종료한다.
* 마지막으로 저장된 `h_index`를 반환한다.

핵심 코드:

```python
sorted_citations = sorted(citations, reverse=True)
h_index = 0

for paper_count, citation in enumerate(sorted_citations, start=1):
    if citation >= paper_count:
        h_index = paper_count
    else:
        break

return h_index
```

## 사용한 주요 Python 문법

### 딕셔너리 기본값 처리

```python
count[name] = count.get(name, 0) + 1
```

```python
clothes_count[category] = clothes_count.get(category, 0) + 1
```

### 딕셔너리 순회

```python
for name, number in count.items():
    ...
```

```python
for count in clothes_count.values():
    ...
```

### set으로 중복 제거 및 빠른 탐색

```python
phone_set = set(phone_book)
```

```python
type_count = len(set(nums))
```

### 문자열 슬라이싱

```python
prefix = phone[:i]
```

### 리스트 슬라이싱과 정렬

```python
sorted_array = sorted(array[i - 1:j])
```

### 문자열 변환

```python
numbers = list(map(str, numbers))
```

### lambda 정렬 기준

```python
sorted_numbers = sorted(
    numbers,
    key=lambda x: x * 4,
    reverse=True
)
```

### 내림차순 정렬

```python
sorted_citations = sorted(citations, reverse=True)
```

### enumerate로 순서와 값 함께 사용

```python
for paper_count, citation in enumerate(sorted_citations, start=1):
    ...
```

### 조건을 만족하지 않으면 반복 종료

```python
else:
    break
```

## 복습 포인트

* Hash는 값을 빠르게 찾거나, 개수를 세거나, 중복을 관리할 때 사용한다.
* `dict.get(key, 0)`은 처음 등장하는 값을 안전하게 처리할 때 유용하다.
* `set`은 중복 제거와 빠른 존재 여부 확인에 사용한다.
* 전화번호 목록 문제에서는 `startswith()`가 아니라 `phone[:i]`로 직접 접두사를 만들어 확인했다.
* 조합 문제에서는 “선택하지 않는 경우”를 포함해 계산해야 한다.
* 정렬 문제에서는 먼저 “무엇을 기준으로 정렬할지”를 정해야 한다.
* Python 리스트 인덱스는 0부터 시작하므로 문제의 순서가 1부터 시작하면 `-1` 처리가 필요하다.
* 숫자를 이어 붙여 비교하는 문제는 문자열로 바꿔 정렬 기준을 만들어야 한다.
* `lambda`는 정렬 기준을 짧게 정의할 때 사용한다.
* `enumerate(iterable, start=1)`을 사용하면 현재 순서와 값을 함께 다룰 수 있다.
* 정렬 후 더 이상 조건을 만족할 수 없는 상황에서는 `break`로 반복을 종료할 수 있다.

## 학습 회고

해시/정렬 유형에서는 자료구조 선택과 정렬 기준 설정이 중요했다.

* 완주하지 못한 선수: 이름별 등장 횟수를 `dict`로 관리
* 전화번호 목록: `set`과 문자열 슬라이싱으로 접두사 확인
* 폰켓몬: `set`으로 종류 수를 구하고 선택 가능 수와 비교
* 의상: 종류별 개수를 세고 조합 수 계산
* K번째수: 구간을 자르고 정렬한 뒤 k번째 값 선택
* 가장 큰 수: 문자열 변환 후 `lambda`로 정렬 기준 설정
* H-Index: 내림차순 정렬 후 논문 수와 인용 횟수 비교

이번 유형을 통해 `dict`, `get()`, `items()`, `values()`, `set`, `min()`, 슬라이싱, `sorted()`, `map()`, `lambda`, `reverse=True`, `enumerate()`, `break` 사용에 익숙해졌다.

해시는 “어떤 값을 기준으로 모을 것인가”가 중요했고, 정렬은 “어떤 기준으로 순서를 정할 것인가”가 중요했다.
