class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        solution = []
        pointer = 1
        for i in range(n):
            solution.append(pointer)
            if pointer * 10 <= n:
                pointer *= 10
            else:
                if pointer >= n:
                    pointer //= 10
                pointer += 1
                while pointer % 10 == 0:
                    pointer //= 10
        return solution         