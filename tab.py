class diff:
    def __init__(self,a):
        self.__elements = a
    def comp(self):
        self.max = 0
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                temp = abs(a[i]-a[j])
                if self.max<temp:
                    self.max = temp
a = [1,2,5,10,10,10,10,10,10,10,10,10,10]
d = diff(a)
d.comp()
print(d.max)



