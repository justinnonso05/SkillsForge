class StringCompressor:
    def compress(self, string: str) -> str:
        if not string:
            return ""
        
        compressed = []
        count = 1
        current_char = string[0]
        
        for i in range(1, len(string)):
            if string[i] == current_char:
                count += 1
            else:
                compressed.append(current_char + str(count))
                current_char = string[i]
                count = 1
        
        # Append the last set of characters
        compressed.append(current_char + str(count))
        
        compressed_string = ''.join(compressed)
        
        # Return the original string if compression doesn't reduce the length
        return compressed_string if len(compressed_string) < len(string) else string

# Test cases
sol = StringCompressor()
assert sol.compress('bbcceeee') == 'b2c2e4'
assert sol.compress('aaabbbcccaaa') == 'a3b3c3a3'
assert sol.compress('a') == 'a'