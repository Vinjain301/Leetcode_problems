class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while i<len(arr):
            j=len(arr)-2
            if arr[i]==0:
                while j>i:
                    arr[j+1]=arr[j]
                    j-=1
                arr[j+1]=0
                i+=2
                continue
            i+=1

                

        