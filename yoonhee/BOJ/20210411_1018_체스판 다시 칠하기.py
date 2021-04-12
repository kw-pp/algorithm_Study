import sys
input = sys.stdin.readline

case1 = [["W","B","W","B","W","B","W","B"],
         ["B","W","B","W","B","W","B","W"],
         ["W","B","W","B","W","B","W","B"],
         ["B","W","B","W","B","W","B","W"],
         ["W","B","W","B","W","B","W","B"],
         ["B","W","B","W","B","W","B","W"],
         ["W","B","W","B","W","B","W","B"],
         ["B","W","B","W","B","W","B","W"]]

case2 = [["B","W","B","W","B","W","B","W"],
         ["W","B","W","B","W","B","W","B"],
         ["B","W","B","W","B","W","B","W"],
         ["W","B","W","B","W","B","W","B"],
         ["B","W","B","W","B","W","B","W"],
         ["W","B","W","B","W","B","W","B"],
         ["B","W","B","W","B","W","B","W"],
         ["W","B","W","B","W","B","W","B"]]
'''
col, row = map(int,input().split())
board = [list(input()) for _ in range(col)]
'''
N,M = map(int, input().split())
board = [list(input()) for _ in range(N)]

def compare(case1, case2, board):
    cnt_w = 0
    cnt_b = 0
    for i in range(8):
        for j in range(8):
            if case1[i][j] != board[i][j]:
                cnt_w += 1
            if case2[i][j] != board[i][j]:
                cnt_b += 1
    return min(cnt_w, cnt_b)

min_answer = 64

for x in range(0, N-7):
    for y in range(0, M-7):
        second_map = []
        second_map.append(board[x][y:y+8])
        second_map.append(board[x+1][y:y+8])
        second_map.append(board[x+2][y:y+8])
        second_map.append(board[x+3][y:y+8])
        second_map.append(board[x+4][y:y+8])
        second_map.append(board[x+5][y:y+8])
        second_map.append(board[x+6][y:y+8])
        second_map.append(board[x+7][y:y+8])

        answer = compare(case1, case2, second_map)
        if min_answer > answer :
            min_answer = answer

        second_map.clear()

print(min_answer)
                
                

