C = [39.2, 36.5, 37.3, 38, 37.8]
print("C is initially ",C)
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print("Now F is ",F)
#[39.2, 36.5, 37.300000000000004, 38.00000000000001, 37.8]
C = list(map(lambda x: (float(5)/9)*(x-32), F))
print("Again C is ",C)
#[39.2, 36.5, 37.300000000000004, 38.00000000000001, 37.8]

