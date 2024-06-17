class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_hash = {}
        for candy in candyType:
            if candy not in candy_hash:
                candy_hash[candy] = 1
            else:
                candy_hash[candy] += 1
        return min(len(candy_hash),len(candyType)//2)