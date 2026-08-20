class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        last1, last2 = nums[0], nums[1]
        n = len(nums)

        for i in range(2, n):
            num = nums[i]
            
            if last1 > last2:
                arr1.append(num)
                last1 = num
            else:
                arr2.append(num)
                last2 = num
        
        return arr1 + arr2
