class FirstNonRepeatingFinder:
    def first_non_repeating(self, string: str) -> str:
        char_count = {}
        
        # Count the occurrences of each character
        for char in string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Find the first character with a count of 1
        for char in string:
            if char_count[char] == 1:
                return char
        
        return -1

# Test cases for first non-repeating character
sol = FirstNonRepeatingFinder()
print(sol.first_non_repeating('swiss'))  