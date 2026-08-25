class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        table = {}
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1

        sorted_items = sorted(
            table.items(),
            key=lambda item: (item[1], -item[0]),
            )
        output = []
        
        for item in sorted_items:
            for freq in range(item[1]):
                output.append(item[0])

        
        return output