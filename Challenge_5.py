# ====================
# Problem 5:
# Language: Python
# Answer: 232792560
# Needs a more efficient solution
# ====================

x = 1
y = 1
while x < 21:
    if y % x != 0:
        y += 1
        x = 1
    
    x += 1

print(y)
