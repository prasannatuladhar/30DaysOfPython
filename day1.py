# Day 1
# Print your age to the console.
# Calculate and print the number of days, weeks, and months in 27 years. Don’t worry about leap years!
# Calculate and print the area of a circle with a radius of 5 units. You can be as accurate as you like with the value of pi.

print("My age is 25 years old")

year=27
number_of_days=year*365
number_of_months=year*12
number_of_weeks=12*4*year
print(f"{year} years have {number_of_days} days , {number_of_months} weeks and {number_of_weeks} weeks")

radius=5
pi=3.1415
area_of_circle=pi*radius**2
result=round(area_of_circle,2)
print(f"area of circle is {result}")