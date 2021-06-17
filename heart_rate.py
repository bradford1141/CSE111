"""
Author: Tyson Bradford
Assignment: Checkpoint 1
"""

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""

text = input("Please enter your age: ")

age = int(text)

max_rate = 220 - age
slowest = max_rate * 0.65
fastest = max_rate * 0.85

print("When you exercise to strengthen your heart, you should keep")
print(f"your heart rate between {slowest:.0f} and {fastest:.0f} beats per minute.")
