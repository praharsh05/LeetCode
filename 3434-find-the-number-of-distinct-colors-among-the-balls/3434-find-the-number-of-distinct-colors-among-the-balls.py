class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Variable to keep track of result
        res = []
        # Dictionary to map color change after every query
        ball_map = {}
        # Counter to keep track of how many times each color is used across all balls
        color_freq = Counter()

        # Iterate over the queries
        for ball, color in queries:
            # If ball is already colored
            if ball in ball_map:
                # Get the old color
                old_color = ball_map[ball]
                # Reduce the counter of old color by 1
                color_freq[old_color] -= 1
                # if the old color's counter reaches 0 then remove it from the counter all together
                if color_freq[old_color] == 0:
                    del color_freq[old_color]
            
            # Add the color to the dictionary and counter
            ball_map[ball] = color
            color_freq[color] += 1

            # Add the length of color_freq to result
            res.append(len(color_freq))
        
        return res