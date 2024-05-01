class Solution:
    def rob(self, houses: List[int]) -> int:
        house_current = 0
        house_next = 0
        for house in houses:
            temp = max(house + house_current, house_next)
            house_current = house_next
            house_next = temp
        return house_next