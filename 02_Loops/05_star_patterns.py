rows = int(input("Enter number of rows: "))
if rows <= 0:
    print("Rows must be positive.")
else:
    print("\\nTriangle:")
    for i in range(1, rows + 1):
        print("* " * i)

    print("\\nPyramid:")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

    print("\\nDiamond:")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "* " * (2 * i - 1))
