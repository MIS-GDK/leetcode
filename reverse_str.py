def reverse_str(strnums: list) -> list:
    if len(strnums) == 1:
        return strnums
    else:
        return reverse_str(strnums[1:]) + strnums[0]


print(reverse_str('ABCDEFG'))
