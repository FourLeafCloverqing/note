class Solution(object):
    def twoSum(self, nums: list, target: int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return_map = dict()
        for index1, value1 in enumerate(nums):
            # if index1 + 1 == len(nums):
            #     return
            # for index2, value2 in enumerate(nums[index1 + 1:]):
            #     if value1 + value2 == target:
            #         return index1, index1 + index2 + 1
            # for i in (0, len(nums)):
            #     if i + 1 < len(nums):
            #         sumnum = nums[i] + nums[i + 1]
            #         if sumnum == target:
            #             print("第%d位数和第%d位数和为目标值" % (i, (i + 1)))
            #             return i, i + 1
            if value1 in return_map.values():
                return nums.index(target - value1), index1
            return_map[value1] = target - value1



if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 3, 4, 5, 6], 11))




    """
    Python  Tensorflow (或者pytorch） (熟悉一个或多个常见的 NLP/ML/DL 开源工具库，如Caffe、Tensorflow等)
   有大数据处理经验（熟悉Hadoop或者Spark等分布式处理平台.
    
    
    """
