def  my_func(x1, x2, x3):
    counter = ((x1+x2+x3)*(x2+x3)*x3)
    denominator=(x1+x2+x3)
    if denominator == 0:
        print("Error: parameters hould be float!!")
    else:
            return counter/denominator;   
x1=input ("enter num 1")   
x2=input ("enter num 2") 
x3=input ("enter num 3")  
x1=float(x1)  
x2=float(x2)  
x3=float(x3)  
print(my_func(x1, x2, x3))
