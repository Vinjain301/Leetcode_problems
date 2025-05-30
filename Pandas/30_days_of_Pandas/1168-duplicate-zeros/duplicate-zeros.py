class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        i=0
        count=0
        for num in arr:
            if num==0:
                count+=1
        if count>0:
            i=n-1
            j=n-1+count
            while j>i:
                if j<n:
                    arr[j]=arr[i]
                if arr[i]==0:
                    j-=1
                    if j<n:
                        arr[j]=0
    
                    
                i-=1
                j-=1
                

    


                

        