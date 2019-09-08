#!/bin/env python3
#-*- coding: utf8 -*-
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        result = []
        for i in range(0, len(nums)):
            needNum = target - nums[i]
            index = numMap.get(needNum, None)
            if index is None:
                numMap[nums[i]] = i
            else:
                result.append(i)
                result.append(index)
                return result
        return result

if __name__ == "__main__":
    nums = [7, 11, 2, 15, -1, 10, 20, 4]
    target = 19
    result = Solution().twoSum(nums, target)
    print(result)