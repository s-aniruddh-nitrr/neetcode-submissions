class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set1 = set()
        set2 = set()
        set3 = set()

        rowset = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rowset:
                        return False
                    rowset.add(board[i][j])
            rowset.clear()

        colset = set()
        for i in range(9):
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in colset:
                        return False
                    colset.add(board[j][i])
            colset.clear()

        for i in range(9):

            if(i%3==0):
                set1.clear()
                set2.clear()
                set3.clear()
            for j in range(0,3):
                if board[i][j] in set1:
                    return False
                if board[i][j] != ".":
                    set1.add(board[i][j])
            for j in range(3,6):
                if board[i][j] in set2:
                    return False
                if board[i][j] != ".":
                    set2.add(board[i][j])
            for j in range(6,9):
                if board[i][j] in set3:
                    return False
                if board[i][j] != ".":
                    set3.add(board[i][j])
        print("final set 1 =", set1)
        print("final set 2 =", set2)
        print("final set 3 =", set3)
        return True 


        