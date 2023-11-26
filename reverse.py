from typing import List

class Solution:
    def reverse(self,num: List[int]) -> int:
        # num.reverse()
        start=0
        end=len(num)-1
        #i=0;i<len/2
        while start<end:  
            temp=num[start]
            num[start]=num[end]
            num[end]=temp
            start+=1
            end-=1
        return num
s=Solution()
answer=s.reverse([3,2,2,1])
print(answer)