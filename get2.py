# import nothing
# -*- coding: utf-8 -*-

def print_unicode_codes(text):
    print(f"字符长度: {len(text)}")
    for char in text:
        if char == "\n":
            print(r"字符: \n  Unicode码点: U+000A")
            continue
        elif char == " ":
            continue
            print(r"字符: [Space]  Unicode码点: U+0020")
            continue
        else:
            print(f"字符: {char}  的 码点 是 U+" + f"{ord(char):04X}")
            # print(f"字符: {ch} \t Unicode码点: U+" + hex(ord(ch))[2:].upper())

def print_txt_file_unicode_codes(file_path):
    print(f"正在打印以下文件的字符码点: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    print_unicode_codes(text)

txt_file = "hebrew_alphabet.txt"
txt_file = "tan.txt"
txt = "baozhi.txt"
txt = "window_icon.txt"
txt = "fraktur_CHIRZ.txt"
txt = "hand_dark.txt"
txt = "colors_of_hands.txt"
txt = "two_hands.txt"

print_txt_file_unicode_codes(txt)
