import math
def calculateStats(numbers):
    for num2 in numbers:
        num1=math.isnan(num2)
        print ("isnan:",num1)
        if num1==1:
           print ("istrue:",numbers)
           return numbers
        
        else:
            x=sum(num2)
            print ("sum",x)
            y=max(num2)
            z=min(num2)
            avg_value = sum(num2) / len(num2)
            print (avg_value,y,z)
            hash1 = {"avg": avg_value, "max": y,"min": z}
    
    
    return hash1

def calculateStats1():
    return True
