class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def goldStart(grid, width, lenth, get):
            if len(grid) - 1 < lenth or lenth < 0:
                return get
            elif len(grid[lenth])- 1 < width or width < 0:
                return get
            elif grid[lenth][width] == 0:
                return get
            else:
                
                get = get + grid[lenth][width]
                save = grid[lenth][width]
                grid[lenth][width] = 0
                
                e = goldStart(grid, width+1, lenth ,get)
            
                s = goldStart(grid, width, lenth+1, get)

                w = goldStart(grid, width-1, lenth, get)
                
                n = goldStart(grid, width, lenth-1, get)
                
                grid[lenth][width] = save
                get = max(e,w,s,n)
                return get

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res = max(res,goldStart(grid,j,i,0))
        return res
