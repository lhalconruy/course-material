def is_alpha(input):
    linput = list(input)
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z"]

    for i in linput:
        if (i in alphabet) or (i.lower() in alphabet):
            return True
    return False

print(is_alpha('2a'))
