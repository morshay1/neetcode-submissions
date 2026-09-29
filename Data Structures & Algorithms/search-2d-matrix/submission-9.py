class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        LOW_ROW, HIGH_ROW = 0, len(matrix)
        LOW_COL, HIGH_COL = 0, len(matrix[0])

        while LOW_ROW < HIGH_ROW:
            MID = (LOW_ROW + HIGH_ROW) // 2
            if matrix[MID][LOW_COL] == target or matrix[MID][HIGH_COL - 1] == target:
                return True
            elif matrix[MID][LOW_COL] < target and matrix[MID][HIGH_COL - 1] > target:
                return self.binary_search(matrix[MID], target)
            elif matrix[MID][LOW_COL] < target:
                LOW_ROW = MID + 1
            elif matrix[MID][HIGH_COL - 1] > target:
                HIGH_ROW = MID
        return False

    def binary_search(self, row_array, target):
        low, high = 0, len(row_array)
        while low < high:
            mid = (low + high) // 2
            if row_array[mid] == target:
                return True
            elif row_array[mid] < target:
                low = mid + 1
            else:
                high = mid
        return False




        # flat_matrix = []
        # for inner_list in matrix:
        #     for num in inner_list:
        #         flat_matrix.append(num)

        # LOW, HIGH = 0, len(flat_matrix)
        # while LOW < HIGH:
        #     MID = (LOW + HIGH) // 2
        #     if flat_matrix[MID] == target:
        #         return True
        #     elif flat_matrix[MID] < target:
        #         LOW = MID + 1
        #     else:
        #         HIGH = MID
        # return False