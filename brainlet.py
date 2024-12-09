#!/usr/bin/env python3

import sys

try:
    import unicodedata
    is_double_width = lambda c: \
        unicodedata.east_asian_width(c) in ['F', 'W']
except:
    is_double_width = lambda _: False

raw_glyphs = {
    "A": """
╭─╮
├─┤
╵ ╵
""",
    "a": """
╭─╮
╭─┤
╰─╯
""",
    "B": """
┌╮ 
├┴╮
└─╯
""",
    "b": """
╷  
├─╮
└─╯
""",
    "C": """
╭─╮
│  
╰─╯
""",
    "c": """
╭─╮
│  
╰─╯
""",
    "D": """
┌─╮
│ │
└─╯
""",
    "d": """
  ╷
╭─┤
╰─┘
""",
    "E": """
╭─╴
├─╴
╰─╴
""",
    "e": """
╭─╮
├─┘
╰─╯
""",
    "F": """
╭─╴
├─╴
╵  
""",
#     "f": """
# ╭─╴
# ┼─╴
# ╵  
# """,
    "f": """
 ╭─
╶┼─
 ╵ 
""",
    "G": """
╭─╴
│╶┐
╰─╯
""",
    "g": """
╭─╮
╰─┤
╰─╯
""",
    "H": """
╷ ╷
├─┤
╵ ╵
""",
    "h": """
╷  
├─╮
╵ ╵
""",
    "I": """
╶┬╴
 │ 
╶┴╴
""",
#     "i": """
#  ╷ 
#  ╭╴
# ╶┴╴
# """,
    "i": """
 ╷ 
╶┐ 
╶┴╴
""",
    "J": """
  ╷
  │
╰─╯
""",
    "j": """
  ╷
  ╷
╰─╯
""",
    "K": """
╷╭ 
├┴╮
╵ ╰
""",
    "k": """
╷╭ 
├┴╮
╵ ╰
""",
    "L": """
╷  
│  
└─╴
""",
    "l": """
╶╮ 
 │ 
╶┴╴
""",
    "M": """
╭┬╮
│││
╵ ╵
""",
    "m": """
╭┬╮
│││
╵ ╵
""",
    "N": """
╭┐╷
│││
╵└╯
""",
    "n": """
┌─╮
│ │
╵ ╵
""",
    "O": """
╭─╮
│ │
╰─╯
""",
    "o": """
╭─╮
│ │
╰─╯
""",
    "P": """
╭─╮
├─╯
╵  
""",
    "p": """
╭─╮
├─╯
╵  
""",
    "Q": """
╭─╮
│╶┼
╰─╯
""",
    "q": """
╭─╮
╰─┤
  ╰
""",
    "R": """
╭─╮
├┬╯
╵╰ 
""",
    "r": """
╭─╮
│  
╵  
""",
    "S": """
╭─╮
╰─╮
╰─╯
""",
    "s": """
╭─╮
╰─╮
╰─╯
""",
    "T": """
─┬─
 │ 
 ╵ 
""",
    "t": """
 ╷ 
╶┼╴
 ╰╴
""",
    "U": """
╷ ╷
│ │
╰─╯
""",
    "u": """
╷ ╷
│ │
╰─┘
""",
    "V": """
╶╮╷
 ││
 ╰╯
""",
    "v": """
╶╮╷
 ││
 ╰╯
""",
    "W": """
╷ ╷
│││
╰┴╯
""",
    "w": """
╷ ╷
│││
╰┴╯
""",
    "X": """
╭┬╮
 │ 
╰┴╯
""",
    "x": """
╭┬╮
 │ 
╰┴╯
""",
    "Y": """
╷ ╷
╰┬╯
 ╵ 
""",
    "y": """
╷ ╷
╰─┤
╰─╯
""",
    "Z": """
╶─╮
╭─╯
╰─╴
""",
    "z": """
╶─╮
╭─╯
╰─╴
""",

    "1": """
╶┐ 
 │ 
╶┴╴
""",
    "2": """
╶─╮
╭─╯
└─╴
""",
    "3": """
╶─╮
╶─┤
╶─╯
""",
    "4": """
╷ ╷
└─┤
  ╵
""",
    "5": """
┌─╴
╰─╮
╰─╯
""",
    "6": """
╭─╴
├─╮
╰─╯
""",
    "7": """
╶─┐
  ┼
  ╵
""",
    "8": """
╭─╮
├─┤
╰─╯
""",
    "9": """
╭─╮
╰─┤
╰─╯
""",
    "0": """
╭─╮
│││
╰─╯
""",
    "{": """
╭╴ 
┤  
╰╴ 
""",
    "}": """
 ╶╮
  ├
 ╶╯
""",
    "(": """
 ╭ 
 │ 
 ╰ 
""",
    ")": """
 ╮ 
 │ 
 ╯ 
""",
    "[": """
┌╴ 
│  
└╴ 
""",
    "]": """
 ╶┐
  │
 ╶┘
""",
    "~": """
╭─╯
   
   
""",
    "`": """
 ╰ 
   
   
""",
    "'": """
 ╯ 
   
   
""",
    ".": """
   
   
 . 
""",
    ",": """
   
   
 , 
""",
    "-": """
   
╶─╴
   
""",
    "+": """
   
╶┼╴
   
""",
    "=": """
   
╶─╴
╶─╴
""",
    '"': """
 ╷╷
   
   
""",
    "?": """
╶─╮
╭─╯
╷  
""",
    "!": """
 ╷ 
 ╵ 
 ╵ 
""",
    "&": """
╭╮ 
╭┼╯
╰╯ 
""",
    "$": """
╭┴╮
╰─╮
╰┬╯
""",
    "%": """
╭╮╷
╰┼╮
╵╰╯
""",
    "@": """
╭─╮
├╮│
╰╯╯
""",
    "^": """
 ╭╮
 ││
 ╵╵
""",
    "#": """
┼─┼
┼─┼
   
""",
}

glyphs = {
    k: v.split("\n")[1:-1]
        for k, v in raw_glyphs.items()
}

def brainlet(s):
    output_buffers = [[], [], []]
    for letter in s:
        if not letter.isprintable():
            continue
        try:
            glyph_lines = glyphs[letter]

            for i, line in enumerate(glyph_lines):
                output_buffers[i].append(line)
        except KeyError:
            output_buffers[0].append("   ")
            output_buffers[1].append(" ")
            output_buffers[1].append(letter)
            if not is_double_width(letter):
                output_buffers[1].append(" ")
            output_buffers[2].append("   ")
    return output_buffers

def print_brainlet(s):
    output_buffers = brainlet(s)
    for output_buffer in output_buffers:
        print("".join(output_buffer))

def main():
    if len(sys.argv) > 1:
        print_brainlet(" ".join(sys.argv[1:]))
    else:
        try:
            for line in sys.stdin:
                if line.endswith("\n"):
                    line = line[:-1]
                print_brainlet(line)
        except EOFError:
            exit(0)
        except KeyboardInterrupt:
            print()
            exit(1)

if __name__ == "__main__":
    main()
