import math as m
a = float(input("Ширина элемента = "))

b = float(input("Длина элемента = "))
A = float(input("Ширина холста = "))
B = float(input("Длина холста = "))

def viches(a,b,A,B):
    res = ""
    chk1 = 0
    chk2 = 0
    print(A,"+",B)
    if (A >= a or A >= b) and (B >= a or B >= b):\
       
        if not(A >= b and B >= a):
            chk1 = 1

        if not(A >= a and B >= b):
            chk2 = 1
        
        if A >= a and B >= b and A//a >= B//a:
            print(A,":1:",B)
            print(A//a,">1>",B//a)
            res = "Г," * m.floor((A//a))
            print(res,"=1")
            res += viches(a,b,(A-(a*(A//a))),B) + viches(a,b,A,(B - b))

        
        if A >= b and B >= a and A//a <= B//a:
            res = "В," * m.floor((B//a))
            print(A,":2:",B)
            print(A//a,"<2<",B//a)
            print(res,"=2")
            res += viches(a,b,(A-b),B) + viches(a,b,A,B-(a*(B//a)))
            
        if chk2 == 0 and chk1 == 1 and m.floor(A//a) >= 0:
            print(A,"::1::",B)
            print(A//a,">>1>>",B//a)
            res = "Г," * m.floor((A//a))
            #print(res,"=1")
            res += viches(a,b,(A-(b*(A//a))),B) + viches(a,b,A,(B - b))

        if chk2 == 1 and chk1 == 0 and m.floor(B//a) >= 0:
            res = "В," * m.floor((B//a))
            print(A,"::2::",B)
            print(A//a,"<<2<<",B//a)
            print(res,"=2")
            res += viches(a,b,(A-b),B) + viches(a,b,A,B-(a*(B//a)))

        return(res)
    else:
        return("")
result = viches(a,b,A,B)
print("Вертикальных элементов: ",result.count("В"),"\nГоризонтальных элементов",result.count("Г"))
print("Вычесленная последовательность: ",result[:-1])
