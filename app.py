# Define each character as a list of 7 booleans
SEGMENTS = {
    "0": [1,1,1,0,1,1,1],
    "1": [0,0,1,0,0,1,0],
    "2": [1,0,1,1,1,0,1],
    "3": [1,0,1,1,0,1,1],
    "4": [0,1,1,1,0,1,0],
    "5": [1,1,0,1,0,1,1],
    "6": [1,1,0,1,1,1,1],
    "7": [1,0,1,0,0,1,0],
    "8": [1,1,1,1,1,1,1],
    "9": [1,1,1,1,0,1,1],
    " ": [0,0,0,0,0,0,0],
    "e": [1,1,0,1,1,0,1],
}

# Default blank character
BLANK = [0] * 7

def render_character(segments):
    def seg(num,seg):
        return f'{seg}' if segments[num] == 1 else ' '
    """
     __
    |__|
    |__|
    """
    """Returns a string representation of a single 7-segment character."""
    return [
        f" {seg(0,"_")*2} ",
        f"{seg(1,"|")}{seg(3,"_")*2}{seg(2,"|")}",
        f"{seg(4,"|")}{seg(6,"_")*2}{seg(5,"|")}"
    ]

def render_display(text):
    """Takes a string and renders it as a 7-segment display."""
    lines = ["", "", ""]

    for char in text:
        segments = SEGMENTS.get(char.upper(), BLANK)  # Get segment data
        char_lines = render_character(segments)  # Convert to display format
        for i in range(3):
            lines[i] += char_lines[i] + "  "  # Add spacing between chars

    return "\n".join(lines)

print(render_display("123"))
print(render_display("e"))

"""
 ____
|\\//|
|//\\|
"""