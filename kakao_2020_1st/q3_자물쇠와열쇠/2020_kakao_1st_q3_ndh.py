def rotate_90(old_key):
    N = len(old_key)
    new_key = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            new_key[col][N-1-row] = old_key[row][col]
    return new_key


def check_unlock(arr, len_lock, len_key):
    for row in range(len_lock):
        for col in range(len_lock):
            if arr[len_key-1+row][len_key-1+col] != 1:
                return False
    return True


def solution(key, lock):
    ex_len = (len(key)-1)*2 + len(lock)
    mid_len = ex_len-(len(key)-1)

    # 새 배열
    new_arr = [[0 for col in range(ex_len)] for row in range(ex_len)]

    # 중간에 Lock 값 넣기
    for i in range(len(lock)):
        for j in range(len(lock)):
            new_arr[i+(len(key)-1)][j+(len(key)-1)] = lock[i][j]

    # 회전말고, 그냥 열쇠범위로 확장된 배열 돌기

    for rotation in range(4):
        key = rotate_90(key)
        for y in range(mid_len):
            for x in range(mid_len):
                # Lock에 Key를 맞춰본다
                for a in range(len(key)):
                    for b in range(len(key)):
                        new_arr[y+a][x+b] += key[a][b]
                # Unlock이 되었는지 확인한다
                if check_unlock(new_arr, len(lock), len(key)) == True:
                    return True
                # Lock에 Key를 뺀다
                for a in range(len(key)):
                    for b in range(len(key)):
                        new_arr[y+a][x+b] -= key[a][b]

  # Key 값을 넣었을 때 Lock 부분이 전체  1이면 True
  # 없을 시 90도로 Key를 회전시켜 다시 진행
  # 끝까지 돌았음에도 없음 False

    return False
