# ====================
# Problem 4:
# Language: Python
# Answer: 906609
# ====================

y = 999
largest = -1

while y > 99:
    z = 999
    
    while z > 99:
        x = str(y * z)
        loc1 = 0
        loc2 = len(x) - 1
        flag = 1
        
        while loc2 > loc1:
            if x[loc1] != x[loc2]:
                flag = 0

            loc1 += 1
            loc2 -= 1
        
        if flag == 1 and (y * z) > largest:
            largest = y * z
        
        z -= 1
        
    y -= 1

print(largest)
