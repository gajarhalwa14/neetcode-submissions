class Solution:

    def binarySearch(self, numbers: List[int], target: int) -> int:
        first, last = 0, len(numbers) - 1
        while first <= last:
            mid = (first + last) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] > target:
                last = mid - 1
            else:
                first = mid + 1
        
        return -1
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Input is sorted in non-decreasing (ascending) order
        # Use Binary Search
        # Iterate through list. Take number, search list for target - number
        # Use binary search for efficiency O(logn)
        # If target - number doesn't exist, we can eliminate two numbers
        # Each number is accessed once at most

        firstIdx, secondIdx = 0, 0
        for index, val in enumerate(numbers):
            searchTarget = target - val
            retVal = self.binarySearch(numbers, searchTarget)
            if retVal == -1:
                continue
            else:
                firstIdx = index + 1
                secondIdx = retVal + 1
                break
        
        return [firstIdx, secondIdx]
                 
            
        