def NQueens(self, n: int):
    res = []
    
    def nQueensHelper(curr, r):
        if r >= n:
            addToBoard(curr)
            return
        for i in range(n):
            placeable = True
            for row in range(r):
                if (curr[row] == i) or (curr[row] == (r - row) + i) or (curr[row] == i - (r - row)):
                    placeable = False
                    
            if placeable:
                curr[r] = i
                nQueensHelper(curr, r + 1)
    
    def addToBoard(arrangement):
        rep = []
        for i in range(n):
            row = ""
            for c in range(n):
                if arrangement[i] == c:
                    row += "Q"
                else:
                    row += "."
                    
            rep.append(row)
        
        res.append(rep)
            
    test = [float("inf")] * n
    for c in range(n):
        test[0] = c
        nQueensHelper(test, 1)
        
    return res