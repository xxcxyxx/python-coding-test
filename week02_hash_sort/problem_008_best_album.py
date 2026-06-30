# 문제: 베스트앨범
# 출처: 프로그래머스
# 유형: 해시, 정렬
#
# 풀이 핵심:
# 1. 장르별 총 재생 수를 딕셔너리에 저장한다.
# 2. 장르별 노래 정보를 딕셔너리에 저장한다.
# 3. 총 재생 수가 높은 장르부터 확인한다.
# 4. 각 장르 안에서는 재생 수가 높은 노래를 최대 2개 선택한다.
# 5. 재생 수가 같으면 고유 번호가 낮은 노래를 먼저 선택한다.


def solution(genres, plays):
    answer = []

    # 장르별 총 재생 수
    genre_total = {}

    # 장르별 노래 목록
    # 예: {"classic": [(0, 500), (2, 150), (3, 800)]}
    genre_songs = {}

    # 1. 장르별 총 재생 수와 노래 목록 만들기
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        # 장르별 총 재생 수 누적
        genre_total[genre] = genre_total.get(genre, 0) + play

        # 장르가 처음 나오면 빈 리스트 생성
        if genre not in genre_songs:
            genre_songs[genre] = []

        # 해당 장르에 노래 정보 추가
        # i는 고유 번호, play는 재생 수
        genre_songs[genre].append((i, play))

    # 2. 총 재생 수가 높은 장르 순서대로 정렬
    sorted_genres = sorted(
        genre_total.keys(),
        key=lambda genre: genre_total[genre],
        reverse=True
    )

    # 3. 장르별로 노래를 정렬하고 최대 2개씩 선택
    for genre in sorted_genres:
        songs = genre_songs[genre]

        # 재생 수는 내림차순, 고유 번호는 오름차순
        songs.sort(key=lambda x: (-x[1], x[0]))

        # 각 장르에서 최대 2곡만 선택
        for song in songs[:2]:
            song_index = song[0]
            answer.append(song_index)

    return answer
