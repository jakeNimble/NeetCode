class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}  #empty dict
        for j, num in enumerate(nums): #use enumerate to iterate over indices for a list
            goal = target - num  #the number we are looking for or our "compliment" number
            if goal in numMap:
                if j < numMap[goal]:
                    return [j, numMap[goal]]
                else:
                    return [numMap[goal], j]
            numMap[num] = j #if goal isn't found at it to hashmap/dict
