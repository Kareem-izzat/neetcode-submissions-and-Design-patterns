class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map ={}
        bucket=[[] for i in range(len(nums))]
        res=[]
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] = map[i] + 1

        for key,value in map.items():
            bucket[value-1].append(key)

        for i in range(len(bucket)-1 ,-1,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        

        