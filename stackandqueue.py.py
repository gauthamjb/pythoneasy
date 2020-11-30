a= input("ENTER THE NAMES: ").split()
b=input("ENTER S-STACK OR Q-QUEUE: ")
c=len(a)
while c>0:
    if b=="Q":
        print("The List is",a)
        if len(a) == 0:
            break
        print("removed str is",a.pop())
        
    elif b=="S":
        print("The List is",a)
        if len(a) == 0:
            break       
        print("removed str is",a.pop(0))
    else:
        print("ENTER EITHER 'S' OR 'Q'")
        break
        

        
 
        
    
    
