INVERSE_SEGMENTS = {
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

def find_character(segment_values):
    """
    Maps segment values to characters based on the predefined mapping.

    Parameters:
    segment_values (list of tuples): The segment values to map to characters.

         a
        ---
    f |     | b
        -g-
    e |     | c
        ---
         d

    Returns:
    list of str: The characters corresponding to the segment values. If a segment value does not correspond to a character, the character is None.
    """
    digits = []
    for i in range(len(segment_values)):
        character = INVERSE_SEGMENTS.get(tuple(segment_values[i]))
        if character is None:
            print("Invalid combination")
            digits.append(None)
        else:
            digits.append(character)
    return digits
