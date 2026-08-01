class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)

        l, r = 0, m * n - 1

        while l <= r:
            print(l, r)
            mid = ((r - l) // 2) + l
            mid_m = mid // m
            mid_n = mid % m

            print(mid, mid_m, mid_n)
            print(matrix[mid_m][mid_n])

            if matrix[mid_m][mid_n] > target:
                r = mid - 1
            elif matrix[mid_m][mid_n] < target:
                l = mid + 1
            else:
                return True

        return False