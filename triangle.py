total= 10
space= total/2-1
space2= total-1
space3= total-1
#first method
for i in range(1,total+1):
    print space2*" ",
    for j in range(i):
        print "*",
    print "\n"
    space2= space2-1
    
#second method
for i in range(1,total+1,2):
    print space*" "+i*"*"
    space=space-1
    
#third method
for i in range(1,total+1):
    print space3*" "+i*"* "
    space3=space3-1
space3=0
for i in range(1,total)[::-1]:
    space3=space3+1
    print space3*" "+i*"* "
    


    
    
    
