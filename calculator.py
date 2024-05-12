print("==================")
print("Area Calculator 📐")
print("==================")

print("Welcome to the Shape Area Calculator!")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")

choice = int(input("Enter your choice (1/2/3/4): "))

if choice == 1:
    side = float(input("Enter the length of the side of the square: "))
    area = side ** 2
    print("The area of the square is:", area)
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is:", area)
elif choice == 3:
    height = float(input("Enter the height of the triangle: "))
    base = float(input("Enter the base length of the triangle: "))
    area = (height * base) / 2
    print("The area of the triangle is:", area)
elif choice == 4:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius ** 2
    print("The area of the circle is:", area)
else:
    print("Invalid choice!")

