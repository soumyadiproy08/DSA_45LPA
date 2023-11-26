from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        print(nums)
        return k

        


s=Solution()
answer1=s.removeElement([3,2,2,3],3)
answer2=s.removeElement([0,1,2,2,3,0,4,2],2)
print(answer1)     
print(answer2)   