"""
Author: Tyson Bradford
Prove 01: Review Python
"""
import math

width = int(input("Please enter the width of the tire in mm (ex 205): "))
aspect = int(input("Please enter the aspect ration of the tire (ex 60): "))
diameter = int(input("Please enter the diameter of the tire in inches (ex 15): "))

volume = (math.pi * width ** 2 * aspect * (width * aspect + 2540 * diameter)) / 10000000

print()

print(f"The dementions of your tire are {width}/{aspect}R{diameter}. \n\ The volume size of your tire is appoximently {volume:.1f}")