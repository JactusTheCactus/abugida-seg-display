# Define each character as a list of 7 booleans
SEGMENTS = {
    "0": [True, True, True, False, True, True, True],
    "1": [False, False, True, False, False, True, False],
    "2": [True, False, True, True, True, False, True],
    "3": [True, False, True, True, False, True, True],
    "4": [False, True, True, True, False, True, False],
    "5": [True, True, False, True, False, True, True],
    "6": [True, True, False, True, True, True, True],
    "7": [True, False, True, False, False, True, False],
    "8": [True, True, True, True, True, True, True],
    "9": [True, True, True, True, False, True, True],
    "A": [True, True, True, True, True, True, False],
    "b": [False, True, False, True, True, True, True],
    "C": [True, True, False, False, True, False, True],
    "d": [False, False, True, True, True, True, True],
    "E": [True, True, False, True, True, False, True],
    "F": [True, True, False, True, True, False, False],
}

# Default blank character
BLANK = [False] * 7

def render_character(segments):
    """Returns a string representation of a single 7-segment character."""
    return [
        " _ " if segments[0] else "   ",
        f"{'|' if segments[1] else ' '} {'|' if segments[2] else ' '}",
        " _ " if segments[3] else "   ",
        f"{'|' if segments[4] else ' '} {'|' if segments[5] else ' '}",
        " _ " if segments[6] else "   ",
    ]

def render_display(text):
    """Takes a string and renders it as a 7-segment display."""
    lines = ["", "", "", "", ""]

    for char in text:
        segments = SEGMENTS.get(char.upper(), BLANK)  # Get segment data
        char_lines = render_character(segments)  # Convert to display format
        for i in range(5):
            lines[i] += char_lines[i] + "  "  # Add spacing between chars

    return "\n".join(lines)

# Example usage
text = "HELLO123"
print(render_display(text))
