print ("1 _ add")
print ("2 _ subtract")
print ("3 _ multiply")
print ("4 _divison")

option = int (input("choose an operation:"))

num1 = float(input ("enter firt number:")) 
num2 = float(input ("enter second number:"))

if (option==1):
    
    result= num1 + num2
    print(result)
elif(option==2):

    result= num1 - num2
    print(result)
elif(option==3):
    result= num1 * num2
    print(result)
    
elif(option==4):
    result= num1 / num2
    print(result)
    
else:
    print("invalid operation enterd")
     
     
    #print("the result of the operation is []".format(results))   


    
    
    
    
    


