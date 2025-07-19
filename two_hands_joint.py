hand1 = "\U0001FAF1"
color1_list = [None, "\U0001F3FB","\U0001F3FC", "\U0001F3FD", "\U0001F3FE", "\U0001F3FF"]
hand2 = "\U0001FAF2"
color2 = "\U0001F3FC"
color2_list = [None, "\U0001F3FB","\U0001F3FC", "\U0001F3FD", "\U0001F3FE", "\U0001F3FF"]
joiner = "\u200D"
for color1 in color1_list:
    for color2 in color2_list:
        if color1 is None and color2 is None:
            two_hands = hand1 + joiner + hand2
        elif color1 is None:
            two_hands = hand1 + joiner + hand2 + color2
        elif color2 is None:
            two_hands = hand1 + color1 + joiner + hand2
        else:
            two_hands = hand1 + color1 + joiner + hand2 + color2
        print(two_hands)
# two_hands = hand1 + joiner + hand2
# two_hands = hand1 + color1 + joiner + hand2 + color2
# print(two_hands)