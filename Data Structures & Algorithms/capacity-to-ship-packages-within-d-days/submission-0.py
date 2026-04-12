class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        def canShip(cap):
            s, curr = 1, cap
            for w in weights:
                if curr - w <0:
                    s+=1
                    if s> days:
                        return False
                    curr = cap
                curr -=w
            return True

        while l<=r:
            m = l + ((r-l)//2)
            if canShip(m):
                res = min(res, m)
                r=m-1
            else:
                l = m+1
        return res