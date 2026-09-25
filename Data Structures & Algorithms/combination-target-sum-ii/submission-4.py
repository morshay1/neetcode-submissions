class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.helper(candidates, target)


    def helper(self, candidates, target):
        output = []
        if target == 0:
            return [[]]

        if len(candidates) == 0 or target < 0:
            return output

        if len(candidates) == 1:
            if candidates[0] == target:
                output.append([target])
            return output

        with_first = self.helper(candidates[1::], target - candidates[0])
        with_first = [[candidates[0]] + lst for lst in with_first]
        
        idx = 0
        diff_idx = 1
        while diff_idx < len(candidates) and candidates[idx] == candidates[diff_idx]:
            idx += 1
            diff_idx += 1
                
        without_first = self.helper(candidates[diff_idx::], target)

        return with_first + without_first