class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += str(len(word)) + "#" + word
        
        print(output)
        return output


    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            # Find the '#'
            j = i
            while s[j] != "#":
                j += 1

            # Get the length of the word
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Extract the word
            word = s[j:j + length]
            output.append(word)

            # Move to the beginning of the next encoded word
            i = j + length

        return output