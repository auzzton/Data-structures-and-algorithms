class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf') #setting a random value


        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: #checking for duplicates
                continue

            low, high = i+1, len(nums)-1 #initialising 2 pointers

            while low < high:
                currsum = nums[i] + nums[low] + nums[high] #Calculating 3sum

                if abs(currsum - target) < abs(closest - target):
                    closest = currsum

                if currsum == target:
                    return currsum
                elif currsum < target:
                    low += 1
                else:
                    high-=1
            
        return closest

                
                


            