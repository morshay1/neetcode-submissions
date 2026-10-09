class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        digits_letters_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        for digit in digits:
            new_output = []
            for letter in digits_letters_map[digit]:
                if len(output) == 0:
                    new_output.append(letter)
                else:
                    new_output += [word + letter for word in output]
            output = new_output
        
        return output
