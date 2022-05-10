# ====================
# Problem 6:
# Language: Python
# Answer: 25164150
# ====================

x = 1
sum_squares = 0
square_sum = 0

while x <= 100:
    
    sum_squares += (x*x)
    square_sum += x
    x += 1

square_sum = (square_sum*square_sum)

print(square_sum)
print(sum_squares)
print(square_sums - sum_squares)
