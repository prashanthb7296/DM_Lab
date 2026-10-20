# Program 2: Calculate Mean, Median, and Mode

import statistics

marks = (65, 72, 80, 72, 90, 68, 75)

mean_value = statistics.mean(marks)
median_value = statistics.median(marks)
mode_value = statistics.mode(marks)

print(f"Mean    = {mean_value:.2f}")
print(f"Median = {median_value}")
print(f"Mode    = {mode_value}")