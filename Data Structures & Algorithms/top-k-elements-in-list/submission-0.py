class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_list = {}
        output = []
        for key, value in enumerate(nums):
            if value in counter_list:
                counter_list[value] += 1
            else:
                counter_list[value] = 1

        sorted_items = sorted(counter_list.items(), key = lambda item: item[1], reverse=True)
        output = [item[0] for item in sorted_items[:k]]
        
        return output