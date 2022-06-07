"""
Understand:
    all possible letter combinations that the number could represent
    
    1. Can a character be used multiple times?
        - no 
    2. Will digits ever be an empty string?
        - yes
        
    Test cases:
        Input: digits = "23"
        Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

        Input: digits = ""
        Output: []
        
        Input: digits = "2"
        Output: ["a","b","c"]
        
Match:
    - backtracking/recursion
    
Plan:
    - create a hashmap that maps a digit to its letters
    - iterate over the digits, find the combinations with 1 digit at a time
    - store all combinations in a set (pass by reference)
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        result = []
        map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        
        def backtrack(i, curString):
            if len(curString) == len(digits):
                result.append(curString)
                return
            else:
                for c in map[digits[i]]:
                    backtrack(i+1, curString + c)
    
        backtrack(0, "")
        return result