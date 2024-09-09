


#input
x1 = float(input("Enter X1 coordinates: "))
y1 = float(input("Enter Y1 coordinates: "))
x2 = float(input("Enter X2 coordinates: "))
y2 = float(input("Enter Y2 coordinates: "))

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("The distance between the two points is: ", distance)