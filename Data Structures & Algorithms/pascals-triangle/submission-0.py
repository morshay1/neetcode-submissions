class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]

        for i in range(1, numRows):
            new_row = output[-1][:]
            new_row.append(1)
            for j in range(1, i):
                new_row[j] = output[i - 1][j - 1] + output[i - 1][j]
            output.append(new_row)

        return output
