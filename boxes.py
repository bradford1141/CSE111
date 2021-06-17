"""
Author: Tyson Bradford
Purpose: python boxes program
"""

import math
number_items = int(input(f"Input the number of items being packaged: "))
items_per_box= int(input(f"Input the number of items being packaged in each box: "))

number_boxes = math.ceil(number_items / items_per_box)

print(f"For {number_items} items, packing {items_per_box} items in each box, you will need {number_boxes} boxes.")