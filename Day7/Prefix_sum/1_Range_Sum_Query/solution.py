class NumArray(object):

    def __init__(self, nums):
        n = len(nums)
        self.prefix = [0] * (n+1)
        for i in range (n):
            self.prefix[i+1] = self.prefix[i] + nums[i]
        

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)