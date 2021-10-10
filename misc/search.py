""" Search algorithms implemented in pure python3. """

class Search:
    @staticmethod
    def binary_search(nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif target > middle:
                left = middle + 1
            else:
                right = middle - 1

        return None

if __name__ == '__main__':
    nums = [1, 2, 2, 2, 3, 4, 7, 8, 99]
    target = 2
    ans = Search.binary_search(nums, target)
    print(ans)