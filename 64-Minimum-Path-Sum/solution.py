class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(grid,step,sum_path,res,row_idx,col_idx):
            row=len(grid)
            col=len(grid[0])
            
            if row_idx<0 or row_idx==row or col_idx<0 or col_idx==col:
                return 
            
            if step==row+col-2:
                res.append(sum_path+grid[row_idx][col_idx])
                
            dfs(grid,step+1,sum_path+grid[row_idx][col_idx],res,row_idx,col_idx+1)
            dfs(grid,step+1,sum_path+grid[row_idx][col_idx],res,row_idx+1,col_idx)
            
        res=[]
        dfs(grid,0,0,res,0,0)
        return min(res)
        
        