rows = range(1,4)  # 1, 2, 3
cols = range(1,3) # 1, 2
cells = [(row, col) for row in rows for col in cols]


# print(cells)

for cell in cells:
    print(cell)

# print(cells)


for row, col in cells:
    print(row, col)


