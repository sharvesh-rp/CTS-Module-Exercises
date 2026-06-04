def display_coordinates(coords):
    if len(coords) != 2:
        return "Invalid Input"

    x, y = coords  # Multiple assignment
    x = float(x)
    y = float(y)

    return f"X Coordinate: {x}\n Y Coordinate: {y}"


def main():
    coords = input("Enter Coordinates (x,y): ").split(",")

    result = display_coordinates(coords)
    print(result)


main()