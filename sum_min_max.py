from typing import List

class Solution:
    def sum_min_max(self,num: List[int],N: int) -> int:
        if N==0:
            return 0
        else:
            i=0
            min=max=num[0]
            while(i<N):
                if(num[i]>max):
                    max=num[i]
                if(num[i]<min):
                    min=num[i]
                i+=1
            return min+max
        
s=Solution()
answer=s.sum_min_max([],0)
print(answer)