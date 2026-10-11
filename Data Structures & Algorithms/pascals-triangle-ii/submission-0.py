class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [1]
        for current_row in range(1, rowIndex + 1):
            output.append(1)
            for j in range(current_row - 1, 0, -1):
                [1,1,1]
                output[j] = output[j - 1] + output[j]
        return output