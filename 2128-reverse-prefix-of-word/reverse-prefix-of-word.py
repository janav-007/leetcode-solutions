class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = ""
        if ch not in word:
            return word
        else:
            count = 0
            for letter in word:
                stack = stack + letter
                count += 1
                if letter == ch:
                    break
            stack = stack[::-1] + word[count:]
            return stack