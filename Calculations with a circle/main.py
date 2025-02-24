import math

def circle_area(radius):  # S = πr^2
    return math.pi * radius ** 2

def circle_circumference(radius):  # L = 2πr
    return 2 * math.pi * radius

def circle_diameter(radius):  # d = 2r
    return 2 * radius

def circle_radius(diameter):  # r = d / 2
    return diameter / 2

def main():
    while True:

        user_input = input("Enter a radius (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Exiting the program. Goodbye!")
            break

        radius = float(user_input)

        diameter = circle_diameter(radius)
        print(f"Area of the circle: {circle_area(radius)}")
        print(f"Circumference of the circle: {circle_circumference(radius)}")
        print(f"Diameter of the circle: {diameter}")
        print(f"Radius from diameter: {circle_radius(diameter)}")
        print("-" * 30)  # Divider


if __name__ == "__main__":
    main()