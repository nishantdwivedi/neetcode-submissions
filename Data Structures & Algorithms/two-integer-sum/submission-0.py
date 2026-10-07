class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        freq = {}
        count = -1
        for num in nums:
            count = count + 1
            if target - num in freq:
                answer.append(freq.get(target - num))
                answer.append(count)
                return answer
            else:
                freq[num] = count
        return answer
        