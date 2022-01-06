"""Calculate area of the inner square"""

r = int(input("Enter radius: "))
area_big = 4 * (r ** 2)
area_small = 2 * (r ** 2)

print("The area of the outer square is: " + str(area_big))
print("The area of the inner square is: " + str(area_small))
