class ThreeSum:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        index_map = {}
        for i in range(0 , len(nums)):
            index_map[nums[i]] = i
        
        result = set()
        for i in range(0 , len(nums)):
            target = nums[i]
            for j in range(0, len(nums)):
                n = target - nums[j]
                if index_map.get(n) != None and j != index_map.get(n) and target + n + index_map.get(n) == 0:
                    print(target , " " , n , " ", index_map.get(n))
                    result.update([target , n , index_map.get(n)])

        return list(result)
    

threeSum = ThreeSum()
result = threeSum.threeSum([-1,0,1,2,-1,-4])   
for num in result:
    print(num) 