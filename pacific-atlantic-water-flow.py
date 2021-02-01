class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def dfs(matrix, row, col, preVal, ocean):
            # Base Cases:
            if row < 0 or col < 0 or row >= m or col >= n:
                return 
            elif matrix[row][col] < preVal:
                return
            elif ocean[row][col] == 1:
                return
            
            # TO DO
            ocean[row][col] = 1
            
            # Traverse in other directions
            dfs(matrix, row+1, col, matrix[row][col], ocean)
            dfs(matrix, row, col-1, matrix[row][col], ocean)
            dfs(matrix, row-1, col, matrix[row][col], ocean)
            dfs(matrix, row, col+1, matrix[row][col], ocean)
            
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        pacific = [[0 for i in range(n)]for j in range(m)]
        atlantic = [[0 for i in range(n)]for j in range(m)]
        
        # Top-Pacific and Bottom-Atlantic
        for i in range(n):
            dfs(matrix, 0, i, float('-inf'), pacific)
            dfs(matrix, m-1, i, float('-inf'), atlantic)
            
        # Left-Pacific and Right-Atlantic
        for i in range(m):
            dfs(matrix, i, 0, float('-inf'), pacific)
            dfs(matrix, i, n-1, float('-inf'), atlantic)

        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    result.append([i,j])
                
        return result