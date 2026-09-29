class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_matrix = []
        for inner_list in matrix:
            for num in inner_list:
                flat_matrix.append(num)

        LOW, HIGH = 0, len(flat_matrix)
        while LOW < HIGH:
            MID = (LOW + HIGH) // 2
            if flat_matrix[MID] == target:
                return True
            elif flat_matrix[MID] < target:
                LOW = MID + 1
            else:
                HIGH = MID
        return False