# problem to solve: https://leetcode.com/problems/minimum-pair-removal/
import heapq

class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        left = list(range(-1, n - 1))
        right = list(range(1, n + 1))
        right[-1] = -1

        alive = [True] * n

        # count of decreasing pairs
        bad = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                bad += 1

        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i, i + 1))

        ops = 0

        while bad > 0:
            s, i, j = heapq.heappop(heap)

            if not (alive[i] and alive[j] and right[i] == j):
                continue

            li = left[i]
            rj = right[j]

            # remove old disorder contributions
            if li != -1 and nums[li] > nums[i]:
                bad -= 1
            if nums[i] > nums[j]:
                bad -= 1
            if rj != -1 and nums[j] > nums[rj]:
                bad -= 1

            # merge
            nums[i] += nums[j]
            alive[j] = False

            right[i] = rj
            if rj != -1:
                left[rj] = i

            # add new disorder contributions
            if li != -1 and nums[li] > nums[i]:
                bad += 1
            if rj != -1 and nums[i] > nums[rj]:
                bad += 1

            # push new adjacent sums
            if li != -1:
                heapq.heappush(heap, (nums[li] + nums[i], li, i))
            if rj != -1:
                heapq.heappush(heap, (nums[i] + nums[rj], i, rj))

            ops += 1

        return ops