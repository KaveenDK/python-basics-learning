import my_calculator.addition
import my_calculator.subtraction

sum = my_calculator.addition.add(10, 5)
difference = my_calculator.subtraction.subtract(10, 5)

print(f"Sum: {sum}")
print(f"Difference: {difference}")

# ------------------------------------------------------------

from my_calculator import addition, subtraction

sum = addition.add(10, 5)
difference = subtraction.subtract(10, 5)

print(f"Sum: {sum}")
print(f"Difference: {difference}")

# ------------------------------------------------------------

from my_calculator.addition import add
from my_calculator.subtraction import subtract

sum = add(10, 5)
difference = subtract(10, 5)

print(f"Sum: {sum}")
print(f"Difference: {difference}")

# ------------------------------------------------------------

from my_calculator import add, subtract

sum = add(10, 5)
difference = subtract(10, 5)

print(f"Sum: {sum}")
print(f"Difference: {difference}")