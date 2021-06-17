"""
Author: Tyson Bradford
Prove 01: Review Python
"""
import math
front_width = float(input("Enter the width of your front tires in mm (ex 205): "))
front_aspect_ratio = float(input("Enter the aspect ratio of the front tire (ex 60): "))
front_diameter = float(input("Enter the diameter of the front tire in inches (ex 15): "))

front_volume = float(round(math.pi * front_width * 2 * front_aspect_ratio( front_width * front_aspect_ratio + 2,540 * front_diameter) / 10,000,000))
print(f"The approximate volume of your front tire is: {front_volume}")