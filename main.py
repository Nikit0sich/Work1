Flag = True
while Flag:
    star = "* "
    three_line = star * 3
    two_line = " " + star * 2
    one_line = "  " + star
    big_star = one_line + "\n" + two_line + "\n" + three_line
    inverse_big_star = three_line + "\n" + two_line + "\n" + one_line
    Flag = False
print(big_star, end=' ')
print(inverse_big_star)