"""Define a function called areaOfRectangle"""
def area(sidelength1, sidelength2):
    """Define a function called areaOfRectangle"""
    return sidelength1 * sidelength2

SIDE1 = float(input("Input side 1: "))
SIDE2 = float(input("Input side 2: "))

AREA_SUM = area(SIDE1, SIDE2)

print("Area: " + str(AREA_SUM))
