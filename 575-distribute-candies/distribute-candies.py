class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)//2
        candy_hash = {}
        for candy in candyType:
            if candy not in candy_hash:
                candy_hash[candy] = 1
            else:
                candy_hash[candy] += 1
        x = len(candy_hash)
        if x<=n:
            return x
        else:
            return n