# Program to store and analyze weekly temperatures
temperatures = []

for i in range(7):
    temp = float(input(f"Enter temperature for day {i + 1}: "))
    temperatures.append(temp)

lowest_temp = min(temperatures)
highest_temp = max(temperatures)
total_temp = sum(temperatures)
average_temp = total_temp / len(temperatures)

print("\n--- Weekly Temperature Summary ---")
print(f"Temperatures: {temperatures}")
print(f"Lowest Temperature: {lowest_temp}")
print(f"Highest Temperature: {highest_temp}")
print(f"Sum of Temperatures: {total_temp}")
print(f"Average Temperature: {average_temp:.2f}")