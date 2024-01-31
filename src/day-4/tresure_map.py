row1 = ['⬜', '⬜', '⬜']
row2 = ['⬜', '⬜', '⬜']
row3 = ['⬜', '⬜', '⬜']
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
datas = input("Where do you want to put the treasure?\n")

column = int(datas[0]) - 1
row = int(datas[1]) - 1

map[row][column] = "x"

print(print(f"{row1}\n{row2}\n{row3}"))

# if row == 1:
#     row1[column] = "x"
#     print(f"{row1}\n{row2}\n{row3}")
# elif row == 2:
#     row2[column] = "x"
#     print(f"{row1}\n{row2}\n{row3}")
# else:
#     row3[column] = "x"
#     print(f"{row1}\n{row2}\n{row3}")
