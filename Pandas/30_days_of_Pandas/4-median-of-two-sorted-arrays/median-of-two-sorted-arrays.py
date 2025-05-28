class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        x,y=len(nums1),len(nums2)
        low,high=0,x
        while low<=high:
            partitionx=(low+high)//2
            partitiony=(x+y+1)//2-partitionx
            maxleftx=float(-inf) if partitionx==0 else nums1[partitionx-1]
            minrightx=float(inf) if partitionx==x else nums1[partitionx]
            maxlefty=float(-inf) if partitiony==0 else nums2[partitiony-1]
            minrighty=float(inf) if partitiony==y else nums2[partitiony]
            if maxleftx<=minrighty and maxlefty<=minrightx:
                if (x+y)%2==0:
                    return ((max(maxleftx,maxlefty)+min(minrightx,minrighty))/2)
                else:
                    return max(maxleftx,maxlefty)
            elif maxleftx>minrighty:
                high=partitionx-1
            else:
                low=partitionx+1