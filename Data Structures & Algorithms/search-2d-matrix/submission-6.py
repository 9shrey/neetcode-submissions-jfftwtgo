class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        lis = [element for row in matrix for element in row]
        r = len(lis) - 1
        while l<=r:
            m = l + ((r-l)//2)
            if target == lis[m]:
                return True
            elif target > lis[m]:
                l = m+1
            else:
                r = m-1
        return False