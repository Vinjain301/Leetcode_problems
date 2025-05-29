class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target=float(inf)
        nums=sorted(nums)
        seen=set()
        i=0
        while i<len(nums):
            if i > 0 and nums[i]==nums[i-1]:
                i+=1
                continue
            target=nums[i]
            j,k=i+1,len(nums)-1
            while j<k:
                if nums[j] + nums[k] == -target:
                    seen.add((target, nums[j], nums[k]))
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -target:
                    j += 1
                else:
                    k -= 1
            i+=1
        return sorted([list(triplet) for triplet in seen])
                        




            

            




        