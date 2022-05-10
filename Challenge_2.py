# ====================
# Problem 2:
# Language: python
# Answer: 4613732
# ====================

x = 1
y = 2
temp_sum = 0
total_sum = 2

while temp_sum < 4000000:
    temp_sum = x + y
    if temp_sum % 2 == 0:
        total_sum += temp_sum
    
    x = y
    y = temp_sum
    
print(total_sum)
