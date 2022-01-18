from typing import List


def isValidSudoku(board: List[List[str]]):

    for i in board: 
        if checkValid(i) == False:
            return False
    for i in changeBoard(board):
        if checkValid(i) == False:
            return False
    for i in groupBoard(board):
        if checkValid(i) == False:
            return False
    return True

def changeBoard(board: List[List[str]]):
    changed = [[] for i in range(9)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            changed[i].append(board[j][i])
    return changed

def groupBoard(board: List[List[str]]):
    grouped = [[] for i in range(9)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            grouped[3*(i // 3) + (j // 3)].append(board[i][j])
    return grouped

def checkValid(target: List[str]) -> bool :
    check = [0 for i in range(9)]
    for i in target:
        if i != ".":
            if check[int(i)-1] == 1:
                return False
            check[int(i)-1] += 1
    return True


tk =[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(tk))
