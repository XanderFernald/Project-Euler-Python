# ====================
# Problem 1:
# Language: Python
# Answer: 233168
# ====================

x = 0
s = 0

while (x < 1000):
    if x % 3 == 0 or x % 5 == 0:
        s += x
        
    x += 1

print(s)
