
x=[5,0,1,2]
temp1=0 
temp=0
temp2=0
cont=0

for i in x:
           
    temp1=i
    temp=temp+temp1
    cont=cont+1

for i in x:
    if i > ((temp-i)/(cont-1)):
        
        temp2 = i
        print(temp2, " es lider")
    
    else:
        
        temp2=i
        print(temp2, " no es el lider")
                               

    