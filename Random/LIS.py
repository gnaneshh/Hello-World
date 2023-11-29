def LIS(nums, index, prev, dp):
    if index < 0:
        return 0
    if dp[index] != -1:
        return dp[index]

    take = 0
    if nums[index] < prev:
        take = 1 + LIS(nums, index - 1, nums[index], dp)
    notTake = 0 + LIS(nums, index - 1, prev, dp)
    dp[index] = max(take, notTake)
    return dp[index]


nums = [10, 9, 2, 5, 3, 4, 7, 101, 18, 19, 100]
dp = [-1] * len(nums)

print(LIS(nums, len(nums) - 1, float("inf"), dp))
