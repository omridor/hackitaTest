def gimatria(string):
    value = 0
    for char in string:
        value += gimatria_char(c)

def gimatria_char(c):
    if ord(c) not in range(ord("א"), ord("ת")):
        return
    index = ord(c) - ord("א")
    return index

def char_index(c):
    if ord(c) not in range(ord("א"), ord("ת")):
        return 0
    return ord(c) - ord("א")


char_index("א")
