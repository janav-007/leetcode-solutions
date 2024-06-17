class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c))
        while l<=r:
            num = l*l + r*r
            if num == c:
                return True
            elif num < c:
                l += 1
            else:
                r -= 1
        return False