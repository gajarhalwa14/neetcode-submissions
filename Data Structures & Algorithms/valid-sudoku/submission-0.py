class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check all rows
        for row in board:
            rowDict = defaultdict(int)
            for char in row:
                if char == ".":
                    continue
                if rowDict[char] == 1:
                    return False
                rowDict[char] = 1;

        # Check all columns
        for i in range(len(board[0])):
            colDict = defaultdict(int)
            for row in board: 
                colChar = row[i]
                if colChar == ".":
                    continue
                if colDict[colChar] == 1:
                    return False
                colDict[colChar] = 1

        squaresDict = [defaultdict(int) for _ in range(9)]
        # Check all squares
        for row in range(len(board)):
            for col in range(len(board[0])):
                char = board[row][col]
                if char == ".":
                    continue
                squareIdx = int(row / 3) * 3 + int(col / 3)
                if squaresDict[squareIdx][char] == 1:
                    return False
                squaresDict[squareIdx][char] = 1
        

        return True
