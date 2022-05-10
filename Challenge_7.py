# ====================
# Problem 7:
# Language: Python
# Answer: 104743
# Needs a more efficient solution
# ====================

primes = [2, 3, 5, 7, 9, 11] # we are given the first 6 primes in the prompt
size = 6
target = 10001
x = 12
i = 0
is_prime = 1

while size <= target:
    while i < size and is_prime == 1:
        if (x % primes[i] == 0):
            is_prime = 0
            
        i += 1
        
    if is_prime == 1:
        primes.append(x)
        size += 1
        #print(x) #debugging
    
    x += 1
    i = 0
    is_prime = 1

print(primes[target])
