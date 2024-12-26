"""
###
base62_encoder_decoder.py 
###

The goal with this script is to predictably encode and decode 7 digits <> 4 digits using base-62.
e.g.
    D052077 <-> 6JJX

some example codes:
D159098
D054080
B052077
"""

def letter_to_int(letter):
    if letter == 'A': return 0
    elif letter == 'B': return 1
    elif letter == 'C': return 2
    elif letter == 'D': return 3
    else: raise ValueError("Letter must be A, B, C, or D")

def int_to_letter(num):
    return ['A', 'B', 'C', 'D'][num]

def encode(input_str):
    if len(input_str) != 7 or not input_str[0].isalpha() or not input_str[1:].isdigit():
        raise ValueError("Input must be in LXXXYYY format where L is A, B, C, or D.")
    
    L = letter_to_int(input_str[0])
    XXX = int(input_str[1:4])
    YYY = int(input_str[4:])
    
    if XXX < 1 or XXX > 999 or YYY < 1 or YYY > 999:
        raise ValueError("XXX or YYY out of range (must be between 001 and 999)")

    number = (L * 999 * 999) + ((XXX - 1) * 999) + (YYY - 1)
    
    base62 = ""
    while number > 0:
        number, i = divmod(number, 62)
        if i < 10:
            base62 = chr(ord('0') + i) + base62
        elif i < 36:
            base62 = chr(ord('A') + i - 10) + base62
        else:
            base62 = chr(ord('a') + i - 36) + base62

    # Ensure we return exactly 4 characters by padding with '0' if necessary
    return base62.zfill(4)

def decode(encoded_str):
    if len(encoded_str) != 4:
        raise ValueError("Encoded string must be 4 characters long.")

    number = 0
    for char in encoded_str:
        if char.isdigit():
            number = number * 62 + (ord(char) - ord('0'))
        elif char.isupper():
            number = number * 62 + (ord(char) - ord('A') + 10)
        elif char.islower():
            number = number * 62 + (ord(char) - ord('a') + 36)
        else:
            raise ValueError("Invalid character in base-62 string")
    
    L = int_to_letter(number // (999 * 999))
    remainder = number % (999 * 999)
    XXX = (remainder // 999) + 1
    YYY = (remainder % 999) + 1

    return f"{L}{XXX:03d}{YYY:03d}"

# Test the functions
sample_codes = ["D159098", "D054080", "B052077", "A600600", "C599600"]
try:
    for code in sample_codes:
        original = code
        encoded = encode(original)
        decoded = decode(encoded)
        print(f"Original: {original}")
        print(f"Encoded: {encoded}")
        print(f"Decoded: {decoded}")
        print("---------")
except ValueError as e:
    print(f"Error: {e}")
    
    
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <https://unlicense.org>
