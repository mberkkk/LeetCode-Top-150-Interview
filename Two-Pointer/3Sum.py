class Solution(object):
    def threeSum(nums):
        solution_list = []
        target = 0
        nums.sort()
        total = 0
        for i in range(len(nums) -2):
            # aynı sayıları geçmek için
            # javadaki gibi i'yi 1 artırmak pythonda işe yaramadığından continue mantıklı bir kullanım
            if i > 0 and nums[i] == nums [i-1]:
                continue

            r = len(nums) -1
            l = i + 1

            while (l < r):
                total = nums[i] + nums[l] + nums[r]

                if total < target:
                    l += 1

                elif total > target:
                    r -=1

                else:
                    solution = [nums[i], nums[l], nums[r]]
                    solution_list.append(solution)
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

        return solution_list


    nums = [-1,0,1,-4]

    print(threeSum(nums))