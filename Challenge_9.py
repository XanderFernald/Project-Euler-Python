# ====================
# Problem 9
# Language: Python
# Answer: 31875000
# ====================

M = 1
N = 1
A = 0
B = 0
C = 0

# 2 positive whole numbers, M and N such that N < M
# A = M^2 - N^2
# B = (MN)*2
# C = M^2 + N^2
# For this problem, A + B + C must equal 1000

while N < 500:
    M = N + 1
    while M < 500:
        A = (M * M) - (N *  N)
        B = (M * N) * 2
        C = (M * M) + (N * N)
        if A + B + C == 1000:
            print(A)
            print(B)
            print(C)
            print(A*B*C)
        M += 1
    N += 1
    
print("done")
