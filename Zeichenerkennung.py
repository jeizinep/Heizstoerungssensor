"""
     a
    ---
f |     | b
    -g-
e |     | c
    ---
     d
"""

def find_character(segment_values):
    # The predefined mapping (inverse of the previous dictionary)
    # (a, b, c, d, e, f, g): character
    inverse_segments = {
        (1, 1, 1, 1, 1, 1, 0): "0",
        (0, 1, 1, 0, 0, 0, 0): "1",
        (0, 0, 0, 0, 1, 1, 0): "1",
        (1, 1, 0, 1, 1, 0, 1): "2",
        (1, 1, 1, 1, 0, 0, 1): "3",
        (0, 1, 1, 0, 0, 1, 1): "4",
        (1, 0, 1, 1, 0, 1, 1): "5",
        (1, 0, 1, 1, 1, 1, 1): "6",
        (1, 1, 1, 0, 0, 0, 0): "7",
        (1, 1, 1, 1, 1, 1, 1): "8",
        (1, 1, 1, 1, 0, 1, 1): "9",
        (1, 0, 0, 0, 1, 1, 1): "F",
        (1, 0, 0, 1, 1, 1, 1): "E",
        (1, 1, 1, 0, 1, 1, 1): "A",
        (0, 0, 1, 1, 1, 1, 0): "L",
        (0, 1, 1, 0, 1, 1, 1): "H"
    }

    # Return the corresponding character or an error message
    return inverse_segments.get(segment_values, "Invalid combination")

# Example usage
example_segments = (0, 0, 0, 0, 0, 1, 1)
find_character(example_segments)
print(find_character(example_segments))