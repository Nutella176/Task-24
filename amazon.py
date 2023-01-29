def min(numbers):
    return min(numbers)


def max(numbers):
    return max(numbers)


def avg(numbers):
    return sum(numbers) / len(numbers)
  
input_file = open("input.txt", "r", encoding= "utf-8")
output_file = open("output.txt", "w", encoding= "utf-8")

for line in input_file:
    operation, numbers_str = line.strip().split(":")
    numbers = list(map(int, numbers_str.split(",")))
    if operation == "min":
        result = min(numbers)
        output_file.write(f"The min of {numbers} is {result}.\n")
    elif operation == "max":
        result = max(numbers)
        output_file.write(f"The max of {numbers} is {result}.\n")
    elif operation == "avg":
        result = avg(numbers)
        output_file.write(f"The avg of {numbers} is {result}.\n")
    break 

input_file.close()
output_file.close()


