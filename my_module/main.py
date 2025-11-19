import addition

result = addition.add(5, 7)
print(f"The Result of Addition is: {result}")

# -----------------------------------------------

import addition  as ad

result = ad.add(5, 7)
print(f"The Result of Addition is: {result}")

# -----------------------------------------------

from addition import add

# print(add(5, 7))
print(f"The Result of Addition is: {add(5, 7)}")

# -----------------------------------------------