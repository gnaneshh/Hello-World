# def minimumEnergy(jumps, i, dp):
#     if i == len(jumps) - 1:
#         return 0

#     # Check if the result for this position is already dpized
#     if dp[i] != -1:
#         return dp[i]

#     oneJump = abs(jumps[i] - jumps[i + 1]) + minimumEnergy(jumps, i + 1, dp)
#     twoJump = oneJump
#     if i < len(jumps) - 2:
#         twoJump = abs(jumps[i] - jumps[i + 2]) + minimumEnergy(jumps, i + 2, dp)

#     # Store the result in the dp dictionary
#     dp[i] = min(oneJump, twoJump)
#     return dp[i]


# jumps = [
#     [7, 4, 4, 2, 6, 6, 3, 4],
#     [4, 8, 3, 10, 4, 4],
#     [10, 20, 30, 10],
#     [10, 50, 10],
#     [1, 3, 5, 8, 9],
# ]

# for jump_sequence in jumps:
#     dp = [-1] * len(jump_sequence)
#     result = minimumEnergy(jump_sequence, 0, dp)
#     print(result)


def minimumEnergy(jumps, i, dp):
    print(dp)
    if i == len(jumps) - 1:
        return 0

    # Check if the result for this position is already in the DP array
    if dp[i] != -1:
        return dp[i]

    oneJump = abs(jumps[i] - jumps[i + 1]) + minimumEnergy(jumps, i + 1, dp)
    twoJump = float("inf")
    if i < len(jumps) - 2:
        twoJump = abs(jumps[i] - jumps[i + 2]) + minimumEnergy(jumps, i + 2, dp)

    # Store the result in the DP array
    dp[i] = min(oneJump, twoJump)
    return dp[i]


jumps_list = [
    [7, 4, 4, 2, 6, 6, 3, 4],
    [4, 8, 3, 10, 4, 4],
    [10, 20, 30, 10],
    [10, 50, 10],
    [1, 3, 5, 8, 9],
]

for jumps in jumps_list:
    n = len(jumps)
    dp = [-1] * n  # Initialize the DP array with -1 values
    result = minimumEnergy(jumps, 0, dp)
    print(result)
