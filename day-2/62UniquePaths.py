class Solution:
    def helper(self,row,col,m,n,dp):
        if row == 0 and col == 0:
            return 1
        elif row < 0 or row>m or col < 0 or col > n:
            return 0

        if dp[row][col] !=-1:
            return dp[row][col]

        row_mov = self.helper(row,col-1,m,n,dp)
        col_mov = self.helper(row-1,col,m,n,dp)
        dp[row][col] = row_mov+col_mov


        return dp[row][col]
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for j in range(m)]
        return self.helper(m-1,n-1,m,n,dp)
