# ====================
# Problem 3:
# Language: Python
# Answer: 6857
# ====================

n = 600851475143
x = 0
y = 2

while n > 1:
    if n % y == 0:
        n = n / y
        if y > x:
            x = y
            y = 2
    else:
        y = y + 1

print(x)
