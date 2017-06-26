a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
print("a: ",a)
print("b: ",b)
print("c: ",c)
m1 = list(map(lambda x,y:x+y, a,b))
print("a+b")
print(m1)
#[18, 14, 14, 14]
m2 = list(map(lambda x,y,z:x+y+z, a,b,c))
print("a+b+c")
print(m2)
#[17, 10, 19, 23]
m3 = list(map(lambda x,y,z : 2.5*x + 2*y - z, a,b,c))
print(' 2.5*a + 2*b')
print(m3)
#[37.5, 33.0, 24.5, 21.0]