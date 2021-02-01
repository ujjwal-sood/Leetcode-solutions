class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        
        def f(arr,row,col,flag):
            if row<0 or col<0 or row>=m or col>=n:
                return
            if arr[row][col]==-1 or arr[row][col]=="0":
                return
            if flag==False and arr[row][col]=="1":
                flag=True
            
            arr[row][col]=-1
            
            f(arr,row-1,col,flag)
            f(arr,row,col-1,flag)
            f(arr,row+1,col,flag)
            f(arr,row,col+1,flag)
            
            flag=True
    
        islands=0
        for i in range(m): 
            for j in range(n):
                if grid[i][j]=="1":
                    islands+=1
                    f(grid,i,j,False)
        return islands