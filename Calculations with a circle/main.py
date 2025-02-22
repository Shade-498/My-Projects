import math

def circle_area(radius): # S=πr^2
	return math.pi * radius ** 2

def circle_circumference(radius): # L=2πr
	return 2 * math.pi * radius

def circle_diameter(radius): # d=2r
	return 2 * radius

def circle_radius(diameter): # r=d/2
	return diameter / 2

radius = int(input("Enter a radius: "))
r = radius

def main():
	print(circle_area(r))
	print(circle_circumference(r))
	print(circle_diameter(r))
	print(circle_radius(r))

if __name__ == "__main__":
	main()