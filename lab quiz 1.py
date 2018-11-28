print("Saifullah Shaikh, 18B-092-CS, A \nLAB-05 QUIZ \nQUESTION 1")
#A function to generate armstrong number
def armstrong():
    'Returns the sum of cube of each digit'
    no = (input("Please enter the number in digits: "))
    ab = 0
    for i in range(len(no)):
        a = no[i]
        res = int(a)**3
        ab = ab + res
    if ab == int(no):
        print("The given number is Armstrong Nmuber!")
    else:
        print("The given number is not a Armstrong Number!")
            
    return(ab)   
        
        
        
    
        
            
        
