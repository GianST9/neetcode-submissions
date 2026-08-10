class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip("?")
        s = s.replace(" ", "")
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        print(cleaned)
        return (cleaned == cleaned[::-1])